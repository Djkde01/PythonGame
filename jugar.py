import pygame
import random
from constantes import *
from jugador import Jugador
from enemigo1 import Enemigo1
from enemigo2 import Enemigo2
from sprites import *

class Creacion(pygame.sprite.Sprite):
    def __init__(self,pared,muros,booster,el1,el2,genera,lava,vidaBarra,totems):
        for i in range (16):
            p = Pared([-800,i*50])
            p2 = Pared([1550,i*50])
            pared.add(p)
            pared.add(p2)
        for j in range (32):
            p3 = Pared([j*50,0])
            p4 = Pared([j*50,750])
            pared.add(p3)
            pared.add(p4)
        for j in range(16):
            p5 = Pared([-j*50,0])
            p6 = Pared([-j*50,750])
            pared.add(p5)
            pared.add(p6)
        m = Muro([-270,50])
        muros.add(m)

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

    #Carga de mapa
    fondo = pygame.image.load("mapavacio.jpg")
    f_info = fondo.get_rect()
    f_velx = 0
    f_posx = -800
    lim_der = 720
    lim_izq = 50
    f_lim_izq = 0
    f_lim_der = ANCHO - f_info[2]

    #Grupos
    jugadores = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    pared = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    booster = pygame.sprite.Group()
    el1 = pygame.sprite.Group()
    el2 = pygame.sprite.Group()
    genera = pygame.sprite.Group()
    lava = pygame.sprite.Group()
    vidaBarra = pygame.sprite.Group()
    totems = pygame.sprite.Group()

    #Llamado a clase para crear todos los sprites
    Creacion(pared,muros,booster,el1,el2,genera,lava,vidaBarra,totems)

    #Creacion personaje principal
    cosa=Jugador([300,200])
    jugadores.add(cosa)
    cosa.bloques = muros
    cosa.pared = pared

    #Creacion de enemigo tipo 1
    x1 = random.randrange(ANCHO-150)
    y1 = random.randrange((ALTO-150))
    r1=Enemigo1([x1,y1])
    rivales1.add(r1)

    '''n=4
    for a in range(n):
        x = random.randrange(ANCHO-150)
        y = random.randrange((ALTO-150))
        r1 = Enemigo1([x,y])
        rivales1.add(r1)'''

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
            if event.type == pygame.KEYUP:
                cosa.velx = 0
                cosa.vely = 0
                cosa.estado = 1
        #cosa.bordes()

        #Control movimiento jugador con mapa
        if cosa.rect.x > lim_der:
            cosa.rect.x = lim_der
            if f_posx > f_lim_der:
                f_velx = -5
            else:
                f_velx = 0

        elif cosa.rect.x < lim_izq:
            cosa.rect.x = lim_izq
            if f_posx < f_lim_izq:
                f_velx = 5
            else:
                f_velx = 0
        else:
            f_velx =  0

        #Control movimiento objetos junto con mapa
        for p in pared:
            p.f_velxs = f_velx
        for m in muros:
            m.f_velxs = f_velx
        for b in booster:
            b.f_velxs = f_velx
        for e in el1:
            e.f_velxs = f_velx
        for h in el2:
            h.f_velxs = f_velx
        for g in genera:
            g.f_velxs = f_velx
        for l in lava:
            l.f_velxs = f_velx
        for t in totems:
            t.f_velxs = f_velx

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
        impacto = False
        col = pygame.sprite.spritecollide(r1,jugadores,False)
        col2 = pygame.sprite.spritecollide(r2,jugadores,False)
        if col:
            impacto = True
            cosa.velx *= -1
            cosa.vely *= -1
            cosa.vidas -= 1
            print ("Vidas: ", cosa.vidas)
            vidas = "Vidas: " + str(cosa.vidas)
        if col2:
            impacto = True
            cosa.velx *= -1
            cosa.vely *= -1
            cosa.vidas -= 1
            print ("Vidas: ", cosa.vidas)
            vidas = "Vidas: " + str(cosa.vidas)

        impacto = False


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
        pared.update()
        muros.update()
        #ventana.fill(NEGRO)
        ventana.blit(fondo,[f_posx,0])
        jugadores.draw(ventana)
        balas.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        pared.draw(ventana)
        muros.draw(ventana)
        booster.draw(ventana)
        el1.draw(ventana)
        el2.draw(ventana)
        genera.draw(ventana)
        lava.draw(ventana)
        vidaBarra.draw(ventana)
        totems.draw(ventana)
        info_vidas = info.render(vidas,True,BLANCO)
        ventana.blit(info_vidas,[10,10])

        pygame.display.flip()
        reloj.tick(40)

        #Movimiento del fondo
        f_posx += f_velx

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
