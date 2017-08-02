# coding=utf-8
from visual import *
text = label(pos=(0, -2, 0))
sphere(pos=(0,2,0))
box(pos = (2, 0, 0))
ray = arrow(pos=(0,0,0), color=(1,0,0))

while True: 
    rate(30)
    texts = []
    for attrname in ["pos", "pick", "pickpos", "camera", "ray"]:
        texts.append("%s=%s" % (attrname, getattr(scene.mouse, attrname)))
    texts.append("project=%s" % 
		scene.mouse.project(normal=scene.forward, point=scene.center))
    text.text = "\n".join(texts)
    ray.axis = scene.mouse.ray
    if scene.mouse.events > 0:
        event = scene.mouse.getevent()
        print "press=%s, click=%s, drag=%s, drop=%s, release=%s" % (
            event.press, event.click, event.drag, event.drop, event.release
        )
