import pygame, ui, constants

class Menu():
    def __init__ (self):
        self._game_started = False
        self.running = True

    @property
    def game_started(self):
        return self._game_started
    
    def set_game_status(self, value):
        self._game_started = value
    
    def start_window(self, screen):
        screen.blit(ui.img_transform_bg, (0, 0))
        pygame.draw.rect(screen, constants.BG, ui.start_button)
        pygame.draw.rect(screen, constants.BG, ui.exit_button)

        screen.blit(ui.title, (constants.TITLE_MENU_WIDTH, constants.TITLE_MENU_HEIGHT))
        screen.blit(ui.text_start_button, (ui.start_button.x + 18, ui.start_button.y + 10))
        screen.blit(ui.text_exit_button, (ui.exit_button.x + 25, ui.exit_button.y + 10))

        pygame.display.update()

    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ui.start_button.collidepoint(event.pos):
                self._game_started = True
                self.running = False
            if ui.exit_button.collidepoint(event.pos):
                print("Salida de juego")
                self.running = False

    def draw(self, screen): 
        screen.blit(ui.img_transform_bg, (0,0))
        pygame.draw.rect(screen, constants.BG, ui.start_button)
        pygame.draw.rect(screen, constants.BG, ui.exit_button)
        screen.blit(ui.title, (constants.TITLE_MENU_WIDTH, constants.TITLE_MENU_HEIGHT))
        screen.blit(ui.text_start_button, (ui.start_button.x + 18, ui.start_button.y + 10))
        screen.blit(ui.text_exit_button, (ui.exit_button.x + 25, ui.exit_button.y + 10))


    def is_game_started(self):
        return self._game_started

    def is_menu_running(self):
        return self.running
