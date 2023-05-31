import turtle as t
import math

class Brush:
    def __init__(self, color=(0,0,0), s=-1) -> None:
        self.color = color
        self.speed = s
    def moveup(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def dt(self, x, y, _a):
        print(t.heading())
        t.penup()
        t.goto(x, y)
        t.left(t.towards(t.xcor(), t.ycor()+1))
        print(t.heading(), t.towards(t.xcor(), t.ycor()+1))
        t.forward(_a*math.sqrt(3)/3)
        t.right(150)
        t.pendown()
        t.begin_fill()
        for i in range(3):
            t.forward(_a)
            t.right(120)
        t.end_fill()