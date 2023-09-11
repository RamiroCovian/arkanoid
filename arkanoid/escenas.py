import pygame as pg


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):  # deberia ser un verbo por ser un metodo
        """
        Este metodo debe ser implementado por todas y cada una de las escenas,
        en funcion de lo que esten esperando hasta la condicion de salida.
        """
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            pg.display.flip()


class Partida(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
