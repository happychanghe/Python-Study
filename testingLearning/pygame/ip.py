import pygame

pygame.init()

s = pygame.display.set_mode((500, 400))

r = pygame.Rect(0, 0, 100, 100)

isrunning = True

while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
            break
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_8]:
        r = r.move(1, 1)
        print(0)
    if keys[pygame.K_9]:
        r.move_ip(1, 1)

    s.fill((0, 0, 0))
    pygame.draw.rect(s, (255, 255, 255), r)

    pygame.display.update()

pygame.quit()