# Función para ingresar las temperaturas diarias
def ingresar_temperaturas(n):
    temperaturas = []
    for i in range(n):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    dias = 7  # Número de días en una semana
    print("Bienvenido al programa de cálculo del promedio semanal del clima.")
    temperaturas = ingresar_temperaturas(dias)
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio de temperaturas de la semana es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()