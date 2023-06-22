import pygame as py

py.init()

flags = py.RESIZABLE
py.display.set_mode((500, 400), flags)

running = True


clock = py.time.Clock()
while running:
    # clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            runnning = False
            break
    keys = py.key.get_pressed()
    if keys[py.K_q]:
        print("q눌렀다~")
    if keys[py.K_w]:
        print('w')
    if keys[py.K_EQUALS]:
        py.quit()
        runnning = False
        break
