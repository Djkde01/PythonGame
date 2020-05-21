import pygame
from constantes import *

class Jugador(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.vidas = 5
        self.estado = 1
        self.llamas = 0
        self.inventario = [0,0,0] #objetos, tótem, buff
        self.mover(0,0)


    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

    def mover(self,x,y):
        self.velx = 0
        self.vely = 0
        self.velx = x
        self.vely = y

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        #self.estado = ?

    def rebotar(self):
        if (self.rect.right >= ANCHO) and (self.velx > 0):
                self.velx = -5
        if (self.rect.left <= 0) and (self.velx < 0):
                self.velx = 5
        if (self.rect.top <= 0) and (self.vely < 0):
                self.vely = 5
        if (self.rect.bottom >= ALTO) and (self.vely > 0):
                self.vely = -5

    def mayo_rakuin(self):
         if self.inventario[3] > 0:
             self.velx *= 2
             self.vely *= 2
             self.estado = 2

    def objetos(self):
        if self.inventario[1] == 2:
            self.estado = 5

    def morir(self):
         if self.vidas <= 0:
            if self.inventario[2] > 0:
                self.estado = 3
                self.vidas = 2
                self.inventario[2] -= 1
            if self.inventario[2] <= 0:
                self.detener()
                self.estado = 7

    def quemado(self):
        if self.llamas == 1:
            self.estado = 6
