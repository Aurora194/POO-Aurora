# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre  # Atributo protegido
        self._salario = salario  # Atributo protegido

    def obtener_info(self):
        """Método para obtener información básica del empleado."""
        return f"Empleado: {self._nombre}, Salario: {self._salario}"

    def calcular_bono(self):
        """Método abstracto que debería ser implementado en clases derivadas."""
        raise NotImplementedError("Este método debe ser sobrescrito en la clase derivada")


# Clase derivada
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_bono(self):
        """Cálculo del bono para empleado a tiempo completo (10% del salario)."""
        return self._salario * 0.10


# Clase derivada
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, salario, horas_trabajadas):
        super().__init__(nombre, salario)
        self.horas_trabajadas = horas_trabajadas  # Atributo específico de tiempo parcial

    def obtener_info(self):
        """Sobrescribe método para incluir horas trabajadas."""
        return f"Empleado a Tiempo Parcial: {self._nombre}, Salario: {self._salario}, Horas: {self.horas_trabajadas}"

    def calcular_bono(self):
        """Cálculo del bono para empleado a tiempo parcial (5% del salario por hora trabajada)."""
        return self.horas_trabajadas * (self._salario * 0.05)


# Función para mostrar información del empleado
def mostrar_info_empleado(empleado):
    """Muestra la información y el bono de un empleado."""
    print(empleado.obtener_info())
    print(f"Bono: {empleado.calcular_bono()}")


# Creación de instancias de las clases
empleado1 = EmpleadoTiempoCompleto("Ana", 50000)
empleado2 = EmpleadoTiempoParcial("Luis", 30000, 20)

# Demostración del polimorfismo
mostrar_info_empleado(empleado1)
mostrar_info_empleado(empleado2)