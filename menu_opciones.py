import pygame

class OptionsMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.volume = 0.5
        self.progress = 10 #simulacion de progreso
        self.back_button =pygame.Rect(50, 500, 150, 40)
        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.volume = max (0.0, self.volume - 0.1)
                pygame.mixer.music.set_volume(self.volume)
            elif event.key == pygame.K_RIGHT:
                self.volume = min(1.0, self.volume + 0.1)
                pygame.mixer.music.set_volume(self.volume)
            elif event.key == pygame.K_r:
                self.progress = 0
            elif event.key == pygame.K_c:
                print ("Créditos: Hecho por Kiara, Uriel, Hernán, Nico y Agos")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                self.game_manager.back_to_main_menu()
                
    def draw(self, screen):
        screen.fill((200, 200, 200))
        font = pygame.font.SysFont(None, 36)
        
        text_vol = font.render(f"Volumen: {int(self.volume * 100)}%", True, (0, 0, 0))
        screen.blit(text_vol, (100, 100))
        
        screen.blit(font.render("+ / - para ajustar volumen", True, (0, 0, 0)), (100, 140))
        screen.blit(font.render("Presiona R para reiniciar progreso", True, (0, 0, 0)), (100, 200))
        screen.blit(font.render("Presiona C para ver créditos", True, (0, 0, 0)), (100, 240))
        screen.blit(font.render("Progreso actual: ", + str(self.progress), True, (0, 0, 0)), (100, 280))
        
        pygame.draw.rect(screen, (100, 100, 100), self.back_button)
        screen.blit(font.render("Volver", True, (255, 255, 255)), (self.back_button.x + 20, self.back_button.y + 5))
        
class TutorialScreen:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.images = {
            pygame.image.load ("tutorial/tutorial1.png"), 
            pygame.image.load ("tutorial/tutorial2.png"),
            pygame.image.load ("tutorial/tutorial3.png")
        }
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.tutorial_button.collidepoint(event.pos):
                    self.game_manager.go_to_tutorial()
                elif self.back_button.collidepoint(event.pos):
                    self.game_manager.back_to_main_menu()
                
    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.images[self.current_index], (100, 50)) # ajusta la posición según mis imágenes
        
        font = pygame.font.SysFont(None, 30)
        
        pygame.draw.rect(screen, (0, 100, 200), self.prev_button)
        screen.blit(font.render("←", True (255, 255, 255)), (self.prev_button.x + 35, self.prev_button.y + 5))
        
        pygame.draw.rect(screen, (0, 100, 200), self.next_button)
        screen.blit(font.render("→", True (255, 255, 255)), (self.prev_button.x + 35, self.prev_button.y + 5))
        
        pygame.draw.rect(screen, (100, 100, 100), self.back_button)
        screen.blit(font.render("Volver", True (255, 255, 255)), (self.back_button.x + 10, self.back_button.y + 5))
        
        pygame.draw.rect(screen, (100, 100, 100), self.tutorial_button)
        screen.blit(font.render("Ver Tutorial", True (255, 255, 255)), (self.tutorial_button.x + 30, self.tutorial_button.y +5))
        