class Usuario:
    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("La identificación no puede estar vacía")
        self._identificacion = str(valor).strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = str(valor).strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("El correo no puede estar vacío")

        if "@" not in str(valor):
            raise ValueError("El correo no tiene un formato válido")

        self._correo = str(valor).strip()

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"]
        )

    def __str__(self):
        return f"{self.identificacion} - {self.nombre} - {self.correo}"
