import os
from random import randint
from pygame.sprite import Sprite
from pygame import image, key, K_LEFT, K_RIGHT
from . import ANCHO, ALTO


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

    vel_x = -10
    vel_y = -13

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

        self.vel_pelota = 5
        self.velocidad_y = 0
        while self.velocidad_y == 0:
            self.velocidad_y = randint(-self.vel_pelota, self.vel_pelota)
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-self.vel_pelota, self.vel_pelota)

        # self.control_animacion = 1

    def update(self, partida_empezada):
        if not partida_empezada:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

        # Animo pelota para los rebotes
        # self.contador_p += self.control_animacion
        # if self.contador_p == 4 or self.contador_p == 0:
        # Otra alternativa
        # if self.contador_p in (0, 4):
        #     self.control_animacion = -self.control_animacion

        self.image = self.imagenes[self.contador_p]
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        if self.rect.x <= 0:
            self.rect.x = 0
            self.velocidad_x = -self.velocidad_x
        if self.rect.x >= ANCHO - self.image.get_width():
            self.rect.x = ANCHO - self.image.get_width()
            self.velocidad_x = -self.velocidad_x

        # Lo establezco para contener la pelota en la pantalla, luego debo sacar
        if self.rect.y <= 0:  # En caso que rebote en un ladrillo (escenas.py)
            self.rect.y = 0
            self.velocidad_y = -self.velocidad_y

    def comprobar_descontar_punto(self):
        if self.rect.y >= ALTO - self.image.get_height():
            self.rect.y = ALTO - self.image.get_height()
            self.velocidad_x = 0
            self.velocidad_y = 0
            return 1  # Si toca parte inferior de la pantalla, devuelve 1 para descontar punto en marcador
        return 0


class Ladrillo(Sprite):
    def __init__(self):
        super().__init__()
        path_verde = os.path.join("resources", "images", "greenTile.png")
        self.image = image.load(path_verde)
        self.rect = self.image.get_rect()


class Marcador:
    pass
