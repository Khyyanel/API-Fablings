import pygame, constants
from menu import Menu

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((constants.SCR_WIDTH, constants.SCR_HEIGH))
    pygame.display.set_caption("Fablings")
    
    clock = pygame.time.Clock()

    principal_menu = Menu()
      
    running = True
    start_view = True

    #Bucle principal
    while running == True:
        clock.tick(constants.MAX_FPS) 
        #Bucle de eventoS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if principal_menu.is_menu_running():
                 principal_menu.handle_events(event)


        if principal_menu.is_menu_running():
            principal_menu.draw(screen)

        elif principal_menu.is_game_started():
            principal_menu.set_game_status(True)
            screen.fill(constants.BG2)
           
        else:
            running = False
             
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main() 