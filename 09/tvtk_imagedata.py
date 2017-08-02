# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk
import numpy as np

img = tvtk.ImageData(spacing=(0.1,0.1,0.1), origin=(0.1,0.2,0.3), dimensions=(3,4,5))
img.point_data.scalars = np.arange(0.0, img.number_of_points)
img.point_data.scalars.name = 'scalars'
