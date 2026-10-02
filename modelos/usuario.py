class Usuario:

    def __init__(self, identificacion: str, nombre: str, correo: str, rol: str = "Cliente") -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            identificacion=data.get("identificacion", ""),
            nombre=data.get("nombre", ""),
            correo=data.get("correo", ""),
            rol=data.get("rol", "Cliente")
        )