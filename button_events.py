import pygame, constants, errors, ui
from button import Button

class Button_Options(Button):
    def __init__(self, x, y, width, height, title: str, description: str, icon_path: str, font_title=ui.font_button_events_title, color=constants.COLOR_WHITE):
        # Llama al constructor de la clase padre (Button)
        # Pasa todos los argumentos que Button necesita

        # Pasamos el título como 'text' al Button padre, 
        # le pasamos la fuente de ui.font_button_events_title y le asignamos un text_offset_x = 0
        # aunque Button_Options luego lo gestionará de forma diferente.
        super().__init__(x, y, width, height, title, font_title, color, text_offset_x = 0)
        self.font_description = ui.font_button_events_description

        self.title_text = title
        self.description_text = description
        self.font_title = font_title # = ui.font_button_events_title
        self.font_description = ui.font_button_events_description
        self.icon_path = icon_path

    
        # Renderizar el título y la descripción
        self.title_surface = self.font_title.render(self.title_text, True, constants.COLOR_BLACK)
        # Usa un color diferente para la descripción para distinguirla
        self.description_surface = self.font_description.render(self.description_text, True, constants.COLOR_DARK_GRAY)

        # Atributos para las posiciones de título y descripción
        self.title_rect = self.title_surface.get_rect()
        self.description_rect = self.description_surface.get_rect()


    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
        pygame.draw.rect(screen, constants.COLOR_BLACK, self.rect, 2, border_radius=8)

        try:
            icon = pygame.image.load(self.icon_path).convert_alpha()
            self.icon_image = pygame.transform.scale(icon, (constants.EVENT_OPTION_IMAGE_WIDTH, constants.EVENT_OPTION_IMAGE_HEIGHT))
            self.icon_rect = self.icon_image.get_rect() 
        except pygame.error as e:
            errors.img_error(self.icon_path, e)

        self._calculate_text_and_icon_positions()

        if self.icon_image and self.icon_rect:
            screen.blit(self.icon_image, self.icon_rect) #Dibuja el icono si hay

         # Dibuja el título y la descripción
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.description_surface, self.description_rect)


    def _calculate_text_and_icon_positions(self):
        # Esta función ahora solo se encarga de calcular las posiciones. No dibuja nada
        content_start_x = self.rect.left + 10 # Margen desde el borde izquierdo del botón

        if self.icon_image and self.icon_rect:  # Si hay un icono, posicionarlo
            self.icon_rect.midleft = (content_start_x, self.rect.centery)
            text_start_x = self.icon_rect.right + 10 # Margen entre el icono y el texto
        else:
            text_start_x = content_start_x  # Si no hay icono, el texto comienza en el margen inicial

        # Calcular el centro vertical del área de texto combinada (título + descripción)
        # Asumiendo que el texto se apilará verticalmente
        total_text_height = self.title_rect.height + self.description_rect.height + 5 # 5px de espacio entre ellos
        text_center_y = self.rect.centery

        # Posicionar el título y la descripción
        # El título va encima, alineado a la izquierda después del ícono
        self.title_rect.midleft = (text_start_x, text_center_y - total_text_height / 2 + self.title_rect.height / 2)
        
        # La descripción va debajo del título
        self.description_rect.midleft = (text_start_x, self.title_rect.bottom + 5 + self.description_rect.height / 2 - self.description_rect.height / 2) 
        # Ajuste para centrar correctamente si el midleft no lo pone en el punto correcto.
        # Una forma más sencilla para la descripción:
        self.description_rect.topleft = (text_start_x, self.title_rect.bottom + 5)

