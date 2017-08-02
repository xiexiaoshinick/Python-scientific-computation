# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab

# 创建数据
x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2) # 高度数据
c = 2*x + y # 颜色数据

src = mlab.pipeline.array2d_source(x, y, z)
dataset = src.mlab_source.dataset # 和src.outputs[0]相同
array_id = dataset.point_data.add_array(c.T.ravel())
dataset.point_data.get_array(array_id).name = "color"
dataset.point_data.update()

# 创建流水线
warp = mlab.pipeline.warp_scalar(src, warp_scale=2.0)
normals = mlab.pipeline.poly_data_normals(warp)
active_attr = mlab.pipeline.set_active_attribute(normals,
    point_scalars="color")
surf = mlab.pipeline.surface(active_attr)

mlab.axes()
mlab.outline()
mlab.show()
