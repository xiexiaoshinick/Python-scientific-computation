# -*- coding: utf-8 -*-
"""
演示菜单、工具栏和状态栏的制作方法
"""
from enthought.traits.api import HasTraits, Code, Str, Int, on_trait_change
from enthought.traits.ui.api import View, Item, Handler, CodeEditor
from enthought.traits.ui.menu import Action, ActionGroup, Menu, MenuBar, ToolBar
from enthought.pyface.image_resource import ImageResource

class MenuDemoHandler(Handler):
    def exit_app(self, info):
        info.ui.control.Close()

class MenuDemo(HasTraits):
    status_info = Str
    current_line = Int
    text = Code
    def traits_view(self):
        file_menu = Menu( 
            ActionGroup(
                Action(id="open", name=u"打开", action="open_file"),
                Action(id="save", name=u"保存", action="save_file"),
            ),
            ActionGroup(
                Action(id="exit_app", name=u"退出", action="exit_app"),
            ),
            name = u"文件"
        )
        
        about_menu = Menu(
            Action(id="about", name=u"关于", action="about_dialog"),
            name = u"帮助"
        )
        
        tool_bar = ToolBar( 
            Action(
                image = ImageResource("folder_page.png", search_path = ["img"]),
                tooltip = u"打开文档",
                action = "open_file"
            ), 
            Action(
                image = ImageResource("disk.png", search_path = ["img"]),
                tooltip = u"保存文档",
                action = "save_file"
            ),                 
        )
        
        return View(
            Item("text", style="custom", show_label=False, 
                editor=CodeEditor(line="current_line")),
            menubar = MenuBar(file_menu, about_menu), 
            toolbar = tool_bar,
            statusbar = ["status_info"], 
            resizable = True,
            width = 500, height = 300,
            title = u"程序编辑器",
            handler = MenuDemoHandler()
        )
        
    @on_trait_change("text,current_line")
    def update_status(self):
        self.status_info = "%d:%d" % (self.text.count("\n")+1, self.current_line)
        
    def open_file(self):
        print "open_file"
        
    def save_file(self):
        print "save_file"
        
    def about_dialog(self):
        print "about_dialog"

demo = MenuDemo()
demo.configure_traits()