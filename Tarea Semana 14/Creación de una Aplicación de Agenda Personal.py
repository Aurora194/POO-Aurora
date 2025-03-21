import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry


class AgendaApp :
    def __init__(self, root) :
        self.root = root
        self.root.title("Agenda Personal")

        # Crear contenedores
        self.frame_eventos = tk.Frame(self.root)
        self.frame_eventos.pack(pady=20)

        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=20)

        # Crear TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Crear campos de entrada
        self.txt_fecha = tk.StringVar()
        self.txt_hora = tk.StringVar()
        self.txt_descripcion = tk.StringVar()

        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        tk.Entry(self.frame_entrada, textvariable=self.txt_fecha).grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        tk.Entry(self.frame_entrada, textvariable=self.txt_hora).grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        tk.Entry(self.frame_entrada, textvariable=self.txt_descripcion).grid(row=2, column=1)

        # Botones
        tk.Button(self.frame_entrada, text="Agregar Evento", command=self.agregar_evento).grid(row=3, column=0, pady=10)
        tk.Button(self.frame_entrada, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=3,column=1,pady=10)
        tk.Button(self.frame_entrada, text="Salir", command=root.quit).grid(row=4, columnspan=2, pady=10)

    def agregar_evento(self) :
        """Agrega un nuevo evento a la lista."""
        fecha = self.txt_fecha.get()
        hora = self.txt_hora.get()
        descripcion = self.txt_descripcion.get()

        if fecha and hora and descripcion :
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.txt_fecha.set("")
            self.txt_hora.set("")
            self.txt_descripcion.set("")
        else :
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    def eliminar_evento(self) :
        """Elimina el evento seleccionado."""
        selected_item = self.tree.selection()
        if selected_item :
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm :
                self.tree.delete(selected_item)
        else :
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

        # Inicializar la aplicación


if __name__ == "__main__" :
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()