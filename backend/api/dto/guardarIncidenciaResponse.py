from datetime import date
from pydantic import BaseModel

class guardarIncidenciaResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    tipo: str
    fecha_registro: date
    nombre_usuario: str
    correo_usuario: str
