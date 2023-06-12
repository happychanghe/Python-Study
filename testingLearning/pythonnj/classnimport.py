import turtle as t 
#from . import nj 
#from testMPLsleep import heartGraph as hg
from Brush import Brush as b

# nj.start()
# hg.convert_tag2dict("ddd", ["a"])

mybrush = b((5, 5, 5), 0.5)
# mybrush.moveup(5, 5)
mybrush.dt(2, 20, 100)
input()


# t.speed(-1)
# for i in range(10000):
#     t.forward(i)
#     t.left(91)