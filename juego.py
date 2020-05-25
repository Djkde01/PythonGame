import pygame
import random
from constantes import *
from jugador import Jugador
from enemigo1 import Enemigo1
from enemigo2 import Enemigo2
from bala import Bala
from velocidad import Velocidad
from salud import Salud

if __name__ == '__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ANCHO,ALTO])

    #SECCION PREVIA, INICIO
    pygame.font.init()
    fuente = pygame.font.Font(None,40)
    mensaje_inicio = fuente.render("El maravilloso juego", True, BLANCO)
    fin = False
    previo = False

    while (not fin) and (not previo):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                previo = True

        ventana.fill(NEGRO)
        ventana.blit(mensaje_inicio,[200,200])
        pygame.display.flip()

    #SECCION DE CONFIGURACION DE NIVEL
    #Grupos
    jugadores = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    speed = pygame.sprite.Group()
    health = pygame.sprite.Group()

    #Creacion personaje principal
    cosa=Jugador([300,200])
    jugadores.add(cosa)

    #Creacion de enemigo tipo 1
    x1 = random.randrange(ANCHO-150)
    y1 = random.randrange((ALTO-150))
    r1=Enemigo1([x1,y1])
    rivales1.add(r1)

    v = Velocidad([50,50])
    speed.add(v)

    s = Salud([600,600])
    health.add(s)


    #Creacion de enemigo tipo 2
    x2 = random.randrange(ANCHO-150)
    y2 = random.randrange((ALTO-150))
    r2=Enemigo2([x2,y2])
    rivales2.add(r2)

    #Texto control vidas jugador
    info = pygame.font.Font(None,30)
    vidas = "Vidas: " + str(cosa.vidas)
    info_vidas = info.render(vidas,True,BLANCO)

    cont = 0
    reloj = pygame.time.Clock()
    fin_juego = False

    #movimiento de los enemigos
    for r in rivales1:
        r.mover()

    for r2 in rivales2:
        r2.mover()

    #Ciclo principal de juego
    while (not fin) and (not fin_juego):
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
                    cosa.dir = 1
                if event.key == pygame.K_LEFT:
                    cosa.mover(-5,0)
                    cosa.estado = 1
                    cosa.dir = 3
                if event.key == pygame.K_UP:
                    cosa.mover(0,-5)
                    cosa.estado = 1
                    cosa.dir = 0
                if event.key == pygame.K_DOWN:
                    cosa.mover(0,5)
                    cosa.estado = 1
                    cosa.dir = 2
                if event.key == pygame.K_s:
                    #Estado de disparo y creacion de bala
                    cosa.estado = 4
                    pos = cosa.RetPos()
                    b = Bala(pos)
                    if cosa.dir == 0:
                        b.velx = 0
                        b.vely = -5
                    if cosa.dir == 1:
                        b.velx = 5
                        b.vely = 0
                    if cosa.dir == 2:
                        b.velx = 0
                        b.vely = 5
                    if cosa.dir == 3:
                        b.velx = -5
                        b.vely = 0
                    balas.add(b)
                #verifica si tiene modificador PERO solo funciona en el primer movimiento
                if cosa.estado == 2:
                    cosa.velx *= 2
                    cosa.vely *= 2
            if event.type == pygame.KEYUP:
                cosa.velx = 0
                cosa.vely = 0
                cosa.estado = 1
        #cosa.bordes()

        #Limpieza de memoria balas
        for b in balas:
            #Deteccion de colision entre bala y enemigo
            disp = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            #Eliminacion al salir de pantalla
            if b.rect.y < -50:
                balas.remove(b)
            if b.rect.y > 850:
                balas.remove(b)
            if b.rect.x < -50:
                balas.remove(b)
            if b.rect.x > 850:
                balas.remove(b)
            #Eliminacion al hacer colision con un enemigo y se reduce
            #la vida de ese enemigo
            for r in disp:
                balas.remove(b)
                r1.vidas -=1
                print("Enemy 1:",r1.vidas)
            for r2 in disp2:
                balas.remove(b)
                r2.vidas -=1
                print("Enemy 2:",r2.vidas)

        #Colision entre enemigo y jugador, REVISAR
        col = pygame.sprite.spritecollide(r1,jugadores,False)
        col2 = pygame.sprite.spritecollide(r2,jugadores,False)
        if col:
            cosa.vidas -= 1
            col = False
            vidas = "Vidas: " + str(cosa.vidas)
            print("Federico: ", cosa.vidas)
        if col2:
            cosa.vidas -= 1
            col2 = False
            vidas = "Vidas: " + str(cosa.vidas)
            print("Federico: ", cosa.vidas)

        #modificadores
        sal = pygame.sprite.spritecollide(s,jugadores,False)
        vel = pygame.sprite.spritecollide(v,jugadores,False)
        if sal:
            cosa.inventario[1] = 1
            health.remove(s)
        if vel:
            cosa.inventario[2] = 1
            speed.remove(v)
            cosa.mayo_rakuin()

        #fin del juego
        cosa.morir()
        if cosa.estado==7:
            jugadores.remove(cosa)
            fin_juego = True


        #Si el rival perdio toda su vida, es eliminado
        for r1 in rivales1:
            r1.morir()
            if r1.estado == 3:
                rivales1.remove(r1)

        for r2 in rivales2:
            r2.morir()
            if r2.estado == 3:
                rivales2.remove(r2)


        #Refresco
        jugadores.update()
        rivales1.update()
        balas.update()
        rivales2.update()
        ventana.fill(NEGRO)
        info_vidas = info.render(vidas,True,BLANCO)
        ventana.blit(info_vidas,[10,10])
        jugadores.draw(ventana)
        balas.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        speed.draw(ventana)
        health.draw(ventana)

        pygame.display.flip()
        reloj.tick(40)

    #SECCION FINAL, FIN DEL JUEGO
    fuente_f = pygame.font.Font(None,32)
    mensaje_fin = fuente_f.render("Que bobo, perdio", True, BLANCO)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin  = True

        ventana.fill(NEGRO)
        ventana.blit(mensaje_fin,[200,200])
        pygame.display.flip()
