# -*- coding: utf-8 -*-
from enthought.mayavi import mlab
from tvtk_rectilineargrid import r
from figure_imagedata import plot_cell

if __name__ == "__main__":
    mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    mlab.clf()
    mlab.pipeline.surface(mlab.pipeline.extract_edges(r), color=(0, 0, 0))
    mlab.pipeline.glyph(r, mode='sphere', scale_factor=0.5, scale_mode='none')
    plot_cell(r.get_cell(1))
    mlab.text(0.01, 0.9, "get_cell(1)", width=0.25)
    axes = mlab.orientation_axes( )
    mlab.show()