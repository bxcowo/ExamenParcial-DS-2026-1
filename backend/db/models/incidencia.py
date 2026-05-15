from datetime import date
from sqlalchemy.orm import Mapped,  mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text
from db.core import BaseModel
from db.models.usuario import Usuario
from enum import Enum

class TiposIncidencias(str, Enum):
    BACHES = 'baches'
    ALUMBRADO = 'alumbrado'
    BASURA = 'basura'
    SEGURIDAD = 'seguridad ciudadana'
    EMERGENCIA = 'emergencia'

class Incidencias(BaseModel):
    __tablename__ = "incidencias"

    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(Text)
    tipo: Mapped[TiposIncidencias] = mapped_column(TiposIncidencias.ALUMBRADO)
    fecha_registro: Mapped[date]
    id_ciudadano: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    ciudadano: Mapped['Usuario'] = relationship()
