import turtle as t
import random as rng


def mygoto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

li_bfs = []      # li bfs: x, y, a, fill color, just fill, stop
li = [(0, 0), (1, 0), (2, 0), (0, -1), (2, -1), (0, -2), (1, -2), (2, -2)]
t.speed(-1)
t.colormode(255)


def put_in(a, x=0, y=0, fc=(0, 0, 0)):
    ans=()
    stop=False
    if a<10:  
        stop = True
    ran = rng.randint(0,1)
    if ran: ans=(x, y, a, fc, True, stop)
    else: ans=(x, y, a, fc, False, stop)
    li_bfs.append(ans)

def rec_bfs(f, r):
    while r>f :
        x = li_bfs[f][0]; y = li_bfs[f][1]; a = li_bfs[f][2]
        fc = li_bfs[f][3]; jf = li_bfs[f][4]; s=li_bfs[f][5]
        f+=1

        mygoto(x, y)
        t.setheading(0)
        if jf:
            t.fillcolor(fc)
            t.begin_fill()
        for i in range(4):
            t.forward(a)
            t.right(90)
        if jf: t.end_fill()
        
        for xy in li:
            nx = x+a*xy[0]/3; ny = y+a*xy[1]/3; na = a/3
            ffcc=fc[0]-50
            if ffcc<0: ffcc=255
            nfc=(ffcc, ffcc, ffcc)
            
            if not s and not jf: 
                put_in(na, nx, ny, nfc)
                r+=1


# rec(81)
li_bfs.append((
       -300, 300, 600, (255, 255, 255), False, False))
rec_bfs(0, 1)
mygoto(-10000,0)
input()
