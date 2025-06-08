import pygame, ui, constants

class Menu():
    def __init__ (self, game_manager_instance):
        self.game_manager = game_manager_instance
        self._game_started = False
        self._game_quit = False
        self.running = True
    
    def reset(self):
        self._game_started = False
        self._game_quit = False


    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ui.start_button.collidepoint(event.pos):
                self._game_started = True

            if ui.exit_button.collidepoint(event.pos):
                self._game_quit = True

    def draw(self, screen): 
        screen.blit(ui.img_transform_bg, (0,0))
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.start_button)
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.options_button)
        pygame.draw.rect(screen, constants.COLOR_WHITE, ui.exit_button)

        screen.blit(ui.title_menu, (constants.TITLE_MENU_WIDTH, constants.TITLE_MENU_HEIGHT))
        screen.blit(ui.text_start_button, (ui.start_button.x + 32, ui.start_button.y + 10))
        screen.blit(ui.text_options_button, (ui.options_button.x + 2, ui.options_button.y +10 ))
        screen.blit(ui.text_exit_button, (ui.exit_button.x + 35, ui.exit_button.y + 10))


    def is_game_started(self):
        return self._game_started

    def is_game_quit(self):
        return self._game_quit
    
