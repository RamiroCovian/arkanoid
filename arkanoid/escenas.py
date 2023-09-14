import os
import pygame as pg
from . import ANCHO, ALTO, FPS, LOGO_PATH
from .entidades import Ladrillo, Raqueta, Pelota


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):  # deberia ser un verbo por ser un metodo
        """
        Este metodo debe ser implementado por todas y cada una de las escenas,
        en funcion de lo que esten esperando hasta la condicion de salida.
        """
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        # windows: resources\images\arkanoid_name.png
        # mac/linux: resources/images/arkanoid_name.png
        # ruta = os.path.join("resources", "images", "arkanoid_name.png")
        self.logo = pg.image.load(LOGO_PATH)

        ruta = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(ruta, 35)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            self.pintar_mensaje()
            pg.display.flip()
        return False

    def pintar_mensaje(self):
        mensaje = "Pulsa <ESPACIO> para comenzar la partida"
        texto = self.tipografia.render(mensaje, True, (255, 255, 255))
        pos_x = (ANCHO - texto.get_width()) / 2
        pos_y = ALTO * 3 / 4
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO - ancho) / 2
        pos_y = (ALTO - alto) / 2
        self.pantalla.blit(self.logo, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        path_fondo = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(path_fondo)
        self.jugador = Raqueta()
        self.pelota = Pelota()
        self.muro = []

    def bucle_principal(self):
        super().bucle_principal()
        print(f"Tengo {len(self.muro)} ladrillos (1)")
        self.crear_muro()
        salir = False
        print(f"Tengo {len(self.muro)} ladrillos (2)")
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            self.pintar_fondo()
            self.jugador.update()
            self.pelota.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)
            hay_punto = self.pelota.comprobar_descontar_punto()  # Devuelve 0, 1
            if hay_punto > 0:
                # Debe descontar de Vidas en Marcador
                print("Pierde vida")
                return True

            pg.display.flip()

    def pintar_fondo(self):
        # TODO: mejorar la logica para "rellenar" el fondo.
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (600, 0))
        self.pantalla.blit(self.fondo, (0, 800))
        self.pantalla.blit(self.fondo, (600, 800))

    def crear_muro(self):
        filas = 4
        columnas = 6

        contador = 1
        for fila in range(filas):  # 0-3
            for col in range(columnas):
                # Por aqui voy a pasar filas*columnas=24
                ladrillo = Ladrillo()
                self.muro.append(ladrillo)
                print(contador, ladrillo)


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()
