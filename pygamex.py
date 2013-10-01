import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d

def flipy(y):
  return 600 - y

#Widget that takes two Vec2D points
class Line:
  def __init__(self, a, b):
    self._shape = pymunk.Segment(pymunk.Body(),a,b,0)
    self._shape.elasticity = 1.0

  @property
  def shape(self):
    return self._shape

  def paint(self, paintable):
    shape = self._shape
    body = shape.body
    pv1 = body.position + shape.a.rotated(body.angle)
    pv2 = body.position + shape.b.rotated(body.angle)
    p1 = pv1.x, flipy(pv1.y)
    p2 = pv2.x, flipy(pv2.y)
    pygame.draw.lines(paintable, THECOLORS["black"],False,[p1,p2])


class App:

  def resolve_collision(self, space, arbiter, *args, **kwargs):
    objecta, objectb = arbiter.shapes
    if objecta in self._collidables:
      self._collidables[objecta].on_collision(objectb, arbiter)

    if objectb in self._collidables:
      self._collidables[objectb].on_collision(objecta, arbiter)



  def __init__(self, width=600, height=600):
    self._running = False
    self._initialized = False
    self._width = width
    self._height = height
    self._space = pymunk.Space()
    self._space.add_collision_handler(0,0, 
	post_solve=self.resolve_collision)
    self._widgets = []
    self._collidables = {}

  def init(self):
    pygame.init()
    self._screen = pygame.display.set_mode((self._width,self._height))
    self._running = True
    self._initialized = True

  def has_collision_event(widget):
    return False

  def add_widget(self,widget,is_static=True,listening_to_collision=False):
    self._widgets.append(widget)
    if listening_to_collision:
      self._collidables[widget.shape] = widget

    if is_static:
      self._space.add(widget.shape)
    else:
      self._space.add(widget.shape.body, widget.shape)


  def start(self):
    if not self._initialized:
      self.init()
    while self._running:
     #Physics run
     dt = 1.0/60.0
     self._space.step(dt)
     self._screen.fill(THECOLORS["white"])
     for widget in self._widgets:
       widget.paint(self._screen)
     pygame.display.flip()
