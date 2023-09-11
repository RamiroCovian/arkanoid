import pygame as pg
from . import ANCHO, ALTO, COLOR_FONDO
from .escenas import MejoresJugadores, Partida, Portada


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ALTO, ANCHO))
        self.reloj = pg.time.Clock()
        self.title = pg.display.set_caption("Arkanoid")
        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        mejores_jugadores = MejoresJugadores(self.pantalla)
        self.escenas = [portada, partida, mejores_jugadores]

    def jugar(self):
        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()


if __name__ == "__main__":
    print("Arrancamos desde el archivo game.py")
    juego = Arkanoid()
    juego.jugar()
