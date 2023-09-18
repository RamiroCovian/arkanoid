import pygame as pg
from . import ANCHO, ALTO
from .escenas import MejoresJugadores, Partida, Portada


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.reloj = pg.time.Clock()
        self.title = pg.display.set_caption("Arkanoid")
        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        mejores_jugadores = MejoresJugadores(self.pantalla)
        self.escenas = [portada, partida, mejores_jugadores]

    def jugar(self):
        # FIXME: evitar que el programa se cierre despues de la pantalla de mejores jugadores
        for escena in self.escenas:
            he_acabado = escena.bucle_principal()
            if he_acabado:
                print("La escena me pide que acabe el juego")
                break
        print("He salido del bucle for de las escenas")

        pg.quit()


if __name__ == "__main__":
    print("Arrancamos desde el archivo game.py")
    juego = Arkanoid()
    juego.jugar()
