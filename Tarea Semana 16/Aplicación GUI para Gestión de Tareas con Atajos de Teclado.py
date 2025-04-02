import tkinter as tk
from tkinter import ttk, messagebox

class TaskManager:
    def __init__(self, root):
        """
        Inicializa la aplicación de gestión de tareas.

        Args:
            root (tk.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista para almacenar las tareas (True si completada, False si pendiente)
        self.tasks = []

        # Variable para rastrear el índice de la tarea seleccionada en la lista
        self.selected_task_index = None

        # Configurar la interfaz gráfica
        self._create_widgets()

        # Configurar los atajos de teclado
        self._setup_keyboard_shortcuts()

    def _create_widgets(self):
        """
        Crea y organiza los widgets de la interfaz de usuario.
        """
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Campo de entrada para añadir nuevas tareas
        self.new_task_entry = ttk.Entry(main_frame, width=40)
        self.new_task_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Botón para añadir tarea
        add_button = ttk.Button(main_frame, text="Añadir Tarea", command=self.add_task)
        add_button.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

        # Lista de tareas
        self.task_list_var = tk.StringVar(value=[""])
        self.task_list = tk.Listbox(main_frame, listvariable=self.task_list_var, height=10)
        self.task_list.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        self.task_list.bind('<<ListboxSelect>>', self._on_task_select)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Frame para los botones de acción
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Botón para marcar como completada
        self.complete_button = ttk.Button(action_frame, text="Marcar como Completada", command=self.mark_complete, state=tk.DISABLED)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar tarea
        self.delete_button = ttk.Button(action_frame, text="Eliminar Tarea", command=self.delete_task, state=tk.DISABLED)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def _setup_keyboard_shortcuts(self):
        """
        Define y vincula los atajos de teclado a sus respectivas funciones.
        """
        # Atajo para añadir tarea (Enter en el campo de entrada)
        self.new_task_entry.bind("<Return>", lambda event: self.add_task())

        # Atajo para marcar como completada (tecla "c")
        self.root.bind("c", lambda event: self.mark_complete())
        self.root.bind("C", lambda event: self.mark_complete()) # Considerar mayúsculas

        # Atajo para eliminar tarea (tecla "Delete" o "d")
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("d", lambda event: self.delete_task())
        self.root.bind("D", lambda event: self.delete_task()) # Considerar mayúsculas

        # Atajo para cerrar la aplicación (tecla "Escape" o "Espacio")
        self.root.bind("<Escape>", lambda event: self.close_application())
        self.root.bind("<space>", lambda event: self.close_application())

    def add_task(self):
        """
        Añade una nueva tarea a la lista.
        """
        new_task_text = self.new_task_entry.get().strip()
        if new_task_text:
            self.tasks.append({"text": new_task_text, "completed": False})
            self._update_task_list()
            self.new_task_entry.delete(0, tk.END)

    def mark_complete(self):
        """
        Marca la tarea seleccionada como completada.
        """
        if self.selected_task_index is not None:
            if 0 <= self.selected_task_index < len(self.tasks):
                self.tasks[self.selected_task_index]["completed"] = True
                self._update_task_list()
                self.selected_task_index = None # Deseleccionar después de marcar como completada
                self._update_button_states()

    def delete_task(self):
        """
        Elimina la tarea seleccionada de la lista.
        """
        if self.selected_task_index is not None:
            if 0 <= self.selected_task_index < len(self.tasks):
                del self.tasks[self.selected_task_index]
                self._update_task_list()
                self.selected_task_index = None # Deseleccionar después de eliminar
                self._update_button_states()

    def _update_task_list(self):
        """
        Actualiza la visualización de la lista de tareas en la interfaz.
        Aplica formato para indicar tareas completadas.
        """
        displayed_tasks = []
        for task in self.tasks:
            if task["completed"]:
                displayed_tasks.append("[Completada] " + task["text"])
            else:
                displayed_tasks.append(task["text"])
        self.task_list_var.set(displayed_tasks)

        # Re-seleccionar la tarea si el índice aún es válido después de una operación
        if self.selected_task_index is not None and 0 <= self.selected_task_index < len(self.tasks):
            self.task_list.selection_clear(0, tk.END)
            self.task_list.selection_set(self.selected_task_index)
            self.task_list.activate(self.selected_task_index)

    def _on_task_select(self, event):
        """
        Se ejecuta cuando se selecciona una tarea en la lista.
        Actualiza el índice de la tarea seleccionada y el estado de los botones.
        """
        try:
            self.selected_task_index = self.task_list.curselection()[0]
        except IndexError:
            self.selected_task_index = None
        self._update_button_states()

    def _update_button_states(self):
        """
        Habilita o deshabilita los botones de acción dependiendo de si hay una tarea seleccionada.
        """
        if self.selected_task_index is not None:
            self.complete_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.complete_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def close_application(self):
        """
        Cierra la aplicación.
        """
        if messagebox.askokcancel("Cerrar", "¿Estás seguro de que quieres cerrar la aplicación?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()