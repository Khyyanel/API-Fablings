"""
UI = Interfaz de Usuario. 
Aquí guardamos las fuentes, textos fijos e imágenes de fondo.
"""

import pygame, constants, errors

pygame.font.init() #Inicializamos las fuentes

#Fuentes
try:
    #Menú principal
    font_title = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 100)
    font_button = pygame.font.Font("assets/fonts/Daydream.ttf", 20)
    
    #Juego
    font_title_event = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 30) 
    font_description_event = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 14) 
    font_button_events_title = pygame.font.Font("assets/fonts/Daydream.ttf", 13)
    font_button_events_description = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 13) 
    font_stadistics = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 25) 
except pygame.error as e:
    print("No se pudieron cargar las fuentes - {e}")

#----------MENU PRINCIPAL----------#
#Imágenes
try:
    img_initial_bg = pygame.image.load("assets/img/fondo inicio.png")
    img_bg_scaled = pygame.transform.scale(img_initial_bg, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/fondo inicio.png", e)

#Textos
title_menu = font_title.render("FABLINGS", True, constants.COLOR_RED)

#Botones
#exit_button = pygame.Rect(constants.BUTTON_LEFT, constants.EXIT_BUTTON_TOP , constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
#options_button = pygame.Rect(constants.BUTTON_LEFT, constants.OPTIONS_BUTTON_TOP , constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

#text_start_button = font_button.render("Jugar", True, 0) #render("texto a mostrar", "Mostrar", Color. Si es 0 = negro)
#text_exit_button = font_button.render("Salir", True, 0)
#text_options_button = font_button.render("Opciones", True, 0)


#----------SELECCIÓN PERSONAJE----------#
try:
    img_character_selec_screen = pygame.image.load("assets/img/seleccion-personaje.png")
    img_transform_sc = pygame.transform.scale(img_character_selec_screen, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/seleccion-personaje.png", e)

#text_ok_button = font_button.render("Aceptar", True, 0)
#text_tutorial_button = font_button.render("Tutorial", True, 0)
#text_back_button = font_button.render("Volver", True, 0)



