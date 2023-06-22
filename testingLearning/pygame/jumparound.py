# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("jump around")
    
    # create a surface on screen that has the size of 800 x 600
    WIDTH = 800
    HEIGHT = 600
    flags = pygame.DOUBLEBUF | pygame.NOFRAME
    screen = pygame.display.set_mode((WIDTH,HEIGHT), flags)
    colorss = [(0, 255, 0)]
    # pygame.display.set_palette(colorss)

    # floor
    finfo = [(0, 300, 200, 300), (200, 500, 350, 100), (550, 450, 250, 150), (395, 250, 50, 50), (650, 100, 50, 50)]
    floors = []
    for info in finfo:
        floors.append(pygame.Rect(*info))

    # player
    p_width = 100
    p_height = 100
    xpos = 10
    ypos = 10
    p_speed = 5
    p_vv = 0
    gravity = 1
    jumpforce = 20
    player = pygame.Rect(xpos, ypos, p_width, p_height)
    image = pygame.image.load("img/nupjuk.png")
    image = pygame.transform.scale(image, (p_width, p_height))
    pygame.display.set_icon(image)
     
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
     
    # main loop
    while running:
        clock.tick(60)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        p_vv += gravity
        for floor in floors:
            if player.colliderect(floor):
                if p_vv > 0: 
                    p_vv = 0
                    if player.y + p_height > floor.y:
                        player.y = floor.y - p_height +1
                break


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            player.x -= p_speed
        if keys[pygame.K_RIGHT]:
            player.x += p_speed
        if keys[pygame.K_SPACE] and player.colliderect(floor):
            p_vv -= jumpforce
        if keys[pygame.K_EQUALS]:
            running = False
        if keys[pygame.K_f]:
            pygame.display.toggle_fullscreen()
        if keys[pygame.K_3]:
            # player.move(10, 10)
            player.x = 10
            player.y = 10
            p_vv= 0

        player.y += p_vv
        
        screen.fill((0, 0, 0))

        # pygame.draw.rect(screen, (255, 255, 255), player)
        screen.blit(image, (player.x, player.y))
        for floor in floors:
            pygame.draw.rect(screen, '#12DE78', floor)

        pygame.display.update()
    pygame.quit()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()