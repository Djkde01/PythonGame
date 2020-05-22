import pygame
import random
from constantes import *
from enemigo import *

class Enemigo1(Enemigo):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "rival1"
        self.velx = 0
        self.vely = 0
        self.vidas = 3
        self.damage = 1
        self.estado = 1 # 1 estándar, 2 rondando, 3 muerto

    def RetPos(self):
        x = self.rect.x + 20
        y = self.rect.bottom
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        self.estado=1

    def morir(self):
        if self.vidas <= 0:
            self.detener()
            self.estado = 3

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

    def mover(self):
        self.velx = random.randrange(-5,6)
        self.estado = 2

    #si llega hasta alguno de los bordes cambiará la dirección en la que iba hacia el lado contrario
    def rebotar(self):
        if self.rect.right >= ANCHO:
                self.velx *= -1
        if self.rect.left <= 0:
                self.velx *= -1
        if self.rect.top <= 0:
                self.vely *= -1
        if self.rect.bottom >= ALTO:
                self.vely *= -1
