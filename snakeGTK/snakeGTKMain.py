#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gtkSnake import menu

snakeMenu = menu.SnakeGTKMenu()
snakeMenu.connect("delete-event", Gtk.main_quit)
snakeMenu.show_all()
Gtk.main()

