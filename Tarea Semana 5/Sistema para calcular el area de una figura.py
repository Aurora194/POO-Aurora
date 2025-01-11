# Programa para calcular el área de diferentes figuras geométricas.
# El usuario puede elegir entre un círculo, un cuadrado o un triángulo.
# El programa utiliza distintos tipos de datos y convenciones de identificadores en snake_case.

import math  # Se importa la librería math para realizar cálculos relacionados con el círculo.

def Calcular_Area_Circulo(radio):
    # Calcula el área de un círculo dado su radio.
    return math.pi * radio ** 2  # Fórmula del área de un círculo: π * r²

def Calcular_Area_Cuadrado(lado):
    # Calcula el área de un cuadrado dado su lado.
    return lado ** 2  # Fórmula del área de un cuadrado: lado²

def Calcular_Area_Triangulo(base, altura):
    # Calcula el área de un triángulo dado su base y altura.
    return (base * altura) / 2  # Fórmula del área de un triángulo: (base * altura) / 2

def main():
    # Función principal que ejecuta el programa.
    print("Seleccione la figura para calcular el área:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")
    
    opcion = int(input("Ingrese el número de la opción seleccionada: "))
    
    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        area = Calcular_Area_Circulo(radio)
        print(f"El área del círculo es: {area:.2f} unidades cuadradas.")
        
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = Calcular_Area_Cuadrado(lado)
        print(f"El área del cuadrado es: {area:.2f} unidades cuadradas.")
        
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = Calcular_Area_Triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f} unidades cuadradas.")
        
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 3.")
    
# Ejecutamos la función principal
if __name__ == "__main__":
    main()
