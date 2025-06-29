import pygame, random, constants, ui, errors
from button_events import Button_Options

class Event():
    def __init__(self): 
         # Cargar las imágenes una sola vez al inicializar la clase
        self.image_paths = {
            "pericia": "assets/img/pericia.png",
            "suerte": "assets/img/suerte.png",
            "supervivencia": "assets/img/supervivencia.png",
            "conocimiento": "assets/img/conocimiento.png"
        }

        self.events = {
            "event0": {
                "image_path": "assets/img/events/event0.png",
                "title": "Ruinas", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type":"conocimiento",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "suerte",
                "option3_title": "Descansar2", "option3_description": "Éxito: Obtiene 2 Amuletos", "option3_type": "pericia",
                "exito": None,
                "fracaso": None
            },

            "event1": {
                "image_path": "assets/img/events/event1.png",
                "title": "Ruinas", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type": "suerte",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "supervivencia",
                "option3_title": "Descansar2", "option3_description": "Éxito: Obtiene 2 Amuletos", "option3_type": "conocimiento", 
                "exito": None,
                "fracaso": None
            },

            "event2": {
                "image_path": "assets/img/events/event1.png",
                "title": "Ruinas", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type": "suerte",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "suerte",
                "option3_title": "Descansar2", "option3_description": "Éxito: Obtiene 2 Amuletos", "option3_type": "conocimiento", 
                "exito": None,
                "fracaso": None
            }
        }

        self.current_event = self.events["event1"]
        self.current_event_image = None

        self.button1 = None
        self.button2 = None
        self.button3 = None

        self.create_buttons(self.current_event)


    def upload_to_option_images(self):
        image_paths = {
            "pericia": "assets/img/pericia.png",
            "suerte": "assets/img/suerte.png",
            "supervivencia": "assets/img/supervivencia.png",
            "conocimiento": "assets/img/conocimiento.png"
        }

        for name, path in image_paths.items():
            try:
                image = pygame.image.load(path).convert_alpha()
                self.option_images[name] = pygame.transform.scale(image, (constants.EVENT_OPTION_IMAGE_WIDTH, constants.EVENT_OPTION_IMAGE_HEIGHT))
            
            except pygame.error as e:
                errors.img_error(path, e)
                self.option_images[name] = None
    
    def create_buttons(self, current_event):
        y_offset = 60

        self.button1 = Button_Options(
            x=constants.EVENT_OPTION_IMAGE_FIRST_X, 
            y=constants.EVENT_OPTION_IMAGE_FIRST_Y, 
            width=constants.BUTTON_OPTION_WIDTH, 
            height=constants.BUTTON_OPTION_HEIGHT,
            title= current_event["option1_title"],
            description= current_event["option1_description"],
            icon_path= f"assets/img/{current_event["option1_type"]}.png"
        )

        self.button2 = Button_Options(
            x=constants.EVENT_OPTION_IMAGE_FIRST_X, 
            y=constants.EVENT_OPTION_IMAGE_FIRST_Y + y_offset, 
            width=constants.BUTTON_OPTION_WIDTH, 
            height=constants.BUTTON_OPTION_HEIGHT,
            title= current_event["option2_title"],
            description= current_event["option2_description"],
            icon_path= f"assets/img/{current_event["option2_type"]}.png"
        )

        self.button3 = Button_Options(
            x=constants.EVENT_OPTION_IMAGE_FIRST_X, 
            y=constants.EVENT_OPTION_IMAGE_FIRST_Y + y_offset*2, 
            width=constants.BUTTON_OPTION_WIDTH, 
            height=constants.BUTTON_OPTION_HEIGHT,
            title= current_event["option3_title"],
            description= current_event["option3_description"],
            icon_path= f"assets/img/{current_event["option3_type"]}.png"
        )


    def draw(self, screen):
        self.current_event_image = pygame.image.load(self.events["event0"]["image_path"]).convert_alpha()
        self.current_event_image = pygame.transform.scale(self.current_event_image, (constants.EVENT_IMAGE_WIDTH, constants.EVENT_IMAGE_HEIGHT))

        screen.blit(self.current_event_image, (constants.EVENT_IMAGE_X, constants.EVENT_IMAGE_Y))
        
        self.draw_buttons(screen)


    def draw_buttons(self, screen):
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
