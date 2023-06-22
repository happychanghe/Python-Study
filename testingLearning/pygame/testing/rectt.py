import pygame as py

py.init()

flags = py.RESIZABLE
s = py.display.set_mode((500, 300), flags)

r = py.Rect(100, 100, 100, 100)
print(f"{r.x, r.y}\n{r.top, r.left, r.bottom, r.right}\n{r.topleft, r.bottomleft, r.topright, r.bottomright}")
print(f"{r.midtop, r.midleft, r.midbottom, r.midright}")
print(f"{r.center, r.centerx, r.centery}\n{r.size, r.width, r.height, r.w, r.h}")
isrunning = True
while isrunning:
    for e in py.event.get():
        if e.type == py.QUIT:
            isrunning = False
    
    keys = py.key.get_pressed()
    if keys[py.K_w]:
        r.top -= 1
        r.height += 1
    if keys[py.K_a]:
        r.left -= 1
        r.width += 1
    if keys[py.K_d]:
        # r.right += 1
        r.width += 1
    if keys[py.K_s]:
        # r.bottom += 1
        r.height += 1

    s.fill((0, 0, 0))
    py.draw.rect(s, (255, 255, 255), r)

    py.display.update()

py.quit()