import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root, restaurante_servicio, usuario):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.usuario = usuario

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        self.crear_interfaz()

    def crear_interfaz(self):
        encabezado = tk.Frame(self.frame)
        encabezado.pack(fill="x", pady=(0, 15))

        titulo = tk.Label(
            encabezado,
            text="Panel principal",
            font=("Arial", 20, "bold")
        )
        titulo.pack(side="left")

        usuario_label = tk.Label(
            encabezado,
            text=f"Usuario: {self.usuario.nombre}"
        )
        usuario_label.pack(side="right")

        notebook = ttk.Notebook(self.frame)
        notebook.pack(fill="both", expand=True)

        productos_frame = tk.Frame(notebook)
        usuarios_frame = tk.Frame(notebook)

        notebook.add(
            productos_frame,
            text="Productos"
        )

        notebook.add(
            usuarios_frame,
            text="Usuarios"
        )

        self.crear_tabla_productos(productos_frame)
        self.crear_tabla_usuarios(usuarios_frame)

    def crear_tabla_productos(self, parent):
        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio"
        )

        tabla = ttk.Treeview(
            parent,
            columns=columnas,
            show="headings"
        )

        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("categoria", text="Categoría")
        tabla.heading("precio", text="Precio")

        tabla.column("codigo", width=100)
        tabla.column("nombre", width=220)
        tabla.column("categoria", width=180)
        tabla.column("precio", width=100)

        tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        productos = self.restaurante_servicio.obtener_productos()

        for producto in productos:
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}"
                )
            )

    def crear_tabla_usuarios(self, parent):
        columnas = (
            "identificacion",
            "nombre",
            "correo"
        )

        tabla = ttk.Treeview(
            parent,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "identificacion",
            text="Identificación"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.heading(
            "correo",
            text="Correo"
        )

        tabla.column(
            "identificacion",
            width=150
        )

        tabla.column(
            "nombre",
            width=220
        )

        tabla.column(
            "correo",
            width=250
        )

        tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        usuarios = self.restaurante_servicio.obtener_usuarios()

        for usuario in usuarios:
            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo
                )
            )
