import pygame, constants, ui, errors
from button import Button

class Character_Selection:
    def __init__(self, game_manager_instance):
        self.game_manager = game_manager_instance
        self._game_started = False

        self.character_selected_name = None
        self.character_selected_image = None

        self.area_selected = None
        self.position_selected = 1
        self.characters = {
            "personaje1": {"rect": pygame.Rect(130, 130, 210, 350), "pos":1, "image_path": "assets/img/personaje1.png", "image": None},
            "personaje2": {"rect": pygame.Rect(374, 130, 210, 350),"pos":2, "image_path": "assets/img/personaje2.png", "image": None},
            "personaje3": {"rect": pygame.Rect(625, 130, 210, 350),"pos":3, "image_path": "assets/img/personaje3.png", "image": None}
        }

        for name, data in self.characters.items():
            try: 
                image = pygame.image.load(data["image_path"]).convert_alpha()
                data["image"] = pygame.transform.scale(image, (data["rect"].width, data["rect"].height))
            except pygame.error as e:
                errors.img_error(data["image_path"], e)
                data["image"] = None
                

        self.tutorial_button = Button(
            x = 60,
            y = 45,
            width = constants.BUTTON_WIDTH, 
            height = constants.BUTTON_HEIGHT,
            text = "Tutorial",
            font = ui.font_button, 
            color = constants.COLOR_WHITE
        )

        self.character_select_button = Button(
            x = constants.SCR_WIDTH - 250,
            y = 15,
            width = constants.BUTTON_WIDTH, 
            height = constants.BUTTON_HEIGHT,
            text = "Aceptar",
            font = ui.font_button, 
            color = constants.COLOR_GRAY
        )

        self.character_back_button = Button(
            x = constants.SCR_WIDTH - 250,
            y = 70,
            width = constants.BUTTON_WIDTH, 
            height = constants.BUTTON_HEIGHT,
            text = "Regresar",
            font = ui.font_button, 
            color = constants.COLOR_BLUE, 
            text_offset_x = 2
        )



    def reset(self):
        self.character_selected_name = None
        self.character_selected_image = None
        self.area_selected = None
        self.position_selected = 1
        self._game_started = False

    def handle_events(self, event):
         if event.type == pygame.MOUSEBUTTONDOWN:
             mouse_pos = event.pos
             
             #Lógica de botón de volver
             if self.character_back_button.collidepoint(event.pos):
                self.reset()
                self.game_manager.set_game_state("MENU")

            #Lógica para selección de personaje
             for name, data in self.characters.items():
                 if data["rect"].collidepoint(mouse_pos):
                    self.character_selected_name = name
                    self.character_selected_image = data["image_path"]
                    self.area_selected = data["rect"]
                    self.position_selected = data["pos"]
                    break #salir del bloque una vez detectada la colisión
                 
             if self.character_selected_name:
                 if self.character_select_button.collidepoint(event.pos):
                    self._game_started = True #listo para jugar


    def draw(self, screen):
        screen.blit(ui.img_transform_sc, (0,0)) #imagen de fondo

        self.draw_buttons(screen)
        
        #Dibujo de personajes en cada rectángulo
        for name, data in self.characters.items():
                if data["image"]:
                    screen.blit(data["image"], data["rect"].topleft)

        if self.area_selected:
            pygame.draw.rect(screen, constants.COLOR_YELLOW, self.area_selected, 5)
           # pygame.draw.rect(screen, constants.COLOR_GREEN, ui.character_select_button)
            self.character_select_button.color = constants.COLOR_GREEN

        else:
            self.character_select_button.color = constants.COLOR_GRAY

        #screen.blit(ui.text_ok_button, (ui.character_select_button.x + 12, ui.character_select_button.y + 10))
        #screen.blit(ui.text_tutorial_button, (ui.tutorial_button.x + 8, ui.tutorial_button.y + 10))

    
    def draw_buttons(self, screen):
        self.character_back_button.draw(screen)
        self.tutorial_button.draw(screen)
        self.character_select_button.draw(screen)

        


    def is_ready(self):
        return self._game_started
    
    def get_character_selected_name(self) -> str:
        return self.character_selected_name
    
    def get_character_selected_image_url(self) -> str:
        return self.character_selected_image
