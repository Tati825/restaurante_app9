import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, root, restaurante_servicio, mostrar_main):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main

        self.frame = tk.Frame(root, padx=30, pady=30)
        self.frame.pack(expand=True)

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=(0, 10))

        subtitulo = tk.Label(
            self.frame,
            text="Acceso pedagógico"
        )
        subtitulo.pack(pady=(0, 20))

        tk.Label(
            self.frame,
            text="Identificación:"
        ).pack(anchor="w")

        self.identificacion_entry = tk.Entry(
            self.frame,
            width=30
        )
        self.identificacion_entry.pack(pady=(5, 15))

        boton = tk.Button(
            self.frame,
            text="Ingresar",
            width=20,
            command=self.iniciar_sesion
        )
        boton.pack()

        self.identificacion_entry.focus()

    def iniciar_sesion(self):
        identificacion = self.identificacion_entry.get().strip()

        if not identificacion:
            messagebox.showwarning(
                "Campo requerido",
                "Ingrese una identificación"
            )
            return

        usuario = self.restaurante_servicio.buscar_usuario(
            identificacion
        )

        if usuario is None:
            messagebox.showerror(
                "Acceso",
                "Usuario no encontrado"
            )
            return

        self.mostrar_main(usuario)
