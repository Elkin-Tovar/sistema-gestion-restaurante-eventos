import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Casa Sabrosa - Sistema de Gestión (Semana 16)")
        self.geometry("980x600")
        self.minsize(850, 520)

        self.servicio = RestauranteServicio()

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.vista_actual = None
        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = LoginView(self.container, self, self.servicio)
        self.vista_actual.grid(row=0, column=0, sticky="nsew")

    def mostrar_main_view(self, usuario_actual) -> None:
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = MainView(self.container, self, self.servicio, usuario_actual)
        self.vista_actual.grid(row=0, column=0, sticky="nsew")


def main() -> None:
    app = RestauranteApp()
    app.mainloop()


if __name__ == "__main__":
    main()