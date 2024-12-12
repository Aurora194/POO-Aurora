class Clima:
    def __init__(self):
        self.temperaturas = []

        # Método para ingresar la temperatura diaria

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

        # Método para calcular el promedio de temperaturas

    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

        # Método para ingresar temperaturas para una semana

    def ingresar_temperaturas_semanales(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.ingresar_temperatura(temperatura)

        # Función principal


def main():
    print("Bienvenido al programa de cálculo del promedio semanal del clima.")
    clima = Clima()
    clima.ingresar_temperaturas_semanales()
    promedio = clima.calcular_promedio()
    print(f"El promedio de temperaturas de la semana es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()