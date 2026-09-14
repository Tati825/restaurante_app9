import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.ruta_productos = os.path.join(
            base_dir, "datos", "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            base_dir, "datos", "usuarios.json"
        )

        self.productos = []
        self.usuarios = []

        self.cargar_datos()

    def cargar_datos(self):
        datos_productos = ArchivoServicio.leer_json(
            self.ruta_productos
        )

        datos_usuarios = ArchivoServicio.leer_json(
            self.ruta_usuarios
        )

        self.productos = [
            Producto.from_dict(datos)
            for datos in datos_productos
        ]

        self.usuarios = [
            Usuario.from_dict(datos)
            for datos in datos_usuarios
        ]

    def obtener_productos(self):
        return self.productos

    def obtener_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None
