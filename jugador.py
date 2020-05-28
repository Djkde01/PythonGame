import pygame
from constantes import *

class Jugador(pygame.sprite.Sprite):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.lim = [7,7,2,2,7,7,2,2]
        self.dir = 0 #0:arriba, 1:derecha, 2:abajo, 3:izquierda
        self.velx = 0
        self.vely = 0
        self.vidas = 5
        self.estado = 1 #1 estándar, 2 velocidad, 3 totem, 4 disparo, 5 con los 2 objetos, 6 en llamas, 7 muerto
        self.llamas = 0
        self.bloques = None
        self.pared = None
        self.inventario = [0,0,0] #objetos, tótem, buff
        self.mover(0,0)

    def animar(self):
        if self.velx != self.vely:
            if self.con < self.lim[self.accion]:
                self.con += 1
            else:
                self.con = 0
                self.accion = self.accion
            self.image = self.animacion[self.accion][self.con]


    def update(self):
        #Colision en x
        self.rect.x += self.velx
        ls_col = pygame.sprite.spritecollide(self,self.bloques,False)
        ls_col2 = pygame.sprite.spritecollide(self,self.pared,False)
        for b in ls_col:
            if (self.rect.right > b.rect.left) and (self.velx > 0):
                self.rect.right = b.rect.left
                self.velx = 0
            elif (self.rect.left < b.rect.right) and (self.velx < 0):
                self.rect.left = b.rect.right
                self.velx = 0

        for m in ls_col2:
            if (self.rect.right > m.rect.left) and (self.velx > 0):
                self.rect.right = m.rect.left
                self.velx = 0
            elif (self.rect.left < m.rect.right) and (self.velx < 0):
                self.rect.left = m.rect.right
                self.velx = 0
        #Colision en y
        self.rect.y += self.vely
        ls_col = pygame.sprite.spritecollide(self,self.bloques,False)
        ls_col2 = pygame.sprite.spritecollide(self,self.pared,False)
        for b in ls_col:
            if (self.rect.top < b.rect.bottom) and (self.vely < 0):
                self.rect.top = b.rect.bottom
                self.vely = 0
            elif (self.rect.bottom > b.rect.top) and (self.vely > 0):
                self.rect.bottom = b.rect.top
                self.vely = 0

        for m in ls_col2:
            if (self.rect.top < m.rect.bottom) and (self.vely < 0):
                self.rect.top = m.rect.bottom
                self.vely = 0
            elif (self.rect.bottom > m.rect.top) and (self.vely > 0):
                self.rect.bottom = m.rect.top
                self.vely = 0

        self.animar()

    def mover(self,x,y):
        self.velx = x
        self.vely = y

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        self.estado = 1

    #cuando recoge el buff activa el estado de velocidad
    def mayo_rakuin(self):
         if self.inventario[2] > 0:
             self.llamas = 0
             self.estado = 2
             self.velx *= 1.05
             self.vely *= 1.05
             self.inventario[2] -= 1

    #cuando tiene ambos objetos pasa al estado 5 (en el que puede ganar?)
    def objetos(self):
        if self.inventario[0] == 2:
            self.estado = 5

    # Muerte ; cuando las vidas llegan a 0
    def morir(self):
         if self.vidas <= 0:
             #verifica si tiene un totem, si es así le suma 3 vidas y le quita el totem del inventario
            if self.inventario[1] > 0:
                self.vidas = 3
                self.inventario[1] -= 1
                #self.estado = 1
            #si no se muere :p
            else:
                self.detener()
                self.estado = 7

    #Si está quemandose la velocidad s---e reduce
    def quemado(self):
        if self.llamas == 1:
            self.estado = 6
            self.velx *= 0.9
            self.vely *= 0.9
