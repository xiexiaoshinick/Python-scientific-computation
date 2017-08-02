# -*- coding: utf-8 -*- 
import numpy as np 
from enthought.mayavi import mlab 
  
x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2) 
  
face = mlab.surf(x, y, z, warp_scale=2)
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(face) 
  
from enthought.tvtk.pipeline.browser import PipelineBrowser 
b = PipelineBrowser() 
b.root_object = [mlab.gcf().scene.render_window] 
b.show() 
mlab.show() 
mscene = mlab.gcf()
tscene = mscene.scene
rw = tscene.render_window
a1 = rw.renderers[0].view_props[0]