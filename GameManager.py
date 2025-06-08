"""
Un GameManager es ideal para centralizar la lógica principal del juego,
 la gestión de estados (menú, juego, pausa, etc.), el bucle principal y la interacción con Pygame.
"""

import pygame, constants, ui
from menu import Menu
from character_selection import Character_Selection

class GameManager():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCR_WIDTH, constants.SCR_HEIGH))
        pygame.display.set_caption("Fablings")

        self.running = True
        self.clock = pygame.time.Clock()

        self.main_menu = Menu()
        self.character_selection = Character_Selection()
        self.character = None

        self.game_state = "MENU" #Para manejar el estado actual del juego


#Para eventos
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.game_state = "EXIT"
            
            if self.game_state == "MENU":
                self.main_menu.handle_events(event)

                if self.main_menu.is_game_started():
                    self.game_state = "CHARACTER_SELECTION"

                if self.main_menu.is_game_quit():
                    self.game_state = "EXIT"

            elif self.game_state == "CHARACTER_SELECTION":
                self.character_selection.handle_events(event)
                if self.character_selection.is_ready():
                    self.character = self.character_selection.get_character()
                    self.game_state = "GAME"

            
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
            pygame.quit()


#Para dibujar en la pantalla
    def draw(self):
        if self.game_state == "MENU":
            self.main_menu.draw(self.screen)

        elif self.game_state == "CHARACTER_SELECTION":
            self.character_selection.draw(self.screen)

        elif self.game_state == "GAME":
            self.screen.fill(constants.COLOR_GRAY)
            ui.texto_prueba("Elegiste a: " + str(self.character), self.screen)
        
        pygame.display.flip()

    
    def run(self):
        while self.running:
            self.clock.tick(constants.MAX_FPS)
            self.handle_events()
            self.draw()
            self.update()
              
        self.game_state = "EXIT"


              