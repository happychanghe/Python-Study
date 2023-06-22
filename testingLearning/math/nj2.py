import turtle as t
import math as m
import random

t.left(90)
t.speed(-1)
t.colormode(255)
d = 10
#138,43,226
def thiss(before, upsidedown, pc):
    t.pencolor(138,pc,226)
    
    for i in range(3):
        t.forward(d)
        t.backward(d)
        t.right(120)
    len=random.randint(0,2)
    if len==before:
        len=(len+1)%3
    for i in range(len):
        t.right(120)
    t.forward(d)
    t.setheading(90)
    ar=[[3, 5, 1],[0, 2, 4]]
    if pc+5>=255: pc=-5
    thiss2(ar[upsidedown][len], pc+5)

def thiss2(before, pc):
    t.pencolor(138,pc,226)
    
    for i in range(6):
        t.forward(d)
        t.backward(d)
        t.right(60)
    len=random.randint(0,5)
    if len==before:
        len=(len+1)%6
    for i in range(len):
        t.right(60)
    t.forward(d)
    if len%2==0: t.setheading(-90)
    else: t.setheading(90)
    ar = [0, 2, 1, 0, 2 ,1]
    if pc+5>=255: pc=-5
    thiss(ar[len], (len+1)%2, pc+5)

thiss2(0, 0)

input()