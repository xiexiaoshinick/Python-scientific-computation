# -*- coding: utf-8 -*-

class GraphvizMatplotlib(object):
    check_attributes = [
        "patch", "axes", "lines", "patches", "texts", "artists", 
        "xaxis", "yaxis", "majorTicks", "label", "tick1line", "tick2line"
    ]
    
    expand_classes = set([
        "Figure", "Axes", "Line2D", "Text"
    ])
    
    expand_once_classes = set([
        "XAxis", "YAxis",  "XTick", "YTick"  
    ])

    def node(self, obj):
        if obj is None or obj == []: return
        if type(obj) is list:
            label="|".join("<f%d> *" % i for i in xrange(len(obj)))
            color = "gray"
        else:
            label = obj.__class__.__name__
            color = "white"
        text = 'obj_%d[label="%s",fillcolor=%s];' % (id(obj), label, color)
        self.result.append(text)
    
    def link(self, obj1, obj2, attr):
        if obj2 is None or obj2 == []: return
        text = 'obj_%d -> obj_%d[label="%s"];' % (id(obj1), id(obj2), attr)
        self.result.append(text)

    def list_link(self, alist, idx, obj):
        if obj is None or obj == []: return
        text = "obj_%d:f%d -> obj_%d;" % (id(alist), idx, id(obj))
        self.result.append(text)

    def __init__(self):
        self.checked_ids = set()
        self.expanded = set()

    def _graphviz(self, obj):
        if obj is None: return
        if id(obj) in self.checked_ids: return
        
        self.node(obj)    
        self.checked_ids.add(id(obj))
        if type(obj) is list:
            for idx, inner in enumerate(obj):
                self._graphviz(inner)
                self.list_link(obj, idx, inner)
            return
            
        class_names = set([cls.__name__ for cls in obj.__class__.mro()])
        klass = obj.__class__.__name__
        if (len(class_names & self.expand_classes) > 0 or 
           klass in self.expand_once_classes and klass not in self.expanded):
            self.expanded.add( klass )
            for attr in self.check_attributes:
                    if hasattr(obj, attr):
                        subobj = getattr(obj, attr)
                        self._graphviz(subobj)
                        self.link(obj, subobj, attr)
                        
    def graphviz(self, obj):
        self.checked_ids = set()
        self.expanded = set()
        self.result = [
        """digraph structs {
rankdir="LR";        
node [shape=record,style=filled];
edge [fontsize=10, penwidth=0.5];"""
        ]
        self._graphviz(obj)
        self.result.append("}")
        return "\n".join(self.result)
        
def graphviz(obj):
    return GraphvizMatplotlib().graphviz(obj)
                
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.figure()
    plt.subplot(211)
    plt.bar([1,2,3],[1,2,3])
    plt.subplot(212)
    plt.plot([1,2,3])
    print graphviz(plt.gcf())
    plt.show()