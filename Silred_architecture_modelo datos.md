# Modelos de Datos Iniciales y Reglas de Negocio Puras

class Recurso:
    def __init__(self, id: str, tipo: str, cantidad: float, ubicacion: dict):
        self.id = id
        self.tipo = tipo
        self.cantidad = cantidad
        self.ubicacion = ubicacion

class Necesidad:
    def __init__(self, id: str, descripcion: str, prioridad: int):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        
