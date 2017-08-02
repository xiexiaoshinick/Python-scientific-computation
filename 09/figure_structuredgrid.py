# -*- coding: utf-8 -*-
from enthought.mayavi import mlab
from enthought.tvtk.api import tvtk
from tvtk_structuredgrid import s1, s2
   
def plot_cell(cell):
    p = tvtk.PolyData()
    p.points = cell.points
    poly = []
    ids = list(cell.point_ids)
    for i in xrange(cell.number_of_faces):
        poly.append([ids.index(x) for x in cell.get_face(i).point_ids])
    p.polys = poly
    mlab.pipeline.surface(p, opacity = 0.3)

if __name__ == "__main__":    
    mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    mlab.clf()
    mlab.pipeline.surface(mlab.pipeline.extract_edges(s1), color=(0, 0, 0))
    mlab.pipeline.glyph(s1, mode='sphere', scale_factor=0.4, scale_mode='none')
    plot_cell(s1.get_cell(2))
    mlab.text(0.01, 0.9, "get_cell(2)", width=0.25)
    mlab.orientation_axes( )

    mlab.figure(2, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    mlab.clf()
    mlab.pipeline.surface(mlab.pipeline.extract_edges(s2), color=(0, 0, 0))
    mlab.axes()
    mlab.pipeline.glyph(s2, mode='sphere', scale_factor=0.2, scale_mode='none')
    plot_cell(s2.get_cell(3))
    mlab.text(0.01, 0.9, "get_cell(3)", width=0.25)
    mlab.show()