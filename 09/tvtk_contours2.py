# -*- coding: utf-8 -*-
from enthought.tvtk.api import tvtk
from utility import show_actors
from tvtk_cut_plane import read_data

if __name__ == "__main__":      
    
    plot3d = read_data()
    plot3d.add_function(153) 
    plot3d.update()
    contours = tvtk.ContourFilter(input = plot3d.output) 
    contours.set_value(0, 0.32) 
    mapper = tvtk.PolyDataMapper(input = contours.output,
        scalar_range = plot3d.output.point_data.get_array(4).range, 
        scalar_mode = "use_point_field_data") 
    mapper.color_by_array_component("VelocityMagnitude", 0) 
    actor = tvtk.Actor(mapper = mapper)
    actor.property.opacity = 0.6 
    
    # StructuredGrid网格的外框
    outline = tvtk.StructuredGridOutlineFilter(input = plot3d.output)
    outline_mapper = tvtk.PolyDataMapper(input = outline.output)
    outline_actor = tvtk.Actor(mapper = outline_mapper)
    outline_actor.property.color = 0.3, 0.3, 0.3
    win, gui = show_actors([actor, outline_actor])
    gui.start_event_loop()
