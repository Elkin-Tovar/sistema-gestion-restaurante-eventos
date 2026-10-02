import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self) -> None:
        self.ruta_datos = "datos"
        os.makedirs(self.ruta_datos, exist_ok=True)
        self.archivo_productos = os.path.join(self.ruta_datos, "productos.json")
        self.archivo_usuarios = os.path.join(self.ruta_datos, "usuarios.json")
        self.archivo_ventas = os.path.join(self.ruta_datos, "ventas.json")
        self._inicializar_usuarios_por_defecto()

    def _inicializar_usuarios_por_defecto(self) -> None:
        if not os.path.exists(self.archivo_usuarios):
            usuarios_iniciales = [
                Usuario("ADM-001", "Elkin Tovar", "elkin@restaurante.com", "Administrador"),
                Usuario("EMP-001", "Ana Pérez", "ana@restaurante.com", "Empleado"),
                Usuario("CLI-001", "Carlos Gómez", "carlos@gmail.com", "Cliente")
            ]
            self.guardar_usuarios(usuarios_iniciales)

    def cargar_productos(self) -> List[Producto]:
        if not os.path.exists(self.archivo_productos):
            return []
        try:
            with open(self.archivo_productos, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Producto.from_dict(p) for p in data]
        except Exception:
            return []

    def guardar_productos(self, productos: List[Producto]) -> None:
        try:
            with open(self.archivo_productos, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in productos], f, indent=4, ensure_ascii=False)
        except Exception:
            pass

    def cargar_usuarios(self) -> List[Usuario]:
        if not os.path.exists(self.archivo_usuarios):
            return []
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Usuario.from_dict(u) for u in data]
        except Exception:
            return []

    def guardar_usuarios(self, usuarios: List[Usuario]) -> None:
        try:
            with open(self.archivo_usuarios, "w", encoding="utf-8") as f:
                json.dump([u.to_dict() for u in usuarios], f, indent=4, ensure_ascii=False)
        except Exception:
            pass

    def cargar_ventas(self) -> List[Venta]:
        if not os.path.exists(self.archivo_ventas):
            return []
        try:
            with open(self.archivo_ventas, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Venta.from_dict(v) for v in data]
        except Exception:
            return []

    def guardar_ventas(self, ventas: List[Venta]) -> None:
        try:
            with open(self.archivo_ventas, "w", encoding="utf-8") as f:
                json.dump([v.to_dict() for v in ventas], f, indent=4, ensure_ascii=False)
        except Exception:
            pass