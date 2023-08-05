from __future__ import absolute_import, division, print_function

import uuid

import numpy as np

from glue.core.exceptions import IncompatibleAttribute
from glue.utils import categorical_ndarray

from .multi_scatter import MultiColorScatter
from .layer_state import ScatterLayerState
from ..common.layer_artist import VispyLayerArtist

COLOR_PROPERTIES = set(['color_mode', 'cmap_attribute', 'cmap_vmin', 'cmap_vmax', 'cmap', 'color'])
SIZE_PROPERTIES = set(['size_mode', 'size_attribute', 'size_vmin', 'size_vmax',
                       'size_scaling', 'size'])
ALPHA_PROPERTIES = set(['alpha'])
DATA_PROPERTIES = set(['layer', 'x_att', 'y_att', 'z_att'])
VISIBLE_PROPERTIES = set(['visible'])


class ScatterLayerArtist(VispyLayerArtist):
    """
    A layer artist to render 3d scatter plots.
    """

    def __init__(self, vispy_viewer, layer=None, layer_state=None):

        super(ScatterLayerArtist, self).__init__(layer)

        self._clip_limits = None

        # Set data caches
        self._marker_data = None
        self._color_data = None
        self._size_data = None

        self.layer = layer or layer_state.layer
        self.vispy_widget = vispy_viewer._vispy_widget

        # TODO: need to remove layers when layer artist is removed
        self._viewer_state = vispy_viewer.state
        self.state = layer_state or ScatterLayerState(layer=self.layer)
        if self.state not in self._viewer_state.layers:
            self._viewer_state.layers.append(self.state)

        # We create a unique ID for this layer artist, that will be used to
        # refer to the layer artist in the MultiColorScatter. We have to do this
        # rather than use self.id because we can't guarantee the latter is
        # unique.
        self.id = str(uuid.uuid4())

        # We need to use MultiColorScatter instance to store scatter plots, but
        # we should only have one per canvas. Therefore, we store the
        # MultiColorScatter instance in the vispy viewer instance.
        if not hasattr(self.vispy_widget, '_multiscat'):
            multiscat = MultiColorScatter()
            multiscat.set_gl_state(depth_test=False,
                                   blend=True,
                                   blend_func=('src_alpha', 'one_minus_src_alpha'))

            self.vispy_widget.add_data_visual(multiscat)
            self.vispy_widget._multiscat = multiscat

        self._multiscat = self.vispy_widget._multiscat
        self._multiscat.allocate(self.id)
        self._multiscat.set_zorder(self.id, self.get_zorder)

        # Watch for changes in the viewer state which would require the
        # layers to be redrawn
        self._viewer_state.add_global_callback(self._update_scatter)
        self.state.add_global_callback(self._update_scatter)

        self.reset_cache()

    def reset_cache(self):
        self._last_viewer_state = {}
        self._last_layer_state = {}

    @property
    def visual(self):
        return self._multiscat

    def get_zorder(self):
        return self.zorder

    def get_layer_color(self):
        if self.state.color_mode == 'Fixed':
            return self.state.color
        else:
            return self.state.cmap

    def redraw(self):
        """
        Redraw the Vispy canvas
        """
        if self._multiscat is not None:
            self._multiscat._update()
        self.vispy_widget.canvas.update()

    def clear(self):
        """
        Clear the visualization for this layer
        """
        self._multiscat.set_data_values(self.id, [], [], [])

    def remove(self):
        """
        Remove the layer artist from the visualization
        """

        if self._multiscat is None:
            return

        self._multiscat.deallocate(self.id)
        self._multiscat = None

        self._viewer_state.remove_global_callback(self._update_scatter)
        self.state.remove_global_callback(self._update_scatter)

    def _update_sizes(self):
        if self.state.size_mode is None:
            pass
        elif self.state.size_mode == 'Fixed':
            self._multiscat.set_size(self.id, self.state.size * self.state.size_scaling)
        else:
            data = self.layer[self.state.size_attribute].ravel()
            if isinstance(data, categorical_ndarray):
                data = data.codes
            if self.state.size_vmax == self.state.size_vmin:
                size = np.ones(data.shape) * 10
            else:
                size = (20 * (data - self.state.size_vmin) /
                        (self.state.size_vmax - self.state.size_vmin))
            size_data = size * self.state.size_scaling
            size_data[np.isnan(data)] = 0.
            self._multiscat.set_size(self.id, size_data)

    def _update_colors(self):
        if self.state.color_mode is None:
            pass
        elif self.state.color_mode == 'Fixed':
            self._multiscat.set_color(self.id, self.state.color)
        else:
            data = self.layer[self.state.cmap_attribute].ravel()
            if isinstance(data, categorical_ndarray):
                data = data.codes
            if self.state.cmap_vmax == self.state.cmap_vmin:
                cmap_data = np.ones(data.shape) * 0.5
            else:
                cmap_data = ((data - self.state.cmap_vmin) /
                             (self.state.cmap_vmax - self.state.cmap_vmin))
            cmap_data = self.state.cmap(cmap_data)
            cmap_data[:, 3][np.isnan(data)] = 0.
            self._multiscat.set_color(self.id, cmap_data)

    def _update_alpha(self):
        self._multiscat.set_alpha(self.id, self.state.alpha)

    def _update_data(self, event=None):

        try:
            x = self.layer[self._viewer_state.x_att].ravel()
            y = self.layer[self._viewer_state.y_att].ravel()
            z = self.layer[self._viewer_state.z_att].ravel()
        except AttributeError:
            return
        except (IncompatibleAttribute, IndexError):
            # The following includes a call to self.clear()
            self.disable_invalid_attributes(self._viewer_state.x_att,
                                            self._viewer_state.y_att,
                                            self._viewer_state.z_att)
            return
        else:
            self._enabled = True

        self._marker_data = np.array([x, y, z]).transpose()

        # We need to make sure we update the sizes and colors in case
        # these were set as arrays, since the size of the data might have
        # changed (in the case of subsets)

        self._multiscat.set_data_values(self.id, x, y, z)

        # Mask points outside the clip limits
        if self._clip_limits is None:
            self._multiscat.set_mask(self.id, None)
        else:
            xmin, xmax, ymin, ymax, zmin, zmax = self._clip_limits
            keep = (x >= xmin) & (x <= xmax) & (y >= ymin) & (y <= ymax) & (z >= zmin) & (z <= zmax)
            self._multiscat.set_mask(self.id, keep)

        self.redraw()

    def _update_visibility(self):
        self._multiscat.set_visible(self.id, self.visible)
        self.redraw()

    @property
    def default_limits(self):
        if self._marker_data is None:
            raise ValueError("Data not yet set")
        dmin = np.nanmin(self._marker_data, axis=0)
        dmax = np.nanmax(self._marker_data, axis=0)
        # TODO: the following can be optimized
        return tuple(np.array([dmin, dmax]).transpose().ravel())

    def set_clip(self, limits):
        self._clip_limits = limits
        self._update_data()

    def _update_scatter(self, force=False, **kwargs):

        if (self._viewer_state.x_att is None or
            self._viewer_state.y_att is None or
            self._viewer_state.z_att is None or
                self.state.layer is None):
            return

        # Figure out which attributes are different from before. Ideally we shouldn't
        # need this but currently this method is called multiple times if an
        # attribute is changed due to x_att changing then hist_x_min, hist_x_max, etc.
        # If we can solve this so that _update_histogram is really only called once
        # then we could consider simplifying this. Until then, we manually keep track
        # of which properties have changed.

        changed = set()

        if not force:

            for key, value in self._viewer_state.as_dict().items():
                if value != self._last_viewer_state.get(key, None):
                    changed.add(key)

            for key, value in self.state.as_dict().items():
                if value != self._last_layer_state.get(key, None):
                    changed.add(key)

        self._last_viewer_state.update(self._viewer_state.as_dict())
        self._last_layer_state.update(self.state.as_dict())

        if force or len(changed & DATA_PROPERTIES) > 0:
            self._update_data()
            force = True

        if force or len(changed & SIZE_PROPERTIES) > 0:
            self._update_sizes()

        if force or len(changed & COLOR_PROPERTIES) > 0:
            self._update_colors()

        if force or len(changed & ALPHA_PROPERTIES) > 0:
            self._update_alpha()

        if force or len(changed & VISIBLE_PROPERTIES) > 0:
            self._update_visibility()

    def update(self):
        with self._multiscat.delay_update():
            self._update_scatter(force=True)
        self.redraw()
