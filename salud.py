import pygame
from constantes import *

class Salud(pygame.sprite.Sprite):
    def __init__(self,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([50,50])
            self.image.fill(VERDE)
            self.rect = self.image.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]
            self.type = "salud"
