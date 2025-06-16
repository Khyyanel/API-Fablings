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
    img_transform_bg = pygame.transform.scale(img_initial_bg, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/fondo inicio.png", e)

#Fuentes
try:
    font_button = pygame.font.Font("assets/fonts/Daydream.ttf", 20)
    font_title = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 100)
except pygame.error as e:
    print("No se pudieron cargar las fuentes - {e}")

#Textos
title_menu = font_title.render("FABLINGS", True, constants.COLOR_RED)

#Botones
start_button = pygame.Rect(constants.BUTTON_LEFT, constants.START_BUTTON_TOP , constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
exit_button = pygame.Rect(constants.BUTTON_LEFT, constants.EXIT_BUTTON_TOP , constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
options_button = pygame.Rect(constants.BUTTON_LEFT, constants.OPTIONS_BUTTON_TOP , constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

text_start_button = font_button.render("Jugar", True, 0)
text_exit_button = font_button.render("Salir", True, 0)
text_options_button = font_button.render("Opciones", True, 0)



### SELECCIÓN PERSONAJE ###
try:
    img_character_selec_screen = pygame.image.load("assets/img/seleccion-personaje.png")
    img_transform_sc = pygame.transform.scale(img_character_selec_screen, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/seleccion-personaje.png", e)

#Botones
character_select_button = pygame.Rect(constants.SCR_WIDTH - 250, 15, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
tutorial_button = pygame.Rect(60, 45, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
character_back_button = pygame.Rect(constants.SCR_WIDTH - 250, 70, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

text_ok_button = font_button.render("Aceptar", True, 0)
text_tutorial_button = font_button.render("Tutorial", True, 0)
text_back_button = font_button.render("Volver", True, 0)

def texto_prueba(texto, screen):
    texto_prueba = font_button.render(texto, True, 0)
    screen.blit(texto_prueba, (constants.TITLE_MENU_WIDTH, constants.TITLE_MENU_HEIGHT))