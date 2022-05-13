import gi
from os import system
from sys import argv

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class myWindow(Gtk.Window):
    def __init__(self):
        self.box = Gtk.Box(spacing=5)

        for i in range(0,len(argv)):
            if argv[i] == '-t' or argv[i] == '--title':
                super().__init__(title=argv[i + 1])
            
            elif argv[i] == '-l' or argv[i] == '--label':
                self.label = Gtk.Label(label=argv[i+1])
                self.box.pack_start(self.label, True, True, 0)
            
            elif argv[i] == '-b' or argv[i] == '--button':
                self.button = Gtk.Button()
                self.button.connect("clicked", self.on_button_clicked)
                self.box.pack_start(self.button, True, True, 0)
        

        self.label = Gtk.Label(label="Button", angle=25)
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        self.add(self.box)
    
    def on_button_clicked(self, button):
        pass

win = myWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()