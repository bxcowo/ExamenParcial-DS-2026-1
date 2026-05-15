from dataclasses import dataclass
from datetime import date
from dominio.usuario_dom import UsuarioDom

@dataclass
class IncidenciaDom():
    id: int
    nombre: str
    descripcion: str
    tipo: str
    fecha_regisro: date
    usuario_data: UsuarioDom
