import pygame, random, constants, ui
from button import Button

class Event():
    def __init__(self): 
        self.options_buttons = []
        self.current_event_image = None

         # Cargar las imágenes una sola vez al inicializar la clase
        self.option_images = {
            "pericia": pygame.transform.scale(pygame.image.load("assets/img/pericia.png").convert_alpha(), 
                                               (constants.EVENT_OPTION_IMAGE_WIDTH, constants.EVENT_OPTION_IMAGE_HEIGHT)),
            "suerte": pygame.transform.scale(pygame.image.load("assets/img/suerte.png").convert_alpha(),
                                              (constants.EVENT_OPTION_IMAGE_WIDTH, constants.EVENT_OPTION_IMAGE_HEIGHT)),
            "supervivencia": pygame.transform.scale(pygame.image.load("assets/img/supervivencia.png").convert_alpha(),
                                                     (constants.EVENT_OPTION_IMAGE_WIDTH, constants.EVENT_OPTION_IMAGE_HEIGHT)),
            "conocimiento": pygame.transform.scale(pygame.image.load("assets/img/conocimiento.png").convert_alpha(),
                                                    (constants.EVENT_OPTION_IMAGE_WIDTH, constants.EVENT_OPTION_IMAGE_HEIGHT))
        }

        self.events = {
            "evento0": {
                "image_path": "assets/img/events/evento0.png",
                "title": "Ruinas", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type": "conocimiento",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "suerte",
                "option3_title": "Descansar2", "option3_description": "Éxito: Obtiene 2 Amuletos", "option3_type": "pericia"
            }
        }
    
    def draw(self, screen):
        self.current_event_image = pygame.image.load(self.events["evento0"]["image_path"]).convert_alpha()
        self.current_event_image = pygame.transform.scale(self.current_event_image, (constants.EVENT_IMAGE_WIDTH, constants.EVENT_IMAGE_HEIGHT))

        screen.blit(self.current_event_image, (constants.EVENT_IMAGE_X, constants.EVENT_IMAGE_Y))
        
        self.draw_buttons(screen)


    def draw_buttons(self, screen):

        button1 = Button(
            x=constants.EVENT_OPTION_IMAGE_FIRST_X, 
            y=constants.EVENT_OPTION_IMAGE_FIRST_Y, width=250, height=60,
            text="Boton",
            icon_image_surface= self.option_images["conocimiento"],
            font = ui.font_button_events,
            action=None
        )
        
        button1.draw(screen)
