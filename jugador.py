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
        self.dir = 0 #0:arriba, 1:derecha, 2:abajo, 3:izquierda
        self.velx = 0
        self.vely = 0
        self.vidas = 5
        self.estado = 1 #1 estándar, 2 velocidad, 3 totem, 4 disparo, 5 con los 2 objetos, 6 en llamas, 7 muerto
        self.llamas = 0
        self.inventario = [0,0,0] #objetos, tótem, buff
        self.mover(0,0)


    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

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

    #Control ; cuando llega a los extremos no permite que pase de los límites y solo se mueve cuando se dirija hacia otra dirección
    '''def bordes(self):
        if (self.rect.right >= ANCHO) and (self.velx > 0):
                self.detener()
        if (self.rect.left <= 0) and (self.velx < 0):
                self.detener()
        if (self.rect.top <= 0) and (self.vely < 0):
                self.detener()
        if (self.rect.bottom >= ALTO) and (self.vely > 0):
                self.detener()'''

    #cuando recoge el buff activa el estado de velocidad
    def mayo_rakuin(self):
         if self.inventario[2] > 0:
             self.estado = 2
             #self.velx *= 2
             #self.vely *= 2

    #cuando tiene ambos objetos pasa al estado 5 (en el que puede ganar?)
    def objetos(self):
        if self.inventario[0] == 2:
            self.estado = 5

    # Muerte ; cuando las vidas llegan a 0
    def morir(self):
         if self.vidas <= 0:
             #verifica si tiene un totem, si es así le suma 3 vidas y le quita el totem del inventario
            if self.inventario[1] == 1:
                self.estado = 3
                self.vidas = 3
                self.inventario[1] = 0
                #self.estado = 1
            #si no se muere :p
            else:
                self.detener()
                self.estado = 7

    #Si está quemandose la velocidad se reduce
    def quemado(self):
        if self.llamas == 1:
            self.estado = 6
            self.velx -= 3 #sería conveniente que esto esté en el código del juego
            self.vely -= 3 #y se dé cuando el estado pase a 6
