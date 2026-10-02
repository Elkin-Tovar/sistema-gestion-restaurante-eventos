import os
import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):

    def __init__(self, parent, controlador, servicio, usuario_actual) -> None:
        super().__init__(parent)
        self.controlador = controlador
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.configure(bg="#f8f9fa")

        frame_top = tk.Frame(self, bg="#1e272e", height=45)
        frame_top.pack(fill="x", side="top")
        frame_top.pack_propagate(False)

        self.logo_img = self._cargar_icono("assets", "logo.png", reducir_factor=15)
        if self.logo_img:
            lbl_logo = tk.Label(frame_top, image=self.logo_img, bg="#1e272e")
            lbl_logo.pack(side="left", padx=8, pady=4)

        rol_txt = f"Rol: {self.usuario_actual.rol}" if self.usuario_actual else "Invitado"
        lbl_header = tk.Label(
            frame_top, text=f"Casa Sabrosa - Gestión ({rol_txt})", font=("Arial", 10, "bold"), bg="#1e272e", fg="#ffffff"
        )
        lbl_header.pack(side="left", padx=4, pady=12)

        self.icon_cerrar = self._cargar_icono("assets", "cerrar.png", reducir_factor=20)
        btn_salir = tk.Button(
            frame_top, text=" Salir", image=self.icon_cerrar, compound="left",
            font=("Arial", 8, "bold"), bg="#c0392b", fg="white", 
            relief="raised", bd=1, padx=5, pady=1, cursor="hand2", command=self.controlador.mostrar_login_view
        )
        btn_salir.pack(side="right", padx=10, pady=8)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=6, pady=6)

        self.icon_prod = self._cargar_icono("assets", "user-interface.png", reducir_factor=20)
        self.icon_user = self._cargar_icono("assets", "registro-en-linea.png", reducir_factor=20)
        self.icon_venta = self._cargar_icono("assets", "metodo-de-pago.png", reducir_factor=20)

        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text=" Productos ", image=self.icon_prod, compound="left")
        self._construir_pestana_productos()

        self.tab_usuarios = ttk.Frame(self.notebook)
        if self.usuario_actual and self.usuario_actual.rol == "Administrador":
            self.notebook.add(self.tab_usuarios, text=" Usuarios ", image=self.icon_user, compound="left")
            self._construir_pestana_usuarios()

        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text=" Ventas ", image=self.icon_venta, compound="left")
        self._construir_pestana_ventas()

        self.actualizar_tabla_productos()
        if self.usuario_actual and self.usuario_actual.rol == "Administrador":
            self.actualizar_tabla_usuarios()
        self.actualizar_tabla_ventas()
        self.actualizar_combos_ventas()

    def _cargar_icono(self, carpeta: str, archivo: str, reducir_factor: int = 20):
        ruta = os.path.join(carpeta, archivo)
        if os.path.exists(ruta):
            try:
                img = tk.PhotoImage(file=ruta)
                if reducir_factor > 1:
                    img = img.subsample(reducir_factor, reducir_factor)
                return img
            except Exception:
                return None
        return None

    def _construir_pestana_productos(self) -> None:
        frame_form = ttk.LabelFrame(self.tab_productos, text=" Formulario de Producto ")
        frame_form.pack(side="left", fill="y", padx=6, pady=6, ipadx=4, ipady=4)

        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky="w", pady=3, padx=3)
        self.ent_codigo = ttk.Entry(frame_form, width=15)
        self.ent_codigo.grid(row=0, column=1, pady=3, padx=2)

        self.img_buscar = self._cargar_icono("assets", "buscar.png", reducir_factor=20)
        btn_buscar = tk.Button(
            frame_form, text=" Buscar", image=self.img_buscar, compound="left",
            font=("Arial", 7, "bold"), bg="#3498db", fg="white", relief="raised", bd=1, padx=4, pady=1, cursor="hand2", command=self._buscar_producto_form
        )
        btn_buscar.grid(row=0, column=2, padx=2)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=3, padx=3)
        self.ent_nombre = ttk.Entry(frame_form, width=20)
        self.ent_nombre.grid(row=1, column=1, columnspan=2, pady=3, padx=2)

        ttk.Label(frame_form, text="Categoría:").grid(row=2, column=0, sticky="w", pady=3, padx=3)
        self.ent_categoria = ttk.Entry(frame_form, width=20)
        self.ent_categoria.grid(row=2, column=1, columnspan=2, pady=3, padx=2)

        ttk.Label(frame_form, text="Precio ($):").grid(row=3, column=0, sticky="w", pady=3, padx=3)
        self.ent_precio = ttk.Entry(frame_form, width=20)
        self.ent_precio.grid(row=3, column=1, columnspan=2, pady=3, padx=2)

        ttk.Label(frame_form, text="Stock:").grid(row=4, column=0, sticky="w", pady=3, padx=3)
        self.ent_stock = ttk.Entry(frame_form, width=20)
        self.ent_stock.grid(row=4, column=1, columnspan=2, pady=3, padx=2)

        frame_botones = ttk.Frame(frame_form)
        frame_botones.grid(row=5, column=0, columnspan=3, pady=8)

        self.img_reg = self._cargar_icono("assets", "registro-en-linea.png", reducir_factor=20)
        self.img_act = self._cargar_icono("assets", "actualizar.png", reducir_factor=20)
        self.img_del = self._cargar_icono("assets", "borrar.png", reducir_factor=20)
        self.img_lim = self._cargar_icono("assets", "limpiar.png", reducir_factor=20)

        btn_registrar = tk.Button(
            frame_botones, text=" Registrar", image=self.img_reg, compound="left",
            bg="#27ae60", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=4, pady=2, cursor="hand2", command=self._registrar_producto
        )
        btn_registrar.grid(row=0, column=0, padx=2, pady=2, sticky="ew")

        btn_actualizar = tk.Button(
            frame_botones, text=" Actualizar", image=self.img_act, compound="left",
            bg="#e67e22", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=4, pady=2, cursor="hand2", command=self._actualizar_producto
        )
        btn_actualizar.grid(row=0, column=1, padx=2, pady=2, sticky="ew")

        btn_eliminar = tk.Button(
            frame_botones, text=" Eliminar", image=self.img_del, compound="left",
            bg="#c0392b", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=4, pady=2, cursor="hand2", command=self._eliminar_producto
        )
        btn_eliminar.grid(row=1, column=0, padx=2, pady=2, sticky="ew")

        btn_limpiar = tk.Button(
            frame_botones, text=" Limpiar", image=self.img_lim, compound="left",
            bg="#7f8c8d", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=4, pady=2, cursor="hand2", command=self._limpiar_formulario
        )
        btn_limpiar.grid(row=1, column=1, padx=2, pady=2, sticky="ew")

        frame_tabla = ttk.LabelFrame(self.tab_productos, text=" Listado de Productos ")
        frame_tabla.pack(side="right", fill="both", expand=True, padx=6, pady=6)

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tree_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
        
        self.tree_productos.heading("codigo", text="Código")
        self.tree_productos.heading("nombre", text="Nombre")
        self.tree_productos.heading("categoria", text="Categoría")
        self.tree_productos.heading("precio", text="Precio")
        self.tree_productos.heading("stock", text="Stock")

        self.tree_productos.column("codigo", width=60, anchor="center")
        self.tree_productos.column("nombre", width=120, anchor="w")
        self.tree_productos.column("categoria", width=90, anchor="w")
        self.tree_productos.column("precio", width=60, anchor="e")
        self.tree_productos.column("stock", width=45, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree_productos.yview)
        self.tree_productos.configure(yscrollcommand=scrollbar.set)

        self.tree_productos.pack(side="left", fill="both", expand=True, padx=3, pady=3)
        scrollbar.pack(side="right", fill="y", pady=3)

    def _construir_pestana_usuarios(self) -> None:
        frame_form_u = ttk.LabelFrame(self.tab_usuarios, text=" Gestión de Usuarios ")
        frame_form_u.pack(side="left", fill="y", padx=6, pady=6, ipadx=4, ipady=4)

        ttk.Label(frame_form_u, text="Identificación:").grid(row=0, column=0, sticky="w", pady=3, padx=3)
        self.ent_user_id = ttk.Entry(frame_form_u, width=20)
        self.ent_user_id.grid(row=0, column=1, pady=3, padx=2)

        ttk.Label(frame_form_u, text="Nombre:").grid(row=1, column=0, sticky="w", pady=3, padx=3)
        self.ent_user_nombre = ttk.Entry(frame_form_u, width=20)
        self.ent_user_nombre.grid(row=1, column=1, pady=3, padx=2)

        ttk.Label(frame_form_u, text="Correo:").grid(row=2, column=0, sticky="w", pady=3, padx=3)
        self.ent_user_correo = ttk.Entry(frame_form_u, width=20)
        self.ent_user_correo.grid(row=2, column=1, pady=3, padx=2)

        ttk.Label(frame_form_u, text="Rol:").grid(row=3, column=0, sticky="w", pady=3, padx=3)
        self.combo_rol = ttk.Combobox(frame_form_u, state="readonly", width=18, values=["Administrador", "Empleado", "Cliente"])
        self.combo_rol.grid(row=3, column=1, pady=3, padx=2)
        self.combo_rol.set("Cliente")
        self.combo_rol.bind("<<ComboboxSelected>>", self._evento_combobox_rol)

        frame_botones_u = ttk.Frame(frame_form_u)
        frame_botones_u.grid(row=4, column=0, columnspan=2, pady=10)

        btn_reg_user = tk.Button(
            frame_botones_u, text="Registrar", bg="#27ae60", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=6, pady=2, cursor="hand2", command=self._registrar_usuario
        )
        btn_reg_user.grid(row=0, column=0, padx=2, pady=2, sticky="ew")

        btn_act_user = tk.Button(
            frame_botones_u, text="Actualizar", bg="#e67e22", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=6, pady=2, cursor="hand2", command=self._actualizar_usuario
        )
        btn_act_user.grid(row=0, column=1, padx=2, pady=2, sticky="ew")

        btn_del_user = tk.Button(
            frame_botones_u, text="Eliminar", bg="#c0392b", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=6, pady=2, cursor="hand2", command=self._eliminar_usuario
        )
        btn_del_user.grid(row=1, column=0, padx=2, pady=2, sticky="ew")

        btn_lim_user = tk.Button(
            frame_botones_u, text="Limpiar", bg="#7f8c8d", fg="white", font=("Arial", 7, "bold"), relief="raised", bd=1, padx=6, pady=2, cursor="hand2", command=self._limpiar_formulario_usuarios
        )
        btn_lim_user.grid(row=1, column=1, padx=2, pady=2, sticky="ew")

        frame_tabla_u = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios Registrados ")
        frame_tabla_u.pack(side="right", fill="both", expand=True, padx=6, pady=6)

        columnas_u = ("id", "nombre", "correo", "rol")
        self.tree_usuarios = ttk.Treeview(frame_tabla_u, columns=columnas_u, show="headings", height=10)
        
        self.tree_usuarios.heading("id", text="Identificación")
        self.tree_usuarios.heading("nombre", text="Nombre")
        self.tree_usuarios.heading("correo", text="Correo")
        self.tree_usuarios.heading("rol", text="Rol")

        self.tree_usuarios.column("id", width=80, anchor="center")
        self.tree_usuarios.column("nombre", width=120, anchor="w")
        self.tree_usuarios.column("correo", width=140, anchor="w")
        self.tree_usuarios.column("rol", width=90, anchor="center")

        scrollbar_u = ttk.Scrollbar(frame_tabla_u, orient="vertical", command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscrollcommand=scrollbar_u.set)

        self.tree_usuarios.pack(side="left", fill="both", expand=True, padx=3, pady=3)
        scrollbar_u.pack(side="right", fill="y", pady=3)

        self.tree_usuarios.bind("<<TreeviewSelect>>", self._evento_seleccionar_usuario)
        self.bind("<Return>", self._evento_tecla_return)
        self.bind("<Escape>", self._evento_tecla_escape)

    def _construir_pestana_ventas(self) -> None:
        frame_form_v = ttk.LabelFrame(self.tab_ventas, text=" Registrar Venta ")
        frame_form_v.pack(side="left", fill="y", padx=6, pady=6, ipadx=6, ipady=6)

        ttk.Label(frame_form_v, text="Usuario (Correo):", font=("Arial", 8, "bold")).pack(anchor="w", pady=3, padx=3)
        self.combo_usuario = ttk.Combobox(frame_form_v, state="readonly", width=22)
        self.combo_usuario.pack(pady=3, padx=3)

        ttk.Label(frame_form_v, text="Producto:", font=("Arial", 8, "bold")).pack(anchor="w", pady=3, padx=3)
        self.combo_producto = ttk.Combobox(frame_form_v, state="readonly", width=22)
        self.combo_producto.pack(pady=3, padx=3)

        btn_registrar_venta = tk.Button(
            frame_form_v, text="Registrar Venta", font=("Arial", 8, "bold"), 
            bg="#2980b9", fg="white", relief="raised", bd=1, padx=6, pady=2, cursor="hand2", command=self._callback_registrar_venta
        )
        btn_registrar_venta.pack(pady=10)

        frame_tabla_v = ttk.LabelFrame(self.tab_ventas, text=" Historial de Ventas ")
        frame_tabla_v.pack(side="right", fill="both", expand=True, padx=6, pady=6)

        columnas_v = ("id_venta", "usuario", "producto", "fecha")
        self.tree_ventas = ttk.Treeview(frame_tabla_v, columns=columnas_v, show="headings", height=10)
        
        self.tree_ventas.heading("id_venta", text="ID Venta")
        self.tree_ventas.heading("usuario", text="Usuario ID")
        self.tree_ventas.heading("producto", text="Producto Cód.")
        self.tree_ventas.heading("fecha", text="Fecha y Hora")

        self.tree_ventas.column("id_venta", width=95, anchor="center")
        self.tree_ventas.column("usuario", width=75, anchor="center")
        self.tree_ventas.column("producto", width=75, anchor="center")
        self.tree_ventas.column("fecha", width=130, anchor="center")

        scrollbar_v = ttk.Scrollbar(frame_tabla_v, orient="vertical", command=self.tree_ventas.yview)
        self.tree_ventas.configure(yscrollcommand=scrollbar_v.set)

        self.tree_ventas.pack(side="left", fill="both", expand=True, padx=3, pady=3)
        scrollbar_v.pack(side="right", fill="y", pady=3)

    def _evento_seleccionar_usuario(self, event) -> None:
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            return
        item = self.tree_usuarios.item(seleccion)
        valores = item.get("values")
        if valores:
            identificacion = str(valores[0])
            usuario_obj = self.servicio.buscar_usuario(identificacion)
            if usuario_obj:
                self._limpiar_formulario_usuarios()
                self.ent_user_id.insert(0, usuario_obj.identificacion)
                self.ent_user_id.config(state="disabled")
                self.ent_user_nombre.insert(0, usuario_obj.nombre)
                self.ent_user_correo.insert(0, usuario_obj.correo)
                self.combo_rol.set(usuario_obj.rol)

    def _evento_tecla_return(self, event) -> None:
        if self.notebook.select() == str(self.tab_usuarios):
            self._registrar_usuario()

    def _evento_tecla_escape(self, event) -> None:
        if self.notebook.select() == str(self.tab_usuarios):
            self._limpiar_formulario_usuarios()

    def _evento_combobox_rol(self, event) -> None:
        pass

    def actualizar_tabla_productos(self) -> None:
        for row in self.tree_productos.get_children():
            self.tree_productos.delete(row)
        for p in self.servicio.obtener_productos():
            self.tree_productos.insert("", "end", values=(p.codigo, p.nombre, p.categoria, f"${p.precio:.2f}", p.stock))

    def actualizar_tabla_usuarios(self) -> None:
        for row in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(row)
        for u in self.servicio.obtener_usuarios():
            self.tree_usuarios.insert("", "end", values=(u.identificacion, u.nombre, u.correo, u.rol))

    def actualizar_tabla_ventas(self) -> None:
        for row in self.tree_ventas.get_children():
            self.tree_ventas.delete(row)
        for v in self.servicio.obtener_ventas():
            self.tree_ventas.insert("", "end", values=(v.id_venta, v.usuario_identificacion, v.producto_codigo, v.fecha))

    def actualizar_combos_ventas(self) -> None:
        usuarios = self.servicio.obtener_usuarios()
        self.combo_usuario['values'] = [f"{u.identificacion} - {u.correo}" for u in usuarios]
        
        productos = self.servicio.obtener_productos()
        self.combo_producto['values'] = [f"{p.codigo} - {p.nombre} (${p.precio:.2f})" for p in productos]

    def _callback_registrar_venta(self) -> None:
        sel_usuario = self.combo_usuario.get()
        sel_producto = self.combo_producto.get()

        if not sel_usuario or not sel_producto:
            messagebox.showwarning("Advertencia", "Debe seleccionar un usuario y un producto.")
            return

        usuario_id = sel_usuario.split(" - ")[0]
        producto_codigo = sel_producto.split(" - ")[0]

        if self.servicio.registrar_venta(usuario_id, producto_codigo):
            messagebox.showinfo("Éxito", "Venta registrada con éxito.")
            self.actualizar_tabla_ventas()
            self.combo_usuario.set('')
            self.combo_producto.set('')
        else:
            messagebox.showerror("Error", "No se pudo registrar la venta.")

    def _limpiar_formulario(self) -> None:
        self.ent_codigo.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_categoria.delete(0, tk.END)
        self.ent_precio.delete(0, tk.END)
        self.ent_stock.delete(0, tk.END)

    def _limpiar_formulario_usuarios(self) -> None:
        self.ent_user_id.config(state="normal")
        self.ent_user_id.delete(0, tk.END)
        self.ent_user_nombre.delete(0, tk.END)
        self.ent_user_correo.delete(0, tk.END)
        self.combo_rol.set("Cliente")
        if self.tree_usuarios.selection():
            self.tree_usuarios.selection_remove(self.tree_usuarios.selection())

    def _buscar_producto_form(self) -> None:
        codigo = self.ent_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Advertencia", "Ingrese un código.")
            return
        p = self.servicio.buscar_producto(codigo)
        if p:
            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, p.nombre)
            self.ent_categoria.delete(0, tk.END)
            self.ent_categoria.insert(0, p.categoria)
            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, str(p.precio))
            self.ent_stock.delete(0, tk.END)
            self.ent_stock.insert(0, str(p.stock))
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def _registrar_producto(self) -> None:
        codigo = self.ent_codigo.get().strip()
        nombre = self.ent_nombre.get().strip()
        categoria = self.ent_categoria.get().strip()
        try:
            precio = float(self.ent_precio.get().strip())
            stock = int(self.ent_stock.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser numéricos.")
            return

        if self.servicio.registrar_producto(codigo, nombre, categoria, precio, stock):
            messagebox.showinfo("Éxito", "Producto registrado.")
            self.actualizar_tabla_productos()
            self.actualizar_combos_ventas()
            self._limpiar_formulario()
        else:
            messagebox.showerror("Error", "Código duplicado o campos vacíos.")

    def _actualizar_producto(self) -> None:
        codigo = self.ent_codigo.get().strip()
        nombre = self.ent_nombre.get().strip()
        categoria = self.ent_categoria.get().strip()
        try:
            precio = float(self.ent_precio.get().strip())
            stock = int(self.ent_stock.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Precio y stock numéricos requeridos.")
            return

        if self.servicio.actualizar_producto(codigo, nombre, categoria, precio, stock):
            messagebox.showinfo("Éxito", "Producto actualizado.")
            self.actualizar_tabla_productos()
            self.actualizar_combos_ventas()
            self._limpiar_formulario()
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def _eliminar_producto(self) -> None:
        codigo = self.ent_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Advertencia", "Ingrese el código.")
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar el producto {codigo}?"):
            if self.servicio.eliminar_producto(codigo):
                messagebox.showinfo("Éxito", "Producto eliminado.")
                self.actualizar_tabla_productos()
                self.actualizar_combos_ventas()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", "Producto no encontrado.")

    def _registrar_usuario(self) -> None:
        identificacion = self.ent_user_id.get().strip()
        nombre = self.ent_user_nombre.get().strip()
        correo = self.ent_user_correo.get().strip()
        rol = self.combo_rol.get()

        if self.servicio.registrar_usuario(identificacion, nombre, correo, rol):
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.actualizar_tabla_usuarios()
            self.actualizar_combos_ventas()
            self._limpiar_formulario_usuarios()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario (ID duplicado o campos vacíos).")

    def _actualizar_usuario(self) -> None:
        identificacion = self.ent_user_id.get().strip()
        nombre = self.ent_user_nombre.get().strip()
        correo = self.ent_user_correo.get().strip()
        rol = self.combo_rol.get()

        if self.servicio.actualizar_usuario(identificacion, nombre, correo, rol):
            messagebox.showinfo("Éxito", "Usuario actualizado con éxito.")
            self.actualizar_tabla_usuarios()
            self.actualizar_combos_ventas()
            self._limpiar_formulario_usuarios()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el usuario.")

    def _eliminar_usuario(self) -> None:
        identificacion = self.ent_user_id.get().strip()
        if not identificacion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")
            return
        if self.usuario_actual and self.usuario_actual.identificacion == identificacion:
            messagebox.showerror("Error", "No puede eliminar la cuenta administrativa actualmente en sesión.")
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar el usuario {identificacion}?"):
            if self.servicio.eliminar_usuario(identificacion):
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self.actualizar_tabla_usuarios()
                self.actualizar_combos_ventas()
                self._limpiar_formulario_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")