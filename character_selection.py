import pygame, constants, ui

class Character_Selection:
    def __init__(self):
        self.character_selected = None
        self.area_selected = None
        self.position_selected = 1
        self._ready = False
        self.areas_characters = {
            "personaje1": {"rect": pygame.Rect(130, 130, 210, 350), "pos":1},
            "personaje2": {"rect": pygame.Rect(374, 130, 210, 350),"pos":2},
            "personaje3": {"rect": pygame.Rect(625, 130, 210, 350),"pos":3}
        }

    def handle_events(self, event):
         if event.type == pygame.MOUSEBUTTONDOWN:
             mouse_pos = event.pos

             for name, data in self.areas_characters.items():
                 if data["rect"].collidepoint(mouse_pos):
                    self.character_selected = name
                    self.area_selected = data["rect"]
                    self.position_selected = data["pos"]
                    print(f"Personaje seleccionado: {name}")
                    break #salir del bloque una vez detectada la colisión
                 
             if self.character_selected:
                 if ui.character_select_button.collidepoint(event.pos):
                    self._ready = True

    def draw(self, screen):
        screen.blit(ui.img_transform_sc, (0,0)) #imagen de fondo
        
        if self.area_selected:
            pygame.draw.rect(screen, constants.COLOR_YELLOW, self.area_selected, 5)
            pygame.draw.rect(screen, constants.COLOR_GREEN, ui.character_select_button)

        else:
            pygame.draw.rect(screen, constants.COLOR_GRAY, ui.character_select_button)

        screen.blit(ui.text_ok_button, (ui.character_select_button.x + 18, ui.character_select_button.y + 10))
            
    def is_ready(self):
        return self._ready
    
    def get_character(self):
        return self.character_selected
