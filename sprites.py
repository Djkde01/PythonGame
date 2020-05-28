import pygame
from constantes import *
import random

#Elemento bala, quita vida a los enemigos
class Bala(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

   def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely

#Elemento pared, delimita el mapa de juego
class Pared(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("borde.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs

#Elemento booster, incrementa la velocidad
class Boost(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("boost.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs

#Elemento gema 2, se agrega al inventario del jugador al recoger
class Elem1(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gem1.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs

#Elemento gema 2, se agrega al inventario del jugador al recoger
class Elem2(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gem2.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs

#Elemento generador, crea enemigos
class Generador(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("genera.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.temp = random.randrange(50)

   def update(self):
       self.temp -= 1
       self.rect.x += self.f_velxs

#Elemento enemigos, se crean a partir de los generadores cada cierto tiempo
class Generados(pygame.sprite.Sprite):
    def __init__ (self,pos):
       pygame.sprite.Sprite.__init__(self)
       self.accion = 1
       self.vidas = 1
       self.con = 0
       #self.animacion = m
       #self.image = self.animacion[self.accion][self.con]
       self.image = pygame.Surface([10,10])
       self.image.fill(NEGRO)
       self.rect = self.image.get_rect()
       self.rect.x = pos[0]
       self.rect.y = pos[1]
       self.velx = 0
       self.vely = 0
       self.damage = 1
       self.f_velxs = 0

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely
        self.rect.x += self.f_velxs
        '''if self.velx != self.vely:
            if self.con < 3:
                self.con += 1
            else:
                self.con = 0
                self.accion = self.accion
            self.image = self.animacion[self.accion][self.con]'''


    def detener(self):
        self.velx=0
        self.vely=0


#Elemento lava,
class Lava(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("lava.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs

#Elemento muro, son las paredes del laberinto
class Muro(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("muro.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs


#Elemento monumento, alli se inicia y gana el JUEGO
class Monumento(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("muro.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs

#Elemento vida, le da un corazon de vida al jugador
class Vida(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("vida.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

   def update(self):
        self.rect.x += self.f_velxs

#Elemento totem, regenera vida al morir
class Totem(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("totem.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0

   def update(self):
        self.rect.x += self.f_velxs
