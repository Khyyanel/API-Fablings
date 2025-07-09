import pygame, random, constants, ui, errors
from button_events import Button_Options

class Event():
    def __init__(self): 
        self.events = {
            "event0": {
                "image_path": "assets/img/events/1.png",
                "title": "Ruinas1", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type":"conocimiento",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "suerte",
                "option3_title": "titulo", "option3_description": "Éxito: Obtiene 2 Amuletos", "option3_type": "pericia",
                "exito": None,
                "fracaso": None, 
                "num_opciones": 3
            },

            "event1": {
                "image_path": "assets/img/events/1.png",
                "title": "Ruinas2", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type": "suerte",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "supervivencia",
                "option3_title": 1, "option3_description": "...", "option3_type": "conocimiento", 
                "exito": None,
                "fracaso": None, 
                "num_opciones": 3
            },

            "event2": {
                "image_path": "assets/img/events/1.png",
                "title": "Ruinas3", "description": "El camino se abrió ante un asentamiento hace mucho tiempo olvidado. El silencio parecía gobernar el aire, y las piedras me recibieron con la indiferencia del paso del tiempo.",
                "option1_title": "Rebuscar", "option1_description": "Éxito: Obtiene 2 Amuletos", "option1_type": "suerte",
                "option2_title": "Descansar", "option2_description": "Éxito: Obtiene 2 Amuletos", "option2_type": "suerte",
                "option3_title": 1, "option3_description": "Éxito: Obtiene 2 Amuletos", "option3_type": "conocimiento", 
                "exito": None,
                "fracaso": None, 
                "num_opciones": 3
            }
        }

        self.current_event = None
        self.current_event_image = None

        self.available_events = list(self.events.keys()) # ["event0", "event1", "event2", etc.]
        self.playable_events = []
        self.past_events = []
        self.choose_other_event = True

        self.button1 = None
        self.button2 = None
        self.button3 = None

        self.current_stadistic = None

        self.events_playable() #Crear la lista de eventos jugables
        self.choose_event_random() #Elegir el primer evento
  
    
    def create_buttons(self):
        y_offset = 60
        current_event = self.current_event

        if self.current_event["num_opciones"] == 1:
            self.button1 = Button_Options(
                x=constants.EVENT_OPTION_IMAGE_FIRST_X, 
                y=constants.EVENT_OPTION_IMAGE_FIRST_Y, 
                width=constants.BUTTON_OPTION_WIDTH, 
                height=constants.BUTTON_OPTION_HEIGHT,
                title= current_event["option1_title"],
                description= current_event["option1_description"],
                icon_path= f"assets/img/{current_event["option1_type"]}.png"
            )
        elif self.current_event["num_opciones"] == 2:
                
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

        elif self.current_event["num_opciones"] == 3:
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
                    title= current_event["option2_title"],
                    description= current_event["option2_description"],
                    icon_path= f"assets/img/{current_event["option2_type"]}.png"
                )


    def draw(self, screen):
        image_path = self.current_event["image_path"]
        self.current_event_image = pygame.image.load(image_path).convert_alpha()
        self.current_event_image = pygame.transform.scale(self.current_event_image, (constants.EVENT_IMAGE_WIDTH, constants.EVENT_IMAGE_HEIGHT))

        screen.blit(self.current_event_image, (constants.EVENT_IMAGE_X, constants.EVENT_IMAGE_Y))
        
        self.draw_buttons(screen)
        self.draw_title_and_description(screen)


    def draw_buttons(self, screen):
        if self.current_event["num_opciones"] == 1:
            self.button1.draw(screen)

        elif self.current_event["num_opciones"] == 2:
            self.button1.draw(screen)
            self.button2.draw(screen)
        
        elif self.current_event["num_opciones"] == 3:
            self.button1.draw(screen)
            self.button2.draw(screen)
            self.button3.draw(screen)

    def draw_title_and_description(self,screen):
        current_event = self.current_event

        title = ui.font_title_event.render(current_event["title"], True, constants.COLOR_BLACK)
        description = ui.font_description_event.render(current_event["description"], True, constants.COLOR_BLACK)

        screen.blit(title, (constants.TITLE_EVENT_TEXT_X, constants.TITLE_EVENT_TEXT_Y))

        description_rect = pygame.Rect(
            constants.DESCRIPTION_EVENT_TEXT_X, 
            constants.DESCRIPTION_EVENT_TEXT_Y, 
            constants.DESCRIPTION_EVENT_TEXT_WIDTH, # Ancho máximo para la descripción
            constants.DESCRIPTION_EVENT_TEXT_HEIGHT # Alto máximo para la descripción
        )

        self.draw_wrapped_text(
            screen,
            current_event["description"],
            description_rect     
        )

    def events_playable(self):
        # Filtrar los eventos que ya se han mostrado
        for name_event in self.available_events: 
            if name_event not in self.past_events:
                self.playable_events.append(name_event)

            if not self.playable_events:
                print("¡Todos los eventos se han jugado! Reiniciando eventos pasados.")
                self.past_events = [] #reiniciamos los eventos
                self.playable_events = self.available_events # Reiniciar para que todos estén disponibles de nuevo


    def choose_event_random(self):
        if self.choose_other_event:
            # Elegir una clave de evento aleatoria de los que quedan
            selected_event = random.choice(self.playable_events)

            # Actualizar el evento actual y añadirlo a los eventos pasados
            self.current_event = self.events[selected_event]
            self.past_events.append(selected_event)

            # Opcional: imprimir para verificar
            print(f"Evento seleccionado: {selected_event}")
            print(f"Eventos pasados: {self.past_events}")

            self.choose_other_event = False
            self.create_buttons()
            


    def time_to_choose(self):
        if self.choose_other_event== True:
            self.choose_event_random()
        else:
            pass

    def draw_wrapped_text(self, surface, text, rect, font=ui.font_description_event , color=constants.COLOR_BLACK):
        # Crear una superficie temporal para dibujar el texto y luego copiarla
        # Sirve para que el texto se dibuje dentro de los límites del rect

        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            # Prueba si la palabra actual + lo que ya tengo en la linea actual excede el ancho del rectángulo
            test_line = ' '.join(current_line + [word])
            text_width, text_height = font.size(test_line)
            
            if text_width <= rect.width:
                current_line.append(word)
            else:
                # Si excede, guardamos la linea actual y empezamos una nueva
                lines.append(' '.join(current_line))
                current_line = [word] # La palabra que excedió empieza la nueva línea

        lines.append(' '.join(current_line)) # Agrega la última línea

        #Dibujamos cada línea
        y_offset = 0
        line_spacing = 5 # Espacio entre líneas

        for line in lines:
            line_surface = font.render(line, True, color) # Si la línea actual excede la altura del área, truncamos el texto
            
            if rect.top + y_offset + line_surface.get_height() <= rect.bottom:
                surface.blit(line_surface, (rect.left, rect.top + y_offset)) #<- Aquí las dibujamos en la pantalla
                y_offset += line_surface.get_height() + line_spacing
            else:
                break # Detener si no hay espacio para más líneas


    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if self.button1.collidepoint(mouse_pos):
                print("Elegiste opcion1")
                self.current_stadistic = self.current_event["option1_type"]
            elif self.button2.collidepoint(mouse_pos):
                print("Elegiste opcion2")
                self.current_stadistic = self.current_event["option2_type"]
            elif self.button3.collidepoint(mouse_pos):
                print("Elegiste opcion3")
                self.current_stadistic = self.current_event["option3_type"]

    def get_current_stadistic(self):
        return self.current_stadistic
