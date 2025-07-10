"""
UI = Interfaz de Usuario. 
Aquí guardamos las fuentes, textos fijos e imágenes de fondo.
"""

import pygame, constants, errors

pygame.font.init() #Inicializamos las fuentes

#Fuentes
try:
    #Menú principal
    #font_title = pygame.font.Font("assets/fonts/TheFrightHouseDEMO.otf", 100)
    font_button = pygame.font.Font("assets/fonts/Linex Sweet Std Bold.otf", 30)
    
    #Menu Opciones
    font_options = pygame.font.Font("assets/fonts/Linex Sweet Std Bold.otf", 36)
    
    #Juego
    font_title_event = pygame.font.Font("assets/fonts/FANTASY MAGIST.otf", 30) 
    font_description_event = pygame.font.Font("assets/fonts/Linex Sweet Std Bold.otf", 18) 
    font_button_events_title = pygame.font.Font("assets/fonts/Linex Sweet Std Bold.otf", 18)
    font_button_events_description = pygame.font.Font("assets/fonts/Linex Sweet Std Bold.otf", 15) 
    font_stadistics = pygame.font.Font("assets/fonts/Linex Sweet Std Bold.otf", 25) 
except pygame.error as e:
    print("No se pudieron cargar las fuentes - {e}")

#----------MENU PRINCIPAL----------#
#Imágenes
try:
    img_initial_bg = pygame.image.load("assets\img\FondoTitulo.png")
    img_initial_scaled = pygame.transform.scale(img_initial_bg, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/fondo inicio.png", e)
    
    
#----------MENU OPCIONES----------------------#    
try:
    img_bg_options = pygame.image.load("assets\img\FondoOpciones.png")
    img_options_scaled = pygame.transform.scale(img_bg_options, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/fondo inicio.png", e)

#Textos
#title_menu = font_title.render("FABLINGS", True, constants.COLOR_RED)


#----------SELECCIÓN PERSONAJE----------#
try:
    img_character_selec_screen = pygame.image.load("assets/img/seleccion-personaje.png")
    img_transform_sc = pygame.transform.scale(img_character_selec_screen, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/seleccion-personaje.png", e)

#----------EVENTOS----------------------#
try:
    img_event_bg = pygame.image.load("assets/img/Fondo.png")
    img_bg_scaled = pygame.transform.scale(img_event_bg, (constants.SCR_WIDTH, constants.SCR_HEIGHT))
except pygame.error as e:
    errors.img_error("assets/img/Fondo.png", e)




