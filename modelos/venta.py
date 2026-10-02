class Venta:

    def __init__(self, id_venta: str, usuario_identificacion: str, producto_codigo: str, fecha: str) -> None:
        self.id_venta = id_venta
        self.usuario_identificacion = usuario_identificacion
        self.producto_codigo = producto_codigo
        self.fecha = fecha

    def to_dict(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "usuario_identificacion": self.usuario_identificacion,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_venta=data.get("id_venta", ""),
            usuario_identificacion=data.get("usuario_identificacion", ""),
            producto_codigo=data.get("producto_codigo", ""),
            fecha=data.get("fecha", "")
        )