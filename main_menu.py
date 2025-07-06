import pygame, ui, constants
from button import Button

class Menu():
    def __init__ (self, game_manager_instance):
        self.game_manager = game_manager_instance
        self._game_started = False
        self._game_quit = False
        self.running = True      
            
        self.start_button = Button (
            x = constants.BUTTON_LEFT,
            y = constants.START_BUTTON_TOP,
            width = constants.BUTTON_WIDTH, 
            height = constants.BUTTON_HEIGHT,
            text = "Jugar",
            font = ui.font_button, 
            color = constants.COLOR_WHITE, 
            text_offset_x = 35
        )

        self.menu_opciones_button = Button (
            x = constants.BUTTON_LEFT,
            y = constants.OPTIONS_BUTTON_TOP,
            width = constants.BUTTON_WIDTH, 
            height = constants.BUTTON_HEIGHT,
            text = "Opciones",
            font = ui.font_button, 
            color = constants.COLOR_WHITE, 
            text_offset_x = 5
        )

        self.exit_button = Button (
            x = constants.BUTTON_LEFT,
            y = constants.EXIT_BUTTON_TOP,
            width = constants.BUTTON_WIDTH, 
            height = constants.BUTTON_HEIGHT,
            text = "Salir",
            font = ui.font_button, 
            color = constants.COLOR_WHITE, 
            text_offset_x = 40
        )
    
    def reset(self): #reiniciamos los valores
        self._game_started = False
        self._game_quit = False


    def handle_events(self, event): #Verificamos los eventos de pygame
        if event.type == pygame.MOUSEBUTTONDOWN: #Si se detecta un clic hacia abajo
            if self.start_button.collidepoint(event.pos): #Y si el clic 'colisiona' o coincide con el botón de start
                self._game_started = True  #asignamos verdadero a la variable de que el juego empezó 

            if self.exit_button.collidepoint(event.pos): #Si el clic 'colisiona' con el botón de salir
                self._game_quit = True #asignamos verdadero a la salida del juego
            if self.menu_opciones_button.collidepoint(event.pos):
                self.menu_opciones.handle_events(event)
                self._show_menu_options = True 

    def draw(self, screen): #Tenemos como parámetro la pantalla del juego, la mandamos a llamar 
        screen.blit(ui.img_bg_scaled, (0,0)) #blit() sirve para dibujar. Aquí dibujamos el fondo a las medidas de la pantalla en la posición (x=0, y=0)

        self.start_button.draw(screen)
        self.menu_opciones_button.draw(screen)
        self.exit_button.draw(screen)

        #mostramos el título 
        screen.blit(ui.title_menu, (constants.TITLE_MENU_X, constants.TITLE_MENU_Y))

    #Funciones GET
    #Sirven para adquirir los valores internos de la clase
    def is_game_started(self):
        return self._game_started #<- como tiene un guión bajo, es una variable privada 
                                    #así evitamos que otras clases modifiquen su valor (ENCAPSULACIÓN)

    def is_game_quit(self):
        return self._game_quit
    
    #Funciones ver menu opciones
    def show_menu_options(self):
        return self._show_menu_options