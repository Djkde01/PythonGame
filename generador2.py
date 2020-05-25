import pygame
import random
from constantes import *
from generador import Generador

class Generador2(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(NARANJA)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.temp = 2

    def update(self):
        self.temp -= 1
