import pygame as pg
from . import ANCHO, ALTO, COLOR_FONDO


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ALTO, ANCHO))
        self.reloj = pg.time.Clock()
        self.title = pg.display.set_caption("Arkanoid")

    def jugar(self):
        """
        Bucle principal
        """
        salir = False
        while not salir:
            # 1. Capturar los eventos
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True
            # 2. Calcular estados de elementos y pintarlos
            self.pantalla.fill(COLOR_FONDO)
            # 3. Mostrar los cambios (pintados) y controlar el reloj
            pg.display.flip()

        pg.quit()


if __name__ == "__main__":
    print("Arrancamos desde el archivo game.py")
    juego = Arkanoid()
    juego.jugar()
