import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta):
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, OSError) as error:
            raise RuntimeError(
                f"No se pudo leer el archivo {ruta}: {error}"
            )
