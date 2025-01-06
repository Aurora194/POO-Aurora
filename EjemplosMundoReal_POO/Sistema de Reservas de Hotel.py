# reservas de hotel para los clientes

from datetime import datetime


class Reserva:
# Clase que representa una Reserva.

    def __init__(self, nombre_cliente, fecha_reserva):
    # Inicializa una nueva reserva con el nombre del cliente y la fecha.
        self.nombre_cliente = nombre_cliente
        self.fecha_reserva = fecha_reserva

    def __str__(self):
    # Devuelve una representación en string de la reserva.
        return f"Reserva para {self.nombre_cliente} en {self.fecha_reserva.strftime('%Y-%m-%d')}"


class SistemaReservas:
# Clase que maneja el sistema de reservas.

    def __init__(self):
    # Inicializa la lista de reservas.
        self.reservas = []

    def hacer_reserva(self, nombre_cliente):
    # Crea una nueva reserva y la añade a la lista.
        fecha_reserva = datetime.now()
        nueva_reserva = Reserva(nombre_cliente, fecha_reserva)
        self.reservas.append(nueva_reserva)
        print(f"Reserva realizada: {nueva_reserva}")

    def mostrar_reservas(self):
    # Muestra todas las reservas existentes.
        if not self.reservas:
            print("No hay reservas.")
        else:
            print("Reservas actuales:")
            for reserva in self.reservas:
                print(reserva)

    def iniciar(self):
        """Método para iniciar el sistema de reservas."""
        while True:
            nombre_cliente = input("Introduce el nombre del cliente: ")
            self.hacer_reserva(nombre_cliente)

            continuar = input("¿Quieres hacer otra reserva? (s/n): ").strip().lower()
            if continuar != 's':
                break

        self.mostrar_reservas()


if __name__ == "__main__":
    sistema = SistemaReservas()
    sistema.iniciar()