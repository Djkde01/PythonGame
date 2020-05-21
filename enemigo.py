import pygame

class Enemigo(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.type = type
        self.vidas = vidas
        self.damage = damage
        self.estado = estado

   def update(self):
        self.rect.x = self.rect.x + self.velx*self.direccion
        self.rect.y = self.rect.y + self.vely
