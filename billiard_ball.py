from pygamex import *
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk import Vec2d
from itertools import izip as zip

from math import cos,sin,pi

def direction_vector(magnitude, angle):
  """Returns the vector for the given magnitude and angle"""
  return (cos(angle)*magnitude, -(sin(angle)*magnitude))

def draw_line(paintable, pos1,pos2):
  pos1_2 = pos1.x, flipy(pos1.y)
  pos2_2 = pos2.x, flipy(pos2.y)
  pygame.draw.aalines(paintable, THECOLORS["blue"], False, [pos1_2, pos2_2],4)


class BilliardBall:
  def __init__(self, position, angle):
    body = pymunk.Body(10,25)
    body.position = position
    body.apply_impulse(direction_vector(20,-angle))
    circle = pymunk.Circle(body, 2, (0,0))
    circle.elasticity = 1.0
    self._shape = circle
    self._collisions = ([position],None)

  @property
  def shape(self):
    return self._shape

  def on_collision(self, other, arbiter):
    points, seen = self._collisions
    points.append(Vec2d(self._shape.body.position))
   
  def paint(self, paintable):
    shape = self._shape
    body = shape.body
    x,y = map(int,body.position)
    #Draw the trail
    points, seen = self._collisions
    pygame.draw.aalines(paintable,
	                THECOLORS["blue"],
			False,
			[(x, flipy(y)) for x,y in points + [(x,y)]],
			4)

    pygame.draw.circle(paintable, THECOLORS["black"],(int(x),int(flipy(y))), int(shape.radius),2)
