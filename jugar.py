import pygame
import random
import time
from constantes import *
from jugador import Jugador
from enemigo1 import Enemigo1
from enemigo2 import Enemigo2
from sprites import *

class Creacion(pygame.sprite.Sprite):
    def __init__(self,pared,muros,booster,el1,el2,gen,lava,vidaBarra,totem,monument):
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
        for i in range(8):
            m = Muro([1460,(i*30)+510])
            muros.add(m)
        for i in range(3):
            m = Muro([(i*30)+1390,510])
            muros.add(m)
        for i in range(3):
            m = Muro([1360,(i*30)+510])
            muros.add(m)
        for i in range(5):
            m = Muro([1480,(i*30)+250])
            muros.add(m)
        for i in range(32):
            m = Muro([(i*30)+600,115])
            muros.add(m)
        for i in range(20):
            m = Muro([521,(i*30)+150])
            muros.add(m)
        for i in range(26):
            m = Muro([(i*30)+551,210])
            muros.add(m)
        for i in range(7):
            m = Muro([600,(i*30)+240])
            muros.add(m)
        for i in range(4):
            m = Muro([(i*30)+630,360])
            muros.add(m)
        for i in range(1):
            m = Muro([1300,240])
            muros.add(m)
        for i in range(5):
            m = Muro([1410,(i*30)+140])
            muros.add(m)
        for i in range(9):
            m = Muro([(i*30)+1280,390])
            muros.add(m)
        for i in range(10):
            m = Muro([1270,(i*30)+390])
            muros.add(m)
        for i in range(18):
            m = Muro([(i*30)+605,638])
            muros.add(m)
        for i in range(8):
            m = Muro([(i*30)+1030,540])
            muros.add(m)
        for i in range(11):
            m = Muro([(i*30)+940,450])
            muros.add(m)
        for i in range(4):
            m = Muro([940,(i*30)+450])
            muros.add(m)
        for i in range(3):
            m = Muro([940,(i*30)+450])
            muros.add(m)
        for i in range(11):
            m = Muro([(i*30)+615,540])
            muros.add(m)
        for i in range(8):
            m = Muro([830,(i*30)+300])
            muros.add(m)
        for i in range(4):
            m = Muro([1093,(i*30)+335])
            muros.add(m)
        for i in range(5):
            m = Muro([(i*30)+943,335])
            muros.add(m)
        #Creacion de generadores
        g1=Generador([-750,430])
        gen.add(g1)
        g2 = Generador([-100,720])
        gen.add(g2)
        g3 = Generador([-400,720])
        gen.add(g3)
        g4 = Generador([1240,500])
        gen.add(g4)
        g5 = Generador([905,510])
        gen.add(g5)
        g6 = Generador([1040,720])
        gen.add(g6)
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
        e = Elem1([-580,430])
        el2.add(e)
        e2 = Elem2([1520,720])
        el2.add(e2)
        #Creacion de Vidas
        v = Vida([234,50])
        vidaBarra.add(v)
        v = Vida([1520,345])
        vidaBarra.add(v)
        #Creacion de boosters(velocidad)
        b = Boost([1520,680])
        booster.add(b)
        b2 = Boost([551,240])
        booster.add(b2)
        b3 = Boost([1023,400])
        booster.add(b3)
        #Creacion de totem vida
        t = Totem([1500,50])
        totem.add(t)
        #Creacion de Monumento
        mon = Monumento([400,720])
        monument.add(mon)

