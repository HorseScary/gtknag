import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class myWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
    
    def on_button_clicked(self, widget):
        print("Hello World")

win = myWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()