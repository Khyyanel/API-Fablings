
import pygame, constants

#recibe como parámetro la imagen y el tipo de error
def img_error(image, e):
    print(f"Error al cargar la imagen: {image} - {e}")

def img_error(image):
    print(f"Error al cargar la imagen: {image}")

def music_error(music, e):
    print(f"No se pudo cargar el archivo de música: {e}")
    print(f"Asegúrate de que {music} existe en la misma carpeta o proporciona la ruta correcta.")
