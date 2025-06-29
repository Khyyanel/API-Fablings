import pygame, constants

class Button:
    def __init__(self, x, y, width, height, text, font, color = constants.COLOR_WHITE, text_offset_x = 5):

        self.rect = pygame.Rect(x, y, width, height) #crea un rectángulo
        self.text = text
        self.font = font
        self.color = color

        # Renderizar el texto una sola vez al inicializar el botón para optimizar
        self.text_surface = (self.font).render(self.text, True, 0) # Texto siempre negro
        
        #Texto del botón
        self.text_offset_x = text_offset_x # Espacio desde el centro para el texto
        self.text_rect = self.text_surface.get_rect(midleft=(self.rect.left + self.text_offset_x, self.rect.centery)) #centrar el texto en el medio del botón

        #Si el botón tiene un icono o imagen, se usarán estas líneas
        self.icon_image = None
        self.icon_rect = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8) #Dibujar el color de fondo para el botón 
        pygame.draw.rect(screen, constants.COLOR_BLACK, self.rect, 2, border_radius=8)  # Dibujar un borde alrededor del botón

        screen.blit(self.text_surface, self.text_rect)  # Dibujar el texto del botón


    def collidepoint(self, pos):
        return self.rect.collidepoint(pos) 

