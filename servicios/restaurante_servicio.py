from datetime import datetime
from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: List[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: List[Usuario] = self.archivo_servicio.cargar_usuarios()
        self.ventas: List[Venta] = self.archivo_servicio.cargar_ventas()

    def validar_acceso(self, usuario_correo: str, clave: str) -> Optional[Usuario]:
        if not usuario_correo.strip() or not clave.strip():
            return None
        
        if usuario_correo.strip().lower() == "admin" and clave == "1234":
            return Usuario("ADMIN-01", "Administrador General", "admin", "Administrador")

        for u in self.usuarios:
            if u.correo.strip().lower() == usuario_correo.strip().lower():
                if clave == "123456" or clave == u.identificacion.strip():
                    return u
                
        return None

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def obtener_ventas(self) -> List[Venta]:
        return self.ventas

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        if not codigo.strip() or not nombre.strip():
            return False
        if self.buscar_producto(codigo) is not None:
            return False
        if precio < 0 or stock < 0:
            return False
            
        nuevo_producto = Producto(codigo, nombre, categoria, precio, stock)
        self.productos.append(nuevo_producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        if precio < 0 or stock < 0:
            return False
            
        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
            
        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def registrar_usuario(self, identificacion: str, nombre: str, correo: str, rol: str) -> bool:
        if not identificacion.strip() or not nombre.strip() or not correo.strip():
            return False
        if self.buscar_usuario(identificacion) is not None:
            return False
            
        nuevo_usuario = Usuario(identificacion, nombre, correo, rol)
        self.usuarios.append(nuevo_usuario)
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True

    def actualizar_usuario(self, identificacion: str, nombre: str, correo: str, rol: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
            
        usuario.nombre = nombre
        usuario.correo = correo
        usuario.rol = rol
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
            
        self.usuarios.remove(usuario)
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True

    def registrar_venta(self, usuario_id: str, producto_codigo: str) -> bool:
        if not usuario_id or not producto_codigo:
            return False
            
        producto_encontrado = self.buscar_producto(producto_codigo)
        if producto_encontrado is None:
            return False

        id_venta = f"V-{int(datetime.now().timestamp())}"
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_venta = Venta(id_venta, usuario_id, producto_codigo, fecha_actual)
        self.ventas.append(nueva_venta)
        self.archivo_servicio.guardar_ventas(self.ventas)
        return True