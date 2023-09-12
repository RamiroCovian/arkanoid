import os
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
        if estado_teclas[K_RIGHT]:
            self.rect.x += self.velocidad
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.left < 0:
            self.rect.left = 0


class Pelota:
    pass
