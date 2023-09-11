import pygame
from . import ANCHO, ALTO, COLOR_FONDO


class Arkanoid:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ALTO, ANCHO))
        self.reloj = pygame.time.Clock()
        self.title = pygame.display.set_caption("Arkanoid")

    def jugar(self):
        """
        Bucle principal
        """
        salir = False
        while not salir:
            # 1. Capturar los eventos
            for evento in pygame.event.get():
                if pygame.QUIT == evento.type:
                    salir = True
            # 2. Calcular estados de elementos y pintarlos
            self.pantalla.fill(COLOR_FONDO)
            # 3. Mostrar los cambios (pintados) y controlar el reloj
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    print("Arrancamos desde el archivo game.py")
    juego = Arkanoid()
    juego.jugar()
