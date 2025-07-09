"""
Un GameManager es ideal para centralizar la lógica principal del juego,
la gestión de estados (menú, juego, pausa, etc.), el bucle principal y la interacción con Pygame.

 El GameManager debe tener un patrón Singleton, debe existir solamente un 1 GameManager. 
 No deben existir varias instancias de él. 

El patrón Singleton garantiza que una clase solo tenga una instancia y 
proporciona un punto de acceso global a esa instancia. 
Esto es ideal para el GameManager porque a menudo maneja el estado general del juego, 
la lógica principal, la puntuación, los recursos, etc., y solo tiene sentido que haya una única 
fuente de verdad para toda esa información.
"""

import pygame, constants, music
from main_menu import Menu
from character_selection import Character_Selection
from game import Game
from menu_opciones import OptionsMenu

class GameManager():
    _instance = None #singleton
    _initialized = False

    def __new__(cls, *args, **kwargs): #singleton
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not GameManager._initialized:
            pygame.init() 
            

            self.screen = pygame.display.set_mode((constants.SCR_WIDTH, constants.SCR_HEIGHT)) #se crea una pantalla de tamaño (ancho, alto)
            pygame.display.set_caption("Fablings") #título del juego

            self.running = True
            self.clock = pygame.time.Clock()

            self.main_menu = Menu(self) #se crea una instancia llamada main_menu de la Clase Menu
            self.character_selection = Character_Selection(self) 
            self.game_logic = Game()

            self.game_state = "MENU" #Para manejar el estado actual del juego
            
            self.options_menu = OptionsMenu(self)

    
    #Función para establecer el estado del juego, le mandamos el parámetro del estado en el que debe estar
    def set_game_state(self, status): 
        self.game_state = status


    #Función para manejar todos los eventos de pygame (clics, uso del teclado, etc.)
    #Sólo se verificarán los eventos que estén sucediendo en cada etapa o estatus del juego. 
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.game_state = "EXIT"
            
            if self.game_state == "MENU":
                self.main_menu.handle_events(event)

            elif self.game_state == "CHARACTER_SELECTION":
                self.character_selection.handle_events(event)
            
            elif self.game_state == "GAME":
                self.game_logic.handle_events(event)
                
            elif self.game_state == "OPTIONS_MENU":
                self.options_menu.handle_events(event)

            
 #Para lógica de cada estado del juego
 # Pasamos de un status a otro o bien, se llaman funciones para actualizar al juego   
    def update(self):
        if self.game_state == "MENU":
            if self.main_menu.is_game_started(): #si se da clic al botón jugar
                    self.game_state = "CHARACTER_SELECTION"
                    self.main_menu.reset()

            if self.main_menu.is_game_quit(): #si se da clic al botón salir
                self.game_state = "EXIT"
                self.main_menu.reset()

        elif self.game_state == "CHARACTER_SELECTION":
                if self.character_selection.is_ready():
                    
                    character_name = self.character_selection.get_character_selected_name()
                    character_image_path = self.character_selection.get_character_selected_image_url()
                    self.game_logic.set_player(character_name, character_image_path)
                    self.game_state = "GAME"
                    self.character_selection.reset()

        elif self.game_state == "GAME":
           self.game_logic.update()

        elif self.game_state == "EXIT":
            self.running = False
            
        elif self.game_state == "OPTIONS_MENU":
            
            pass


#Para dibujar imágenes y fondos en la pantalla
    def draw(self):
        if self.game_state == "MENU":
            self.main_menu.draw(self.screen)

        elif self.game_state == "CHARACTER_SELECTION":
            self.character_selection.draw(self.screen)

        elif self.game_state == "GAME":
            self.game_logic.draw(self.screen) 
            
        elif self.game_state == "OPTIONS_MENU":
            self.options_menu.draw(self.screen)

            
            pass
            
        pygame.display.flip() #Le muestra al usuario las imagenes que cargamos

    def run(self):
        while self.running:
            self.clock.tick(constants.MAX_FPS)
            self.handle_events()
            self.draw()
            self.update()
              
        pygame.mixer.music.stop()
        pygame.quit()


              