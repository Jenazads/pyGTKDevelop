#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SnakeGTKAbout(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Snake About ... ")
    hbox = Gtk.Box(spacing=10)
    hbox.set_homogeneous(False)
    vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox_left.set_homogeneous(False)

    hbox.pack_start(vbox_left, True, True, 0)
    label = Gtk.Label()
    label.set_markup("\t\tSnake GTK game by Felipe Moreno.\t\t\t\n"
                     "\t\tYou can find this on <b>Jenazad</b> profile.\t\t\n"
                     "\t\t<a href=\"https://github.com/Jenazad/pyGTKDevelop\" "
                     "title=\"Click to find more\">Review my snakeGTK source code</a>.\t\t")
    label.set_line_wrap(True)
    vbox_left.pack_start(label, True, True, 0)
    
    self.add(hbox)
