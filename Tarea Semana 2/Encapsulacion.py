
class Perso:

    def __init__(self, nomb, eda):
        self.__nomb = nomb  # Atributo
        self.__eda = eda  # Atributo

    def obtener_nombre(self):  # Metodo publico
        return self.__nomb

    def set_edad(self, eda):  # Metodo publico
        if eda > 0:
            self.__eda = eda
        else:
            print("Edad no válida")

# Uso de la clase

perso = Perso("Rebeca", 36)
print(perso.obtener_nombre())  # "Rebeca"
perso.set_edad(41)

