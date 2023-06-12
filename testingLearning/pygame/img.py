import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

image = pygame.image.load("/img/redbrush.png")
width, height = image.get_rect().width, image.get_rect().height
print(width, height)            #1007, 354      2.8
# image = pygame.transform.scale(image, (width//2, height//2))
image = pygame.transform.scale(image, (50*2.8, 50))
x = 100
y = 100

isrunning= True

while isrunning:
    screen.blit(image, (x, y))
    # pygame.draw.rect(image, (255, 255, 255), (x, y, image.get_rect().width, image.get_rect().height))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            isrunning = False
