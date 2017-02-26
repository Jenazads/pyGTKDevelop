#!/usr/bin/python

import sys
import panel
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SnakeGTKGame(Gtk.Window):
  def __init__(self,Width,Height,pixel):
    super(SnakeGTKGame, self).__init__()
    self.set_title('Snake GTK')
    self.set_size_request(Width, Height)
    self.set_resizable(False)
    self.set_position(Gtk.WindowPosition.CENTER)
    self.panel = panel.snakeGTKPanel(Width,Height,pixel)
    self.connect("key-press-event", self.on_key_down)
    self.add(self.panel)
    self.connect("destroy", Gtk.main_quit)
    self.show_all()

  def on_key_down(self, widget, event): 
    key = event.keyval
    self.panel.on_key_down(event)

