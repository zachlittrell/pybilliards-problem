from pygamex import *
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk import Vec2d

from math import cos,sin,pi

def direction_vector(magnitude, angle):
  """Returns the vector for the given magnitude and angle"""
  return (cos(angle)*magnitude, -(sin(angle)*magnitude))

class BilliardBall:
  def __init__(self, position, angle):
    body = pymunk.Body(10,25)
    body.position = position
    body.apply_impulse(direction_vector(20,-angle))
    circle = pymunk.Circle(body, 2, (0,0))
    circle.elasticity = 1.0
    self._shape = circle

  @property
  def shape(self):
    return self._shape

  def paint(self, paintable):
    shape = self._shape
    body = shape.body
    x,y = body.position
    pygame.draw.circle(paintable, THECOLORS["black"],(int(x),int(flipy(y))), int(shape.radius),2)
