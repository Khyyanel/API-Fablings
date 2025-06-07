
import pygame, constants

def img_error(image, e):
    print(f"Error al cargar la imagen: {image} - {e}")
    img_transform_sc = pygame.Surface((constants.SCR_WIDTH, constants.SCR_HEIGH)) 
    img_transform_sc.fill(constants.COLOR_BLACK) 
