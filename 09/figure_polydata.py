# -*- coding: utf-8 -*-
from enthought.mayavi import mlab

import tvtk_polydata
reload(tvtk_polydata)
from tvtk_polydata import p1, p2
   
if __name__ == "__main__":    
    mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    mlab.clf()
    mlab.pipeline.surface(p1)
    mlab.pipeline.glyph(p1, mode='sphere', scale_factor=0.4, scale_mode='none')

    mlab.figure(2, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    mlab.clf()
    mlab.pipeline.surface(p2, representation='wireframe')
    mlab.pipeline.glyph(p2, mode='sphere', scale_factor=0.08, scale_mode='none')
    mlab.show()    