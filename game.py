import pygame, constants

from player import Player
from event import Event

class Game():
    def __init__(self): 
        self.player = None
        self.event = Event()

    def set_player(self, character_name, character_image_path):
        self.player = Player(character_name, character_image_path)

    def update(self):
        self.event.time_to_choose()

    def draw(self, screen):
       screen.fill(constants.COLOR_WHITE)
       self.player.draw(screen)
       self.event.draw(screen)
       

    


   

