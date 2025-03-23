import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaPersonal :
    def __init__(self, root) :
        self.root = root
        self.root.title("Agenda Personal")  # Título de la ventana
        self.root.geometry("500x410")  # Tamaño de la ventana principal


        # Frame para la tabla de eventos
        frame_tree = tk.Frame(self.root)
        frame_tree.pack(pady=10)

        # TreeView para mostrar los eventos programados
        self.tree = ttk.Treeview(frame_tree, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Ajuste del ancho de las columnas
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=70)
        self.tree.column("Descripción", width=200)

        self.tree.pack()

        # Frame para el formulario de entrada
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)

        # Campo de entrada para la fecha con DateEntry
        tk.Label(frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(frame_form, date_pattern='yyyy-mm-dd')
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Campo de entrada para la hora
        tk.Label(frame_form, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_form)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        # Campo de entrada para la descripción del evento
        tk.Label(frame_form, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(frame_form, width=30)
        self.entry_desc.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones de acción
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        # Botón para agregar un evento a la lista
        btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.grid(row=0, column=0, padx=5)

        # Botón para eliminar un evento seleccionado
        btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento", command=self.eliminar_evento)
        btn_eliminar.grid(row=0, column=1, padx=5)

        # Botón para cerrar la aplicación
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.root.quit)
        btn_salir.grid(row=0, column=2, padx=5)

    def agregar_evento(self) :
        """Función para agregar un evento a la lista."""
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        # Validación de que los campos no estén vacíos
        if fecha and hora and descripcion :
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
        else :
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def eliminar_evento(self) :
        """Función para eliminar un evento seleccionado."""
        selected_item = self.tree.selection()  # Obtener el elemento seleccionado
        if selected_item :
            confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
            if confirm :
                self.tree.delete(selected_item)  # Eliminar el evento de la lista
        else :
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")


if __name__ == "__main__" :
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
