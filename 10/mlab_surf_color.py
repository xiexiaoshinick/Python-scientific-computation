# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2)

face = mlab.surf(x, y, z, warp_scale=2)
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(face)

c = 2*x + y
# 获得Array2DSource
img = mlab.gcf().children[0].image_data
# 注意c的第0轴对应于x，第一轴对应于y，因此需要先将其转置
# 标量数组只接受一维数组，因此调用ravel()方法将数组变成一维的
array_id = img.point_data.add_array(c.T.ravel())
img.point_data.get_array(array_id).name = "color"
img.point_data.update()

normals = mlab.gcf().children[0].children[0].children[0]
surf = normals.children[0]
del normals.children[0]
active_attr = mlab.pipeline.set_active_attribute(normals, point_scalars="color")
active_attr.children.append(surf)
mlab.show()