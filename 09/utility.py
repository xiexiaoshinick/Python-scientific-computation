# -*- coding: utf-8 -*-
import os
import os.path as path
from enthought.tvtk.tools import ivtk
from enthought.pyface.api import GUI

def vtk_data(name):
    folder = os.environ.get("VTK_DATA_ROOT", "VTKData")
    datapath = os.path.join(folder, "data", name)
    if not path.exists(datapath):
        raise IOError("please set environment variable: VTK_DATA_ROOT")
    return datapath
    
def show_actors(actors, shell=False):
    gui = GUI()
    if shell:
        window = ivtk.IVTKWithCrustAndBrowser(size=(800,600))
    else:
        window = ivtk.IVTKWithBrowser(size=(600,400))
    window.open()
    for a in actors:
        window.scene.add_actor( a )
    window.scene.background = (1,1,1)
    return window, gui