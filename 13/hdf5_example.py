# -*- coding: utf-8 -*-
import h5py
import numpy as np

f = h5py.File("tmp.hdf5")
f.create_group("group1")
g2 = f.create_group("group2")
g2.create_group("subgroup1")
g2["a"] = np.arange(0,5)
print g2["a"]
print g2["a"].value
print np.sum(g2["a"])
print g2["a"] + np.arange(1, 6)
g2["a"][-1] = 10
print g2["a"].value
d = g2.create_dataset("b", (4,4), np.float)
d[:,0] = 2.0
print d.value
g2.create_dataset("c", data=np.arange(0, 1.0, 0.2))
print g2["c"].value
del g2["a"]
g2["a"] = np.linspace(0, 1, 5)
print g2["a"].value
print g2.attrs
g2.attrs["title"] = "test data"
g2.attrs["test"] = np.arange(5)
print g2.attrs
print g2.attrs["test"]
f.close()