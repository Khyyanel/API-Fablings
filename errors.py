
import pygame, constants

def img_error(image, e):
    print(f"Error al cargar la imagen: {image} - {e}")
    img_transform_sc = pygame.Surface((constants.SCR_WIDTH, constants.SCR_HEIGHT)) 
    img_transform_sc.fill(constants.COLOR_BLACK) 

def music_error(music, e):
    print(f"No se pudo cargar el archivo de música: {e}")
    print(f"Asegúrate de que {music} existe en la misma carpeta o proporciona la ruta correcta.")