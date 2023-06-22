import pygame

pygame.init()
flags = pygame.RESIZABLE
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode((500, 400), flags)
# AWIDTH = 0
# AHEIGHT = 0
def ratiomaking(WIDTH, HEIGHT):
    actualstart:tuple
    if HEIGHT / 4 * 5 >= WIDTH:
        AWIDTH = WIDTH
        AHEIGHT = WIDTH / 5 * 4
        actualstart = (0, (HEIGHT - AHEIGHT)/2)
    else:
        AHEIGHT = HEIGHT
        AWIDTH = HEIGHT / 4 * 5
        actualstart = ((WIDTH - AWIDTH)/2, 0)
    # print(AWIDTH, AHEIGHT, actualstart)
    return AWIDTH, AHEIGHT, actualstart

clock = pygame.time.Clock()
isrunning = True
while isrunning:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
            break
    AWIDTH, AHEIGHT, actualstart = ratiomaking(*pygame.display.get_window_size())
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (*actualstart, AWIDTH, AHEIGHT))

    pygame.display.update()

pygame.quit()