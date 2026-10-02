class Producto:

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            codigo=data.get("codigo", ""),
            nombre=data.get("nombre", ""),
            categoria=data.get("categoria", ""),
            precio=float(data.get("precio", 0.0)),
            stock=int(data.get("stock", 0))
        )