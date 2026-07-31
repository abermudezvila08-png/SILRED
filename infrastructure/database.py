# Capa de Infraestructura - Conexión de Base de Datos PostgreSQL

class ConexionBaseDatos:
    def __init__(self, url_conexion: str):
        self.url = url_conexion
        self.conectado = False

    def conectar(self):
        # Configuración física del motor de datos
        self.conectado = True
        return "Conexión establecida con PostgreSQL"
