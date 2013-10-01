from pygamex import *
from billiard_ball import *
from pymunk import Vec2d
from math import pi

def main():
  app = App()
  app.add_widget(Line(Vec2d(50,50),Vec2d(300,300)))
  app.add_widget(Line(Vec2d(300,300),Vec2d(300,50)))
  app.add_widget(Line(Vec2d(300,50),Vec2d(50,50)))
  app.add_widget(BilliardBall(Vec2d(100,75),pi/2),False,True)
  app.start()

if __name__ == '__main__':
  main()
