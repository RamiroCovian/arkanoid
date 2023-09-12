import os
from pygame.sprite import Sprite
from pygame import image
from . import ANCHO, ALTO


class Raqueta(Sprite):
    """
    1. Debe ser de tipo Sprite (herencia)
    2. Se tiene que poder mover (metodo)
    3. Pintarse (metodo)
    4. Volver a la posicion inicial (metodo)
    """

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            path_paleta = os.path.join("resources", "images", f"electric0{i}.png")
            self.imagenes.append(image.load(path_paleta))

        margen_y = 25
        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(midbottom=((ANCHO / 2), (ALTO - margen_y)))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]
