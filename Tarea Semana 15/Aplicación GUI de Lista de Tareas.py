import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    """Agrega una nueva tarea a la lista si el campo de entrada no está vacío."""
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada():
    """Marca la tarea seleccionada como completada cambiando su apariencia."""
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"✔ {tarea}")  # Agrega un check a la tarea
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def agregar_con_enter(event):
    """Permite agregar una tarea presionando la tecla Enter."""
    agregar_tarea()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Campo de entrada y botón para agregar tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_con_enter)  # Asocia la tecla Enter con agregar tarea

boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Botones para marcar como completada y eliminar tareas
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

