from pygamex import *
from billiard_ball import *
from turtle import *
from pymunk import Vec2d
from math import pi

from itertools import izip as zip

def main():
  app = App()
  turtle = Turtle()
  turtle.move_to((50,50))
  turtle.rotate_to(60)
  turtle.move(100)
  turtle.rotate_by(-120)
  turtle.move(100)
  turtle.rotate_to(180)
  turtle.move(100)
  log = turtle.log 
  for (x2,y2),(x1,y1) in zip(log[1::],log):
    app.add_widget(Line(Vec2d(x1,y1),Vec2d(x2,y2)))
  app.add_widget(BilliardBall(Vec2d(125,75),pi/2),False,True)
  app.start()

if __name__ == '__main__':
  main()
