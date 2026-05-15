from pydantic import BaseModel
from typing import Optional

class obtenerIncidenciasRequest(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
