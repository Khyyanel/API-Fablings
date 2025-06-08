import pygame, constants, ui

class Character_Selection:
    def __init__(self, game_manager_instance):
        self.game_manager = game_manager_instance
        self._game_started = False
        self.character_selected = None
        self.area_selected = None
        self.position_selected = 1
        self.areas_characters = {
            "personaje1": {"rect": pygame.Rect(130, 130, 210, 350), "pos":1},
            "personaje2": {"rect": pygame.Rect(374, 130, 210, 350),"pos":2},
            "personaje3": {"rect": pygame.Rect(625, 130, 210, 350),"pos":3}
        }

    def reset(self):
        self.character_selected = None
        self.area_selected = None
        self.position_selected = 1
        self._game_started = False

    def handle_events(self, event):
         if event.type == pygame.MOUSEBUTTONDOWN:
             mouse_pos = event.pos
             
             #Lógica de botón de volver
             if ui.character_back_button.collidepoint(event.pos):
                self.reset()
                self.game_manager.set_game_state("MENU")

            #Lógica para selección de personaje
             for name, data_characters in self.areas_characters.items():
                 if data_characters["rect"].collidepoint(mouse_pos):
                    self.character_selected = name
                    self.area_selected = data_characters["rect"]
                    self.position_selected = data_characters["pos"]
                    print(f"Personaje seleccionado: {name}")
                    break #salir del bloque una vez detectada la colisión
                 
             if self.character_selected:
                 if ui.character_select_button.collidepoint(event.pos):
                    self._game_started = True #listo para jugar


    def draw(self, screen):
        screen.blit(ui.img_transform_sc, (0,0)) #imagen de fondo
        pygame.draw.rect(screen, constants.COLOR_BLUE, ui.character_back_button)
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.tutorial_button)
        
        if self.area_selected:
            pygame.draw.rect(screen, constants.COLOR_YELLOW, self.area_selected, 5)
            pygame.draw.rect(screen, constants.COLOR_GREEN, ui.character_select_button)

        else:
            pygame.draw.rect(screen, constants.COLOR_GRAY, ui.character_select_button)

        screen.blit(ui.text_ok_button, (ui.character_select_button.x + 12, ui.character_select_button.y + 10))
        screen.blit(ui.text_tutorial_button, (ui.tutorial_button.x + 8, ui.tutorial_button.y + 10))
        screen.blit(ui.text_back_button, (ui.character_back_button.x + 18, ui.character_back_button.y + 10))


    def is_ready(self):
        return self._game_started
    
    def get_character(self):
        return self.character_selected
