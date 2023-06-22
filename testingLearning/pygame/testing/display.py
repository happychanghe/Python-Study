import pygame

def main():

    pygame.init()
    # logo = pygame.image.load("../img/nupjuk.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("rect")
    flags = pygame.OPENGL | pygame.RESIZABLE | pygame.NOFRAME
    window = pygame.display.set_mode((500, 400), flags)
    pygame.display.set_allow_screensaver(True)
    print(pygame.display.get_desktop_sizes())
    print(pygame.display.get_window_size())

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                is_running = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            print(pygame.display.get_active(), pygame.display.get_init(), sep='\n', end='\n\n')
        if keys[pygame.K_EQUALS]:
            if pygame.display.get_init():
                pygame.display.quit()
            else: 
                pygame.display.init()
        if keys[pygame.K_f]:
            pygame.display.toggle_fullscreen()
            
    
    


if __name__=='__main__':
    main()