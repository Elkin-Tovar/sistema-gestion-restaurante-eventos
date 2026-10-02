import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):

    def __init__(self, parent, controlador, servicio) -> None:
        super().__init__(parent)
        self.controlador = controlador
        self.servicio = servicio

        self.configure(bg="#f0f0f0")

        lbl_titulo = tk.Label(
            self, text="CASA SABROSA - INICIO DE SESIÓN", 
            font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2c3e50"
        )
        lbl_titulo.pack(pady=35)

        frame_form = tk.Frame(self, bg="#ffffff", padx=25, pady=25, relief="solid", bd=1)
        frame_form.pack(pady=10)

        lbl_user = tk.Label(frame_form, text="Correo Electrónico:", font=("Arial", 10), bg="#ffffff")
        lbl_user.pack(anchor="w", pady=5)
        self.entry_user = tk.Entry(frame_form, font=("Arial", 10), width=28)
        self.entry_user.pack(pady=5)

        lbl_pass = tk.Label(frame_form, text="Contraseña:", font=("Arial", 10), bg="#ffffff")
        lbl_pass.pack(anchor="w", pady=5)
        self.entry_pass = tk.Entry(frame_form, font=("Arial", 10), width=28, show="*")
        self.entry_pass.pack(pady=5)

        lbl_nota = tk.Label(
            frame_form, text="Contraseña empleados: 123456\nAdmin: admin / 1234", 
            font=("Arial", 8, "italic"), bg="#ffffff", fg="#7f8c8d"
        )
        lbl_nota.pack(pady=5)

        btn_ingresar = tk.Button(
            frame_form, text="Ingresar", font=("Arial", 10, "bold"), 
            bg="#27ae60", fg="white", width=20, pady=5, cursor="hand2", 
            command=self._intentar_login
        )
        btn_ingresar.pack(pady=15)

    def _intentar_login(self) -> None:
        usuario_str = self.entry_user.get()
        clave = self.entry_pass.get()

        usuario_obj = self.servicio.validar_acceso(usuario_str, clave)
        if usuario_obj:
            self.controlador.mostrar_main_view(usuario_obj)
        else:
            messagebox.showerror("Error de Acceso", "Correo o contraseña incorrectos. Verifique sus credenciales.")