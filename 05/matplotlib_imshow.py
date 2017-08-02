# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.subplots_adjust(0,0,1,1,0.05,0.05)
plt.subplot(331)
img = plt.imread("lena.jpg")
plt.imshow(img)

plt.subplot(332)
plt.imshow(img[::-1])

plt.subplot(333)
plt.imshow(img, origin="lower")

img = img[::-1]
plt.subplot(334)
plt.imshow(img*1.0)

plt.subplot(335)
plt.imshow(img/255.0)

plt.subplot(336)
plt.imshow(np.clip(img/200.0, 0, 1))

plt.subplot(325)
plt.imshow(img[:,:,0])
plt.colorbar()

plt.subplot(326)
plt.imshow(img[:,:,0], cmap=cm.copper)
plt.colorbar()

for ax in plt.gcf().axes:
    ax.set_axis_off()
    ax.set_axis_off()

plt.show()