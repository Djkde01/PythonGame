import pygame
import random
from constantes import *
from jugador import Jugador
from enemigo1 import Enemigo1
from enemigo2 import Enemigo2
from sprites import *

class Creacion(pygame.sprite.Sprite):
    def __init__(self,pared,muros,booster,el1,el2,gen,lava,vidaBarra,totem):
        #Creacion de paredes
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
        #Creacion de muros
        for i in range(7):
            m = Muro([(30*i)-750,460])
            muros.add(m)
        for i in range(9):
            m = Muro([-266,(i*30)+50])
            muros.add(m)
        for i in range(8):
            m = Muro([(i*30)-266,290])
            muros.add(m)
        for i in range(6):
            m = Muro([-130,(i*30)+570])
            muros.add(m)
        for i in range(13):
            m = Muro([(i*30)-100,570])
            muros.add(m)
        for i in range(6):
            m = Muro([260,(i*30)+390])
            muros.add(m)
        m = Muro([360,720])
        muros.add(m)
        m = Muro([430,720])
        muros.add(m)

        #Creacion de generadores
        g1=Generador([-750,430])
        gen.add(g1)
        g2 = Generador([-100,720])
        gen.add(g2)
        g3 = Generador([-400,720])
        gen.add(g3)

        #Creacion de suelo de Lava
        cont = 0
        for i in range(5):
            l = Lava([(-434)+cont,(i*30)+50])
            lava.add(l)
            cont+=15
        for i in range(3):
            l = Lava([-374,(i*30)+200])
            lava.add(l)
        cont = 0
        for i in range(4):
            l = Lava([(-390)+cont,(i*30)+290])
            lava.add(l)
            cont -= 15
        cont = 0
        for i in range(2):
            l = Lava([(-530)+cont,(i*30)+400])
            lava.add(l)
            cont -= 10
        cont = 0
        for i in range(3):
            l = Lava([(-590)+cont,(i*30)+310])
            lava.add(l)
            cont += 30
        cont = 0
        for i in range(6):
            l = Lava([(-740)+cont,(i*30)+130])
            lava.add(l)
            cont += 10
        l = Lava([-30,290])
        lava.add(l)
        for i in range(3):
            l = Lava([27,(i*30)+50])
            lava.add(l)
        for i in range(3):
            l = Lava([42,(i*30)+140])
            lava.add(l)
        for i in range(9):
            l = Lava([325+cont,(i*30)+120])
            lava.add(l)
            cont -= 15
        cont = 0
        for i in range(2):
            l = Lava([264,(i*30)+50])
            lava.add(l)
        for i in range(6):
            l = Lava([249+cont,(i*30)+110])
            lava.add(l)
            cont -=15
        l = Lava([150,280])
        lava.add(l)
        #Creacion de gemas(elementos)
        t = Elem1([-580,430])
        totem.add(t)
        t2 = Elem2([1520,720])
        totem.add(t2)
        #Creacion de Vidas
        v = Vida([234,50])
        vidaBarra.add(v)

        #Creacion de boosters(velocidad)
        b = Boost([1520,680])
        booster.add(b)

        #Creacion de totem vida
        t = Totem([1500,50])
        totem.add(t)


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
    lim_der = 710
    lim_izq = 50
    f_lim_izq = 0
    f_lim_der = ANCHO - f_info[2]

    #Grupos
    #Jugador
    jugadores = pygame.sprite.Group()
    #Rivales base
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    #Balas generadas por el jugador
    balas = pygame.sprite.Group()
    #Limite mapa
    pared = pygame.sprite.Group()
    #Muros
    muros = pygame.sprite.Group()
    #Incremento de velocidad
    booster = pygame.sprite.Group()
    #Elementos, gemas, que debe recoger el jugador
    el1 = pygame.sprite.Group()
    el2 = pygame.sprite.Group()
    #Generador de enemigos
    gen = pygame.sprite.Group()
    #Suelo de lava
    lava = pygame.sprite.Group()
    #Corazon, una vida mas al jugador
    vidaBarra = pygame.sprite.Group()
    #Resurreccion
    totem = pygame.sprite.Group()
    #Enemigos creados a partir del generador
    enemy = pygame.sprite.Group()

    #Llamado a clase para crear todos los sprites
    Creacion(pared,muros,booster,el1,el2,gen,lava,vidaBarra,totem)

    #Creacion personaje principal
    cosa=Jugador([390,690])
    jugadores.add(cosa)
    cosa.bloques = muros
    cosa.pared = pared

    #Creacion de enemigo tipo 1
    #x1 = random.randrange(ANCHO-150)
    #y1 = random.randrange((ALTO-150))
    r1=Enemigo1([400,400])
    rivales1.add(r1)
    r1.bloques = muros
    r1.pared = pared

    #Creacion de enemigo tipo 2
    #x2 = random.randrange(ANCHO-150)
    #y2 = random.randrange((ALTO-150))
    r2=Enemigo2([500,400])
    rivales2.add(r2)
    r2.bloques = muros
    r2.pared = pared

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
        #creacion enemigos
        for g in gen:
            if g.temp < 0:
                direccion = random.randrange(500)
                r = Generados(g.rect.center)
                if direccion < 125:
                    r.velx = 5
                elif direccion < 250:
                    r.velx = -5
                elif direccion < 375:
                    r.vely = 5
                elif direccion < 500:
                    r.vely = -5
                enemy.add(r)
                g.temp = random.randrange(50)

        #control de los enemigos
        for r1 in rivales1:
            r1.rebotar()

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
        for g in gen:
            g.f_velxs = f_velx
        for l in lava:
            l.f_velxs = f_velx
        for t in totem:
            t.f_velxs = f_velx
        for v in vidaBarra:
            v.f_velxs = f_velx
        for r1 in rivales1:
            r1.f_velxs = f_velx
        for r2 in rivales2:
            r2.f_velxs = f_velx
        for en in enemy:
            en.f_velxs = f_velx

        #Limpieza de memoria balas
        for b in balas:
            #Deteccion de colision entre bala y enemigo
            disp = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            choq_mur = pygame.sprite.spritecollide(b,muros,False)
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
            for m in choq_mur:
                balas.remove(b)

        #Limpieza enemigos creados en generadores, se eliminan al chocar con un muro
        for r in enemy:
            mur = pygame.sprite.spritecollide(r,muros,False)
            pare = pygame.sprite.spritecollide(r,pared,False)
            for m in mur:
                enemy.remove(r)
            for f in pare:
                enemy.remove(r)

        #Colision entre enemigo y jugador
        impacto = False
        col = pygame.sprite.spritecollide(r1,jugadores,False)
        col2 = pygame.sprite.spritecollide(r2,jugadores,False)
        if col:
            impacto = True
            cosa.velx *= -1
            cosa.vely *= -1
            cosa.vidas -= 1
            print ("Vidas: ", cosa.vidas)
            print ("impacto: ",impacto)
            vidas = "Vidas: " + str(cosa.vidas)
        if col2:
            impacto = True
            cosa.velx *= -1
            cosa.vely *= -1
            cosa.vidas -= 3
            print ("Vidas: ", cosa.vidas)
            print ("impacto: ",impacto)
            vidas = "Vidas: " + str(cosa.vidas)

        impacto = False

        #modificadores
        '''sal = pygame.sprite.spritecollide(s,jugadores,False)
        vel = pygame.sprite.spritecollide(v,jugadores,False)
        if sal:
            cosa.inventario[1] = 1
            health.remove(s)
        if vel:
            cosa.inventario[2] = 1
            speed.remove(v)
            cosa.mayo_rakuin()'''

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
        #Update de objetos
        jugadores.update()
        rivales1.update()
        balas.update()
        rivales2.update()
        pared.update()
        muros.update()
        gen.update()
        enemy.update()
        vidaBarra.update()
        totem.update()
        lava.update()
        el1.update()
        el2.update()
        booster.update()
        #Ubicacion mapa
        ventana.blit(fondo,[f_posx,0])
        #Dibujo de objetos
        jugadores.draw(ventana)
        balas.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        enemy.draw(ventana)
        muros.draw(ventana)
        vidaBarra.draw(ventana)
        booster.draw(ventana)
        totem.draw(ventana)
        el1.draw(ventana)
        el2.draw(ventana)
        gen.draw(ventana)
        lava.draw(ventana)
        pared.draw(ventana)
        vidaBarra.draw(ventana)
        #Mensaje vidas jugador
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
