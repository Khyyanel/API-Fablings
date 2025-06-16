import pygame, constants, errors

class Player():
    def __init__(self, name, image_path):
        self.name = name
        self.x = constants.PLAYER_X
        self.y = constants.PLAYER_Y
        self.width = constants.PLAYER_WIDTH
        self.height = constants.PLAYER_HEIGHT
        
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.shape = self.image.get_rect(center=(self.x, self.y)) 

        self.stadistics = {
             "pericia": 10, 
             "supervivencia": 10,
             "conocimiento": 10, 
             "suerte": 10, 
             "carisma": 10
        }

        self.items = []
        self.health = 100
      

    def draw(self, screen: pygame.Surface):
          screen.blit(self.image, (self.x, self.y))