#!/usr/bin/python

import gi
import about, snake
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SnakeGTKMenu(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Snake GTK Game Menu")
    self.set_border_width(50)

    grid = Gtk.Grid()
    self.add(grid)

    lblWelcome = Gtk.Label()
    lblWelcome.set_markup("Welcome to snakeGTK !!\n\n\n")
    
    btnStart = Gtk.Button.new_with_label("Start Game")
    btnStart.connect("clicked", self.on_click_me_clicked)

    btnAbout = Gtk.Button.new_with_label("About ...")
    btnAbout.connect("clicked", self.on_about_clicked)

    btnQuit = Gtk.Button.new_with_mnemonic("_Quit")
    btnQuit.connect("clicked", self.on_quit_clicked)

    grid.attach(lblWelcome,0,0,4,1)
    grid.attach_next_to(btnStart,lblWelcome,Gtk.PositionType.BOTTOM,4,1)
    grid.attach_next_to(btnAbout, btnStart , Gtk.PositionType.BOTTOM, 4, 1)
    grid.attach_next_to(btnQuit, btnAbout, Gtk.PositionType.BOTTOM, 4, 1)

  def on_click_me_clicked(self, button):
    snakeWin = snake.SnakeGTKGame(400,300,10)
    snakeWin.connect("delete-event", Gtk.main_quit)
    snakeWin.show_all()
    Gtk.main()

  def on_about_clicked(self, button):
    aboutWin = about.SnakeGTKAbout()        
    aboutWin.connect("delete-event", Gtk.main_quit)
    aboutWin.show_all()
    Gtk.main()

  def on_quit_clicked(self, button):
    Gtk.main_quit()

