import pygame, music, constants, ui
from button import Button

class OptionsMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.volume = 0.5
        self.progress = 10 #simulacion de progreso
        self.font = ui.font_options #exporta la fuente desde el archivo ui
        self.back_button = Button(x = 50, y = 460, width = 150, height = 50, text = "Volver", font = self.font, color = constants.COLOR_WHITE, text_offset_x = 25)
        
        
        pygame.mixer.init() #Inicializa el módulo mixer para la música

            # --- MÚSICA --- #
        music.load_music("assets/music/medieval-prueba.mp3")
        music.set_volume(self.volume)
        music.play_music()
        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_MINUS:
                self.volume = max (0.0, self.volume - 0.1)
                pygame.mixer.music.set_volume(self.volume)
            elif event.key == pygame.K_KP_PLUS:
                self.volume = min(1.0, self.volume + 0.1)
                pygame.mixer.music.set_volume(self.volume)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                self.game_manager.set_game_state("MENU")
                
    def draw(self, screen):
        screen.blit(ui.img_options_scaled, (0,0)) #añade el fondo desde el archivo ui
        font = ui.font_options #se declara la fuente
        
        text_vol = font.render(f"Volumen:  {int(self.volume * 100)}%", True, (255, 255, 255))
        screen.blit(text_vol, (100, 100))
        
        screen.blit(font.render("+ / - para ajustar volumen", True, (255, 255, 255)), (100, 140))
        text_credits = "Creditos" #Hice los textos por separado asi quedaban uno abajo del otro
        text_names = "Hecho por Uriel, Kiara, Hernán y Agostina"
        text_credits_draw = font.render(text_credits, True, (255, 255, 255)) #Convierte al texto para poder mostrar en pantalla
        text_names_draw = font.render(text_names, True, (255, 255, 255))
        
        screen.blit(text_credits_draw, (385, 280)) #Los muestra en la pantalla y le da su ubicacion
        screen.blit(text_names_draw, (125, 330))
        
        self.back_button.draw(screen)
        
class TutorialScreen:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.images = [
            pygame.image.load ("tutorial/tutorial1.png"), 
            pygame.image.load ("tutorial/tutorial2.png"),
            pygame.image.load ("tutorial/tutorial3.png")
        ]
        self.current_index = 0
        self.next_button = pygame.Rect (650, 500, 100, 40)
        self.prev_button = pygame.Rect (50, 500, 100, 40)
        self.back_button = pygame.Rect (350, 500, 100, 40)
        self.tutorial_button = pygame.Rect (250, 400, 250, 40)
        
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.next_button.collidepoint(event.pos):
                if self.current_index < len(self.images) - 1:
                    self.current_index += 1
            elif self.prev_button.collidepoint(event.pos):
                if self.current_index > 0:
                    self.current_index -= 1
            elif self.back_button.collidepoint(event.pos):
                self.game_manager.back_to_options_menu()
                if self.tutorial_button.collidepoint(event.pos):
                    self.game_manager.go_to_tutorial()
                elif self.back_button.collidepoint(event.pos):
                    self.game_manager.set_game_state("MENU")
                
    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.images[self.current_index], (100, 50)) # ajusta la posición según mis imágenes
        
        font = pygame.font.SysFont(None, 30)
        
        pygame.draw.rect(screen, (0, 100, 200), self.prev_button)
        screen.blit(font.render("←", True, (255, 255, 255)), (self.prev_button.x + 35, self.prev_button.y + 5))
        
        pygame.draw.rect(screen, (0, 100, 200), self.next_button)
        screen.blit(font.render("→", True, (255, 255, 255)), (self.next_button.x + 35, self.next_button.y + 5))
        
        pygame.draw.rect(screen, (100, 100, 100), self.back_button)
        screen.blit(font.render("Volver", True, (255, 255, 255)), (self.back_button.x + 10, self.back_button.y + 5))
        
        pygame.draw.rect(screen, (100, 100, 100), self.tutorial_button)
        screen.blit(font.render("Ver Tutorial", True, (255, 255, 255)), (self.tutorial_button.x + 30, self.tutorial_button.y +5))
        