from datetime import date
from pydantic import BaseModel

class guardarIncidenciaRequest(BaseModel):
    nombre: str
    descripcion: str
    tipo: str
    fecha_registro: date
    nombre_usuario: str
    correo_usuario: str
