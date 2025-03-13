import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_lista():
    lista.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Etiqueta y campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()


