import pygame, constants

class Button:
    def __init__(self, x, y, width, height, text, font, color = constants.COLOR_WHITE, text_offset_x = 5, action=None):

        self.rect = pygame.Rect(x, y, width, height) #crea un rectángulo

        self.text = text
        
        self.font = font
        self.color = color
        self.action = action # La función que se ejecutará al hacer clic ---------------------------
        

        # Renderizar el texto una sola vez al inicializar el botón para optimizar
        self.text_surface = (self.font).render(self.text, True, 0) # Texto siempre negro

        self.icon_image = None
        self.icon_rect = None

        # Posicionar el icono y el texto dentro del Rect principal del botón.
        # Ajusta estas coordenadas según cómo quieras que se vean en tu diseño.
        # Aquí, el icono se coloca a la izquierda del centro y el texto a la derecha.
        
        self.text_offset_x = text_offset_x # Espacio desde el centro para el texto
        
        
        
        self.text_rect = self.text_surface.get_rect(midleft=(self.rect.left + self.text_offset_x, self.rect.centery))

    def draw(self, screen):
        """
        Dibuja el botón en la pantalla.

        Args:
            screen (pygame.Surface): La superficie de Pygame donde se dibujará el botón.
        """
        #Dibujar el color de fondo para el botón 
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
        # Dibujar un borde alrededor del botón
        pygame.draw.rect(screen, constants.COLOR_BLACK, self.rect, 2, border_radius=8)

        # Dibujar el texto del botón
        screen.blit(self.text_surface, self.text_rect)

    def draw_image(self,screen, icon_image_surface):
        icon_padding = 10 # Espacio desde el borde izquierdo para el icono
        self.draw(screen)
        # Dibujar la imagen del icono
        self.icon_image = icon_image_surface # La superficie de la imagen del icono
        self.icon_rect = self.icon_image.get_rect(midleft=(self.rect.left + icon_padding, self.rect.centery))
        screen.blit(self.icon_image, self.icon_rect)


    def collidepoint(self, pos):
        return self.rect.collidepoint(pos) 

    def handle_event(self, event):
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 es el botón izquierdo del ratón
                # La clave: verifica si la posición del clic está dentro del Rect del botón
                if self.rect.collidepoint(event.pos):
                    # print(f"¡Botón '{self.text}' ({self.option_type}) clicado!") # Para depuración
                    if self.action:
                        self.action() # Ejecuta la función asociada al botón
                    return True # Indica que este botón fue el que recibió el clic
        return False


