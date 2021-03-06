import pygame
import random
from constantes import *
from enemigo import *

class Enemigo2(Enemigo):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "rival2"
        self.velx = 0
        self.vely = 0
        self.f_velxs = 0
        self.vidas = 1
        self.damage = 3
        self.estado = 1 # 1 estándar, 2 rondando, 3 muerto
        self.bloques = None
        self.pared = None

    def RetPos(self):
        x = self.rect.x + 20
        y = self.rect.bottom
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        self.estado = 1

    def morir(self):
        if self.vidas <= 0:
            self.detener()
            self.estado = 3

    def camino(self):
        if self.vely <= 0:
            self.accion = 3
        else:
            self.accion = 2

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.rect.x += self.f_velxs
        self.camino()
        if self.con < 3:
            self.con += 1
        else:
            self.con = 0
            self.accion = self.accion
        self.image = self.animacion[self.accion][self.con]

    def mover(self):
        self.vely = 5
        self.estado = 2

    #si llega hasta alguno de los bordes cambiará la dirección en la que iba hacia el lado contrario
    def rebotar(self):
        self.rect.y += self.vely
        ls_col = pygame.sprite.spritecollide(self,self.bloques,False)
        ls_col2 = pygame.sprite.spritecollide(self,self.pared,False)
        if ls_col:
            self.vely *= -1

        if ls_col2:
            self.vely *= -1
