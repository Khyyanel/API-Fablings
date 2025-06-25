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

import pygame, sys, constants, music
from menu import Menu
from character_selection import Character_Selection
from player import Player

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
            pygame.mixer.init() #Inicializa el módulo mixer para la música

            # --- MÚSICA --- #
            music.load_music("assets/music/medieval-prueba.mp3")
            music.set_music_volume(0.5)
            music.play_music()

            self.screen = pygame.display.set_mode((constants.SCR_WIDTH, constants.SCR_HEIGHT))
            pygame.display.set_caption("Fablings")

            self.running = True
            self.clock = pygame.time.Clock()

            self.main_menu = Menu(self)
            self.character_selection = Character_Selection(self)
            self.player = None

            self.game_state = "MENU" #Para manejar el estado actual del juego

    
    def set_game_state(self, status):
        self.game_state = status

#Para eventos
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.game_state = "EXIT"
            
            if self.game_state == "MENU":
                self.main_menu.handle_events(event)

                if self.main_menu.is_game_started():
                    self.game_state = "CHARACTER_SELECTION"
                    self.main_menu.reset()

                if self.main_menu.is_game_quit():
                    self.game_state = "EXIT"
                    self.main_menu.reset()

            elif self.game_state == "CHARACTER_SELECTION":
                self.character_selection.handle_events(event)
                
                if self.character_selection.is_ready():
                    character_name = self.character_selection.get_character_selected_name()
                    character_image = self.character_selection.get_character_selected_image_url()
                    self.player = Player(character_name, character_image)
                    self.game_state = "GAME"
                    self.character_selection.reset()
            
            elif self.game_state == "GAME":
                pass

            
 #Para lógica de cada estado del juego     
    def update(self):
        if self.game_state == "MENU":
            #print(f"Estado: {self.game_state}")
            pass

        elif self.game_state == "GAME":
            #print(f"Estado: {self.game_state}")
            pass

        elif self.game_state == "EXIT":
            self.running = False


#Para dibujar en la pantalla
    def draw(self):
        if self.game_state == "MENU":
            self.main_menu.draw(self.screen)

        elif self.game_state == "CHARACTER_SELECTION":
            self.character_selection.draw(self.screen)

        elif self.game_state == "GAME":
            self.screen.fill(constants.COLOR_GRAY)
            self.player.draw(self.screen)
            
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(constants.MAX_FPS)
            self.handle_events()
            self.draw()
            self.update()
              
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()


              