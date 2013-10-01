from math import pi, cos, sin, radians, degrees
#A class for manipulating a turtle. It records the locations it's been at
class Turtle:
  def __init__(self):
    self._angle = 90
    self._log = []

  @property
  def log(self):
    return self._log
  
  def move_to(self, position):
    self._log.append(position)

  def rotate_to(self, angle, in_radians=False):
    self._angle = angle if in_radians else radians(angle)

  def rotate_by(self,angle, in_radians=False):
    self._angle += angle if in_radians else radians(angle)
    self._angle %= 2*pi

  def move(self, how_far):
    x,y = self._log[-1]
    self.move_to((x+how_far*cos(self._angle),
                  y+how_far*sin(self._angle)))

