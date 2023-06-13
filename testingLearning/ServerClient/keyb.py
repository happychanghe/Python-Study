import pygame, sys
import pygame.locals

pygame.init()
BLACK = (0,0,0)
WIDTH = 100
HEIGHT = 100
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # replace the 'p' to whatever key you wanted to be pressed
            print(1) #Do what you want to here

        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

