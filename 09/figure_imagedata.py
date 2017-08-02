# -*- coding: utf-8 -*-
from enthought.mayavi import mlab
from tvtk_imagedata import img

def plot_cell(cell):
    x0,x1,y0,y1,z0,z1 = cell.bounds
    p = mlab.points3d((x0+x1)/2, (y0+y1)/2, (z0+z1)/2, opacity=0.2, mode="cube")
    cube = p.glyph.glyph_source.glyph_source
    cube.x_length = x1-x0
    cube.y_length = y1-y0
    cube.z_length = z1-z0
    
if __name__ == "__main__":
    mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    mlab.clf()

    mlab.pipeline.surface(mlab.pipeline.extract_edges(img), color=(0, 0, 0))
    mlab.pipeline.glyph(img, mode='sphere', scale_factor=0.03, scale_mode='none')
    plot_cell(img.get_cell(0))
    mlab.text(0.01, 0.9, "get_cell(0)", width=0.25)
    mlab.orientation_axes( )
    mlab.show()