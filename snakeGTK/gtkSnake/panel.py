#!/usr/bin/python

import sys
import random
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
import cairo

class snakeGTKPanel(Gtk.DrawingArea):
  def __init__(self,Width,Height,pixel):
    super(snakeGTKPanel, self).__init__()
    #self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 0))
    #self.set_size_request(Width, Height)
    self.connect("draw", self.expose)
    self.init_game(Width,Height,pixel)

  def on_timer(self):
    if self.Playing:
      self.existApple()
      self.collision()
      self.move()
      self.queue_draw()
      return True
    else:
      return False
  
  def init_game(self,Width,Height,pixel):
    self.pixel = pixel
    self.Height = Height
    self.Width = Width
    self.mark = Width * Height / (pixel * pixel)
    self.left = False
    self.right = True
    self.up = False
    self.down = False
    self.Playing = True
    self.Pause = False
    self.dots = 3
    self.posX = [0] * self.mark
    self.posY = [0] * self.mark
    for i in range(self.dots):
      self.posX[i] = 50 - i * 10
      self.posY[i] = 50
    try:
      self.cola = cairo.ImageSurface.create_from_png("img/cola.png")
      self.cabeza = cairo.ImageSurface.create_from_png("img/cabeza_de.png")
      self.apple = cairo.ImageSurface.create_from_png("img/diamond.png")
    except Exception, e:
      print e.message
      sys.exit(1)
    self.newApple()
    GLib.timeout_add(100, self.on_timer)

  def expose(self, widget, ctx):
    if self.Playing:
      ctx.set_source_rgba( 0, 0, 0)
      ctx.paint()
      ctx.set_source_surface(self.apple, self.apple_x, self.apple_y)
      ctx.paint()
      ctx.set_source_rgba(0.5, 0.5, 0.5)
      ctx.rectangle(0,0,10,self.Height)
      ctx.rectangle(0,0,self.Width,10)
      ctx.rectangle(0,self.Height-10,self.Width,self.Height)
      ctx.rectangle(self.Width-10,0,self.Width,self.Height)
      ctx.fill()
      for num in range(self.dots):
        if (num == 0): 
          ctx.set_source_surface(self.cabeza, self.posX[num], self.posY[num])
          ctx.paint()
        else:
          ctx.set_source_surface(self.cola, self.posX[num], self.posY[num])
          ctx.paint()
    else:
      self.game_over(ctx)

  def game_over(self, ctx):
    ctx.set_source_rgba( 0, 0, 0)
    ctx.paint()
    w = self.Width / 2
    h = self.Height / 2
    (x, y, width, height, dx, dy) = ctx.text_extents("Game Over")
    ctx.set_source_rgba(65535, 65535, 65535)
    ctx.move_to(w - width/2, h)
    ctx.show_text("Game Over")
    self.Playing = False
  
  def existApple(self):
    if self.posX[0] == self.apple_x and self.posY[0] == self.apple_y: 
      self.dots = self.dots + 1
      self.newApple()
  
  def move(self):
    if self.Pause:
      return
    numdots = self.dots
    while numdots > 0:
      self.posX[numdots] = self.posX[(numdots - 1)]
      self.posY[numdots] = self.posY[(numdots - 1)]
      numdots = numdots - 1
    if self.left:
      self.cabeza = cairo.ImageSurface.create_from_png("img/cabeza_iz.png")
      self.posX[0] -= self.pixel
    if self.right:
      self.cabeza = cairo.ImageSurface.create_from_png("img/cabeza_de.png")
      self.posX[0] += self.pixel
    if self.up:
      self.cabeza = cairo.ImageSurface.create_from_png("img/cabeza_top.png")
      self.posY[0] -= self.pixel
    if self.down:
      self.cabeza = cairo.ImageSurface.create_from_png("img/cabeza_down.png")
      self.posY[0] += self.pixel
      
  def collision(self):
    numdots = self.dots
    while numdots > 0:
      if numdots > 4 and self.posX[0] == self.posX[numdots] and self.posY[0] == self.posY[numdots]:
        self.Playing = False
      numdots = numdots - 1
      
    if self.posY[0] > self.Height - self.pixel - 20:
      self.Playing = False
    if self.posY[0] < 20:
      self.Playing = False
    if self.posX[0] > self.Width - self.pixel - 20:
      self.Playing = False
    if self.posX[0] < 20:
      self.Playing = False

  def newApple(self):
    r = random.randint(10, 26)
    self.apple_x = r * self.pixel
    r = random.randint(10, 26)
    self.apple_y = r * self.pixel
 
  def on_key_down(self, event):
    keyname = Gdk.keyval_name(event.keyval)
    print("Key %s (%d) pulsada" % (keyname, event.keyval))
    if keyname == "Left" and not self.right and self.Pause == False:
      self.left = True
      self.up = False
      self.down = False
    if keyname == "Right" and not self.left and self.Pause == False:
      self.right = True
      self.up = False
      self.down = False
    if keyname == "Up" and not self.down and self.Pause == False:
      self.up = True
      self.right = False
      self.left = False
    if keyname == "Down" and not self.up and self.Pause == False:
      self.down = True
      self.right = False
      self.left = False
    if keyname == "space":
      self.Pause = not self.Pause
        
