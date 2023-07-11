import pygame
from auxiliar import Auxiliar
from constantes import *
from player import Player

class Coins:
    def __init__(self, xx, yy, width, height, type=1):
    
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("images/botin/green ({0}).png",1,4,flip=False,step=1,scale= 2,w=width,h=height)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = xx
        self.rect.y = yy
        self.collision_rect = pygame.Rect(self.rect)
        self.ground_collision_rect = pygame.Rect(self.rect)
        self.ground_collision_rect.height = GROUND_COLLIDE_H
        self.coins_list = []

    def lista_coins(self):
        coins_list = []  # Create an empty list to store coins
        coins_list.append(self)  # Add the current coin instance to the list
        return coins_list

    

    def update(self):
        pass
    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the coin image on the screen


