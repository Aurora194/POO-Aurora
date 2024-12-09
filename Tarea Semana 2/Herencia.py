class Vehiculo:
    def __init__(self, marc, mode):
        self.mode = mode
        self.marc = marc


    def descripcion(self):
        return f"{self.marc} {self.mode}"

class Coche(Vehiculo):
    def __init__(self, marc, mode, puertas):
        super().__init__(marc, mode)  # Llamada al constructor de la superclase
        self.puertas = puertas

    def descripcion(self):
        return f"{self.marc} {self.mode}, {self.puertas} puertas"


# Uso de la herencia
coche = Coche("Chevrolet", "Onix Turbo", 4)
print(coche.descripcion()) # "Chevrolet Onix Turbo, 4 puertas"