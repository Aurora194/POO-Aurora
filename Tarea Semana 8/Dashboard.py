import os
import subprocess

# Definición de códigos de color ANSI
class Color:
    CYAN = "\033[96m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

historial = []  # Lista para almacenar scripts ejecutados recientemente

def obtener_ruta_base():
    """Obtiene la ruta base del script actual."""
    return os.path.abspath(os.getcwd())

def mostrar_codigo(ruta_script):
    """Lee y muestra el código fuente de un script en la terminal."""
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(Color.CYAN + f"\n--- Código de {ruta_script} ---\n" + Color.RESET)
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(Color.RED + "El archivo no se encontró." + Color.RESET)
    except Exception as e:
        print(Color.RED + f"Error al leer el archivo: {e}" + Color.RESET)
    return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script en una nueva terminal y lo agrega al historial."""
    try:
        historial.append(ruta_script)  # Agregar el script al historial de ejecución
        if os.name == 'nt':  # Verificar si el sistema es Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Para sistemas basados en Unix
            subprocess.Popen(['x-terminal-emulator', '-e', 'python3', ruta_script])
    except Exception as e:
        print(Color.RED + f"Error al ejecutar el código: {e}" + Color.RESET)

def mostrar_menu():
    """Muestra el menú principal y maneja la navegación del usuario."""
    ruta_base = obtener_ruta_base()

    while True:
        print(Color.BLUE + "\nMenú Principal - Dashboard" + Color.RESET)
        print("1 - Seleccionar unidad")
        print("2 - Crear nueva unidad")
        print("3 - Ver historial de ejecución")
        print("0 - Salir")

        try:
            opcion = input("Elige una opción: ").strip()
        except (EOFError, OSError):
            print(Color.RED + "\nEntrada no disponible. Saliendo..." + Color.RESET)
            break

        if opcion == '0':
            print(Color.RED + "Saliendo..." + Color.RESET)
            break
        elif opcion == '1':
            # Obtener lista de unidades (directorios dentro de la ruta base)
            unidades = [d for d in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, d))]
            print(Color.GREEN + "\nUnidades disponibles:" + Color.RESET)
            for i, unidad in enumerate(unidades, start=1):
                print(f"{i} - {unidad}")
        elif opcion == '2':
            try:
                nueva_unidad = input("Nombre de la nueva unidad: ").strip()
                os.makedirs(os.path.join(ruta_base, nueva_unidad), exist_ok=True)
                print(Color.GREEN + "Unidad creada con éxito." + Color.RESET)
            except (EOFError, OSError):
                print(Color.RED + "Error al crear la unidad." + Color.RESET)
        elif opcion == '3':
            print(Color.MAGENTA + "\nHistorial de scripts ejecutados:" + Color.RESET)
            if historial:
                for script in historial:
                    print(script)
            else:
                print(Color.RED + "No hay scripts en el historial." + Color.RESET)
        else:
            print(Color.RED + "Opción no válida." + Color.RESET)

# Ejecutar el dashboard si el script es ejecutado directamente
if __name__ == "__main__":
    mostrar_menu()