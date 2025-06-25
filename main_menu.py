import pygame, ui, constants

class Menu():
    def __init__ (self, game_manager_instance):
        self.game_manager = game_manager_instance
        self._game_started = False
        self._game_quit = False
        self.running = True
    
    def reset(self): #reiniciamos los valores
        self._game_started = False
        self._game_quit = False


    def handle_events(self, event): #Verificamos los eventos de pygame
        if event.type == pygame.MOUSEBUTTONDOWN: #Si se detecta un clic hacia abajo
            if ui.start_button.collidepoint(event.pos): #Y si el clic 'colisiona' o coincide con el botón de start
                self._game_started = True  #asignamos verdadero a la variable de que el juego empezó 

            if ui.exit_button.collidepoint(event.pos): #Si el clic 'colisiona' con el botón de salir
                self._game_quit = True #asignamos verdadero a la salida del juego

    def draw(self, screen): #Tenemos como parámetro la pantalla del juego, la mandamos a llamar 
        screen.blit(ui.img_bg_scaled, (0,0)) #blit() sirve para dibujar. Aquí dibujamos el fondo a las medidas de la pantalla en la posición (x=0, y=0)
        
        #dibujamos rectangulos en la pantalla para cada botón del menú principal
        #rect(pantalla, color, rectángulo)
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.start_button) 
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.options_button)
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.exit_button)

        #mostramos el título y botones
        screen.blit(ui.title_menu, (constants.TITLE_MENU_X, constants.TITLE_MENU_Y))
        screen.blit(ui.text_start_button, (ui.start_button.x + 32, ui.start_button.y + 10))
        screen.blit(ui.text_options_button, (ui.options_button.x + 2, ui.options_button.y +10 ))
        screen.blit(ui.text_exit_button, (ui.exit_button.x + 35, ui.exit_button.y + 10))

    #Funciones GET
    #Sirven para adquirir los valores internos de la clase
    def is_game_started(self):
        return self._game_started #<- como tiene un guión bajo, es una variable privada 
                                    #así evitamos que otras clases modifiquen su valor (ENCAPSULACIÓN)

    def is_game_quit(self):
        return self._game_quit
    
