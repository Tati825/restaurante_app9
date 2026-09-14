import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("800x500")
        self.root.minsize(700, 450)

        self.restaurante_servicio = RestauranteServicio()
        self.vista_actual = None

        self.mostrar_login()

    def limpiar_vista(self):
        if self.vista_actual is not None:
            self.vista_actual.frame.destroy()

    def mostrar_login(self):
        self.limpiar_vista()

        self.vista_actual = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_main
        )

    def mostrar_main(self, usuario):
        self.limpiar_vista()

        self.vista_actual = MainView(
            self.root,
            self.restaurante_servicio,
            usuario
        )

def main():
    root = tk.Tk()

    app = RestauranteApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()
