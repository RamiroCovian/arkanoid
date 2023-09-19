import csv
import os

MAX_RECORDS = 10


class Records:
    # (__file__) me va a dar la ruta del archivo en el que estoy (records.py)
    filename = "records.csv"
    file_dir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        self.game_records = []
        self.data_path = os.path.join(os.path.dirname(self.file_dir), "data")
        self.file_path = os.path.join(self.data_path, self.filename)
        self.check_records_file()

    def check_records_file(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
            print("No habia directorio para datos, pero lo he creado!!!")

        if not os.path.exists(self.file_path):
            self.reset()

    def insert_record(self, nombre, puntuacion):
        pass

    def puntuacion_menor(self):
        pass

    def guardar(self):
        # lector = open(self.file_path, mode= "w")
        # lector.close()
        with open(self.file_path, mode="w") as records_file:
            writer = csv.writer(records_file)
            writer.writerow(("Nombre", "Puntos"))
            writer.writerows(self.game_records)

    def cargar(self):
        pass

    def reset(self):
        """
        Crea el archivo de records VACIO
        """
        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(["-----", 0])
        self.guardar()
