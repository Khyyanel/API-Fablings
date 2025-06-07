"""
UI = Interfaz de Usuario. 
Aquí guardamos las fuentes, imágenes de menús y lo relacionado a la estética de las interfaces.
"""

import pygame, constants, errors

pygame.font.init()

### MENU PRINCIPAL ###
#Imágenes
try:
    img_initial_bg = pygame.image.load("assets/img/fondo inicio.png")
    img_transform_bg = pygame.transform.scale(img_initial_bg, (constants.SCR_WIDTH, constants.SCR_HEIGH))
except pygame.error as e:
    errors.img_error("assets/img/fondo inicio.png", e)

#Fuentes
try:
    font_button = pygame.font.Font("assets/fonts/Daydream.ttf", 20)
    font_title = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 100)
except pygame.error as e:
    print("No se pudieron cargar las fuentes - {e}")

#Botones
start_button = pygame.Rect(constants.SCR_WIDTH / 2 - 100, constants.SCR_HEIGH / 2 - 10 , 150, 50)
exit_button = pygame.Rect(constants.SCR_WIDTH / 2 - 100, constants.SCR_HEIGH / 2 + 70 , 150, 50)
text_start_button = font_button.render("Jugar", True, 0)
text_exit_button = font_button.render("Salir", True, 0)
title = font_title.render("FABLINGS", True, constants.COLOR_RED)

### SELECCIÓN PERSONAJE ###
try:
    img_character_selec_screen = pygame.image.load("assets/img/seleccion-personaje.png")
    img_transform_sc = pygame.transform.scale(img_character_selec_screen, (constants.SCR_WIDTH, constants.SCR_HEIGH))
except pygame.error as e:
    errors.img_error("assets/img/seleccion-personaje.png", e)
    
