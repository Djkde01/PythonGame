import pygame
import random
from constantes import *
from jugador import Jugador
from enemigo1 import Enemigo1
from enemigo2 import Enemigo2

if __name__ == '__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    #Grupos
    jugadores = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()

    cosa=Jugador([300,200])
    jugadores.add(cosa)

    n=6
    for i in range(n):
        x = random.randrange(ANCHO-150)
        y = random.randrange((ALTO-150))
        r = Enemigo1([x,y])
        rivales1.add(r)

    m=3
    for k in range(m):
        x = random.randrange(ANCHO-150)
        y = random.randrange((ALTO-150))
        r2 = Enemigo2([x,y])
        rivales2.add(r2)

    reloj = pygame.time.Clock()
    fin = False

    #movimiento de los enemigos
    for r in rivales1:
        r.mover()

    for r2 in rivales2:
        r2.mover()

    while not fin:
        #control de los enemigos
        for r in rivales1:
            r.rebotar()

        for r2 in rivales2:
            r2.rebotar()

        #movimiento y control del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cosa.mover(5,0)
                    cosa.estado = 1
                if event.key == pygame.K_LEFT:
                    cosa.mover(-5,0)
                    cosa.estado = 1
                if event.key == pygame.K_UP:
                    cosa.mover(0,-5)
                    cosa.estado = 1
                if event.key == pygame.K_DOWN:
                    cosa.mover(0,5)
                if event.key == pygame.K_s:
                    cosa.estado = 4
            if event.type == pygame.KEYUP:
                cosa.velx = 0
                cosa.vely = 0
                cosa.estado = 1
        cosa.bordes()

        #Colision ; debería ver si el jugador está atacando y solo bajarle vidas si no lo está pero it doesn't work :(
        choq = pygame.sprite.spritecollide(cosa,rivales1,True)
        for b in choq:
            if cosa.estado == 4:
                for r in rivales1:
                    r.vidas -= 1
            else:
                cosa.vidas -= 1

        choq2 = pygame.sprite.spritecollide(cosa,rivales2,True)
        for c in choq2:
            if cosa.estado == 4:
                for r in rivales1:
                    r2.vidas -= 1
            else:
                cosa.vidas -= 3
        #------

        #fin del juego
        cosa.morir()
        if cosa.estado==7:
            jugadores.remove(cosa)
            #ventana.fill(NEGRO)
            #pygame.font.init()
            #fuente = pygame.font.Font(None, 32)
            #msj = fuente.render("Fin de juego",True,BLANCO)
            #pygame.display.flip()
            fin = True
        #----

        #debería verificar si los enemigos están muertos y eliminarlos cuando lo estén but ya los eliminó entonces no c bro
        for r in rivales1:
            r.morir()
            if r.estado == 3:
                rivales1.remove(r)

        for r2 in rivales2:
            r2.morir()
            if r2.estado == 3:
                rivales2.remove(r2)
        #----

        #Refresco
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        jugadores.update()
        rivales1.update()
        rivales2.update()
        pygame.display.flip()
        reloj.tick(40)
