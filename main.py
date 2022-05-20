import gi
from os import system
import argparse

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

global parser
parser = argparse.ArgumentParser(description="owo")
parser.add_argument("-b", "--button", type=str, nargs=2, help="<label> <'command'>")
parser.add_argument("-m", "--message", type=str, nargs=1, help="<message>")
parser.parse_args()
global args
args = parser.parse_args()

class myWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="ljalkjflskj")

        self.box = Gtk.Box(spacing=5)
        self.add(self.box)

        self.label = Gtk.Label(label=args.message[0])
        self.box.pack_start(self.label, True, True, 0)
        
        self.button = Gtk.Button(label=args.button[0])
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    
    def on_button_clicked(self, button):
        system(args.button[1])

win = myWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()