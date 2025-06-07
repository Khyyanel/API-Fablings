import pygame

SCR_WIDTH = 960
SCR_HEIGH = 540
BG = (255, 255, 255)
BG2 = (255, 0, 0)
BG3 = (0, 204, 255)

img = pygame.image.load("assets/img/fondo inicio.png")
img_transform = pygame.transform.scale(img, (SCR_WIDTH, SCR_HEIGH))

MAX_FPS = 60
    
def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGH))
    pygame.display.set_caption("Fablings")
    
    #Fuentes
    font_button = pygame.font.Font("assets/fonts/Daydream.ttf", 20)
    font_title = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 100)
    
    #Boton
    start_button = pygame.Rect(SCR_WIDTH / 2 - 100, SCR_HEIGH / 2 - 10 , 150, 50)
    exit_button = pygame.Rect(SCR_WIDTH / 2 - 100, SCR_HEIGH / 2 + 70 , 150, 50)
    
    text_start_button = font_button.render("Jugar", True, 0)
    text_exit_button = font_button.render("Salir", True, 0)
    
    title = font_title.render("FABLINGS", True, BG2)
    
    def start_window():
        screen.blit(img_transform, (0, 0))
        pygame.draw.rect(screen, BG, start_button)
        pygame.draw.rect(screen, BG, exit_button)
        screen.blit(title, (280, 100))
        screen.blit(text_start_button, (start_button.x + 18, start_button.y + 10))
        screen.blit(text_exit_button, (exit_button.x + 25, exit_button.y + 10))
        pygame.display.update()
    
    clock = pygame.time.Clock()
    
    start_view = True    
    running = True

    #Bucle principal
    while running == True:
        #Bucle de eventoS
        if start_view:
            start_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        start_view = False
                    if exit_button.collidepoint(event.pos):
                        running = False
                              
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.fill(BG)
        
            pygame.display.flip()

            clock.tick(MAX_FPS)  

    pygame.quit()


if __name__ == "__main__":
    main() 