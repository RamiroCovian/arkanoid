import os
from random import randint
import pygame as pg
from pygame.sprite import Sprite
from pygame import image, key, K_LEFT, K_RIGHT
from . import ANCHO, ALTO, VEL_MAX, VEL_MIN_Y, VIDAS


class Raqueta(Sprite):
    """
    1. Debe ser de tipo Sprite (herencia)
    2. Se tiene que poder mover (metodo)
        2.1 Leer el teclado
        2.2 Limites de movimiento(no debe salir de la pantalla)
    3. Pintarse (metodo)
    4. Volver a la posicion inicial (metodo)
    5. Velocidad
    """

    margen_y = 25  # Atributo de clase
    velocidad = 15

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            path_paleta = os.path.join("resources", "images", f"electric0{i}.png")
            self.imagenes.append(image.load(path_paleta))

        self.contador = 0  # Atributo de objeto
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(midbottom=((ANCHO / 2), (ALTO - self.margen_y)))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]

        estado_teclas = key.get_pressed()
        if estado_teclas[K_LEFT]:
            self.rect.x -= self.velocidad
        if self.rect.left < 0:
            self.rect.left = 0
        if estado_teclas[K_RIGHT]:
            self.rect.x += self.velocidad
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO


class Pelota(Sprite):
    """
    - [x] 1. Debe ser de tipo Sprite
    2. Se debe mover (Metodo)
    - [x] 2.1. Debe rebotar con el jugador
        - [x] 2.2. Debe rebotar contra los laterales
        2.3. Debe rebotar contra ladrillos (Se debe realizar en escenas.py)
        2.4. Al tocar el borde inferior de la pantalla debe hacer perder una vida al jugador
            o finalizar partida (Se debe realizar en escenas.py)
    - [x] 3. Se debe pintar (Metodo)
    - [x] 4. Posicion inicial (encima de la Raqueta)
    - [x] 5. Velocidad
    """

    def __init__(self, raqueta):
        super().__init__()
        self.imagenes = []
        for i in range(1, 6):
            path_pelota = os.path.join("resources", "images", f"ball{i}.png")
            self.imagenes.append(image.load(path_pelota))
        self.contador_p = 0
        self.image = self.imagenes[self.contador_p]

        self.raqueta = raqueta
        self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        self.inicializar_velocidades()
        self.he_perdido = False

    def inicializar_velocidades(self):
        self.vel_x = randint(-VEL_MAX, VEL_MAX)
        self.vel_y = randint(-VEL_MAX, VEL_MIN_Y)

        # self.control_animacion = 1

    def update(self, se_mueve_la_pelota):
        if not se_mueve_la_pelota:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
            # return False, False
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x

            self.rect.y += self.vel_y
            if self.rect.top <= 0:
                self.vel_y = -self.vel_y

            if self.rect.top >= ALTO:
                self.inicializar_velocidades()
                self.he_perdido = True

            self.comprobar_rebote_pala()

        """
        # Animo pelota para los rebotes
        self.contador_p += self.control_animacion
        if self.contador_p == 4 or self.contador_p == 0:
        Otra alternativa
        if self.contador_p in (0, 4):
            self.control_animacion = -self.control_animacion
        """

    def comprobar_rebote_pala(self):
        if pg.sprite.collide_mask(self, self.raqueta):
            self.inicializar_velocidades()


class Ladrillo(Sprite):
    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2
    IMG_LADRILLO = ["greenTile.png", "redTile.png", "redTileBreak.png"]

    def __init__(self, puntos, color=VERDE):
        super().__init__()
        self.tipo = color
        self.imagenes = []
        for img in self.IMG_LADRILLO:
            ruta = os.path.join("resources", "images", img)
            self.imagenes.append(pg.image.load(ruta))
        self.image = self.imagenes[color]
        self.rect = self.image.get_rect()
        self.puntos = (color + 1) * 10

    def update(self, muro):
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
        else:
            muro.remove(self)
        self.image = self.imagenes[self.tipo]


class Marcador:
    pass


class ContadorVidas:
    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas < 0

    def pintar(self):
        pass