if __name__ == '__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    disparo = pygame.mixer.Sound("shooting2.wav")
    win = pygame.mixer.Sound("WinMenu.wav")
    level = pygame.mixer.Sound("Level.wav")
    death = pygame.mixer.Sound("DeathMenu.wav")
    start = pygame.mixer.Sound("MainMenu.wav")
    pygame.mixer.music.load

    #SECCION PREVIA, INICIO
    pygame.font.init()
    img_inicio = pygame.image.load("Inicio.jpeg")
    fin = False
    previo = False

    while (not fin) and (not previo):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                previo = True

        ventana.blit(img_inicio,[0,0])
        start.play()
        pygame.display.flip()

    #SECCION DE CONFIGURACION DE NIVEL

    #Carga de mapa
    fondo = pygame.image.load("Map.jpg")
    start.stop()
    level.play()
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
    #Monumento jugador
    monument = pygame.sprite.Group()

    #Llamado a clase para crear todos los sprites
    Creacion(pared,muros,booster,el1,el2,gen,lava,vidaBarra,totem,monument)

    #Creacion personaje principal
    player_spr = pygame.image.load("SpritesPlayer.png")

    m = []
    for f in range(8):
        fila=[]
        for c in range(8):
            cuadro = player_spr.subsurface(40*c,60*f,40,60)
            fila.append(cuadro)
        m.append(fila)

    cosa=Jugador([390,690],m)
    jugadores.add(cosa)
    cosa.bloques = muros
    cosa.pared = pared

    #Creacion de enemigo tipo 1
    en1_spr = pygame.image.load("SpritesEnemy1.png")
    n = []
    for f1 in range(4):
        fila1=[]
        for c1 in range(6):
            cuadro1 = en1_spr.subsurface(90*c1,60*f1,90,60)
            fila1.append(cuadro1)
        n.append(fila1)
    r1=Enemigo1([-400,350],n)
    rivales1.add(r1)
    r1.bloques = muros
    r1.pared = pared

    #Creacion de enemigo tipo 2
    en2_spr = pygame.image.load("SpritesEnemy2.png")
    o = []
    for f2 in range(4):
        fila2=[]
        for c2 in range(4):
            cuadro2 = en2_spr.subsurface(90*c2,60*f2,90,60)
            fila2.append(cuadro2)
        o.append(fila2)
    r2=Enemigo2([-500,400],o)
    rivales2.add(r2)
    r2.bloques = muros
    r2.pared = pared

    #Texto control vidas jugador
    info = pygame.font.Font(None,30)
    vidas = "Vidas: " + str(cosa.vidas)
    info_vidas = info.render(vidas,True,BLANCO)

    #Timer del juego
    cont = 0
    reloj = pygame.time.Clock()
    fin_juego = False
    tiempo = 0
    info_t = pygame.font.Font(None,30)
    restante = "Tiempo: " + str(tiempo)
    info_restante = info.render(restante,True,BLANCO)
    #Tiempo en segundos
    p = 120.00
    alarm = time.time() + p

    #movimiento de los enemigos
    for r in rivales1:
        r.mover()

    for r2 in rivales2:
        r2.mover()

    #Ciclo principal de juego
    while (not fin) and (not fin_juego):
        #Control de Tiempo
        n = time.time()
        if n < alarm:
            tiempo = (round(alarm-n))
            restante = "Tiempo: " + str(tiempo)
            info_restante = info.render(restante,True,BLANCO)
        else:
            fin_juego = True
            victoria = False

        for g in gen:
            if g.temp < 0:
                direccion = random.randrange(500)
                r = Generados(g.rect.center)
                if direccion < 125:
                    r.velx = 5
                    r.accion = 2
                elif direccion < 250:
                    r.velx = -5
                    r.accion = 1
                elif direccion < 375:
                    r.vely = 5
                    r.accion = 3
                elif direccion < 500:
                    r.vely = -5
                    r.accion = 0
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
                    if cosa.estado == 1:
                        cosa.mover(7,0)
                    if cosa.estado == 2:
                        cosa.mover(10,0)
                    if cosa.estado == 6:
                        cosa.mover(4,0)
                    cosa.dir = 1
                    cosa.accion = 1
                if event.key == pygame.K_LEFT:
                    if cosa.estado == 1:
                        cosa.mover(-7,0)
                    if cosa.estado == 2:
                        cosa.mover(-10,0)
                    if cosa.estado == 6:
                        cosa.mover(-4,0)
                    cosa.dir = 3
                    cosa.accion = 0
                if event.key == pygame.K_UP:
                    if cosa.estado == 1:
                        cosa.mover(0,-7)
                    if cosa.estado == 2:
                        cosa.mover(0,-10)
                    if cosa.estado == 6:
                        cosa.mover(0,-4)
                    cosa.dir = 0
                    cosa.accion = 4
                if event.key == pygame.K_DOWN:
                    if cosa.estado == 1:
                        cosa.mover(0,7)
                    if cosa.estado == 2:
                        cosa.mover(0,10)
                    if cosa.estado == 6:
                        cosa.mover(0,4)
                    cosa.dir = 2
                    cosa.accion = 5
                if event.key == pygame.K_s:
                    disparo.play()
                    #Estado de disparo y creacion de bala
                    cosa.estado = 4
                    pos = cosa.RetPos()
                    b = Bala(pos)
                    if cosa.dir == 0:
                        b.velx = 0
                        b.vely = -5
                        cosa.accion = 6
                    if cosa.dir == 1:
                        b.velx = 5
                        b.vely = 0
                        cosa.accion = 3
                    if cosa.dir == 2:
                        b.velx = 0
                        b.vely = 5
                        cosa.accion = 7
                    if cosa.dir == 3:
                        b.velx = -5
                        b.vely = 0
                        cosa.accion = 2
                    balas.add(b)
            if event.type == pygame.KEYUP:
                cosa.velx = 0
                cosa.vely = 0
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
        for mo in monument:
            mo.f_velxs = f_velx
        for ba in balas:
            ba.f_velxs = f_velx


        #Limpieza de memoria balas
        for b in balas:
            #Deteccion de colision entre bala y enemigo
            disp = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            disp3 = pygame.sprite.spritecollide(b,enemy,False)
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
            #Eliminacion de bala al hacer colision con un enemigo y se reduce la vida de este
            for r1 in disp:
                r1.vidas -= 1
                print("Enemy 1:",r1.vidas)
                balas.remove(b)
            for r2 in disp2:
                r2.vidas -= 1
                print("Enemy 2:",r2.vidas)
                balas.remove(b)
            for r in disp3:
                r.vidas -= 1
                balas.remove(b)
            if choq_mur:
                balas.remove(b)

        for m in enemy:
            en = pygame.sprite.spritecollide(m,jugadores,False)
            if en:
                cosa.vidas -= m.damage
                cosa.estado = 1
                vidas = "Vidas: " + str(cosa.vidas)
                m.vidas = 0

        #Si el rival perdio toda su vida, es eliminado
        for r in enemy:
            if r.vidas == 0:
                enemy.remove(r)
                r.damage = 0

        for r1 in rivales1:
            r1.morir()
            if r1.estado == 3:
                rivales1.remove(r1)
                r1.damage = 0
                print ("Rival 1 eliminado")

        for r2 in rivales2:
            r2.morir()
            if r2.estado == 3:
                rivales2.remove(r2)
                r2.damage = 0
                print ("Rival 2 eliminado")

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
            if r1.damage > 0:
                impacto = True
                cosa.velx *= -1
                cosa.vely *= -1
                cosa.vidas -= r1.damage
                cosa.estado = 1
                vidas = "Vidas: " + str(cosa.vidas)
        if col2:
            if r2.damage > 0:
                impacto = True
                cosa.velx *= -1
                cosa.vely *= -1
                cosa.vidas -= r2.damage
                cosa.estado = 1
                vidas = "Vidas: " + str(cosa.vidas)
        impacto = False

        #colision con los objetos
        #Colision con booster
        boo = pygame.sprite.spritecollide(cosa,booster,True)
        if boo:
            cosa.inventario[2] += 1
        cosa.mayo_rakuin()

        #Colision con gemas
        gem1 = pygame.sprite.spritecollide(cosa,el1,True)
        gem2 = pygame.sprite.spritecollide(cosa,el2,True)
        if gem1 or gem2:
            cosa.inventario[0] +=1

        #Colision con lava
        lav = pygame.sprite.spritecollide(cosa,lava,False)
        if lav:
            cosa.llamas = 1
        cosa.quemado()

        #Colision con vidas
        cor = pygame.sprite.spritecollide(cosa,vidaBarra,True)
        if cor:
            cosa.vidas += 1
            print("vidas =", cosa.vidas)
            vidas = "Vidas: " + str(cosa.vidas)

        #Colision con totem
        tot = pygame.sprite.spritecollide(cosa,totem,True)
        if tot:
            cosa.inventario[1] += 1
            print("totem", cosa.inventario[1])

        #Colision con Monumento
        monum = pygame.sprite.spritecollide(cosa,monument,False)
        if monum:
            if cosa.inventario[0]>=2:
                fin_juego = True
                victoria = True

        #fin del juego
        cosa.morir()
        vidas = "Vidas: " + str(cosa.vidas)
        if cosa.estado==7:
            jugadores.remove(cosa)
            fin_juego = True
            victoria = False

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
        monument.update()
        booster.update()
        #Ubicacion mapa
        ventana.blit(fondo,[f_posx,0])
        #Dibujo de objetos
        monument.draw(ventana)
        balas.draw(ventana)
        jugadores.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        muros.draw(ventana)
        enemy.draw(ventana)
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
        ventana.blit(info_vidas,[190,10])
        ventana.blit(info_restante,[10,10])

        pygame.display.flip()
        reloj.tick(20)

        #Movimiento del fondo
        f_posx += f_velx

    #SECCION FINAL, FIN DEL JUEGO POR PERDIDA
    img_fin_loose = pygame.image.load("Fin.jpeg")
    while (not fin) and (not victoria):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin  = True
            if event.type == pygame.KEYDOWN:
                fin = True

        ventana.blit(img_fin_loose,[0,0])
        level.stop()
        death.play()
        pygame.display.flip()

    #SECCION FINAL, FIN JUEGO CON TRIUNFO
    img_fin_win = pygame.image.load("Triunfo.jpg")
    while (not fin) and (victoria):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin  = True
            if event.type == pygame.KEYDOWN:
                fin = True

        ventana.blit(img_fin_win,[0,0])
        level.stop()
        win.play()
        pygame.display.flip()
