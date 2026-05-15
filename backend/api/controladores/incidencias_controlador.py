from fastapi import APIRouter, Depends
from api.dto.obtenerIncidenciasRequest import obtenerIncidenciasRequest
from api.dto.obtenerIncidenciasResponse import obtenerIncidenciasResponse
from api.dto.guardarIncidenciaRequest import guardarIncidenciaRequest
from api.dto.guardarIncidenciaResponse import guardarIncidenciaResponse
from api.dto.eliminarIncidenciaRequest import eliminarIncidenciaRequest
from servicios.servicio_incidencias import IncidenciasServicio
from repositorios.export.di import get_incidencias_repositorio

router = APIRouter(
    prefix="/incidencias",
    tags=["incidencias"]
)

def get_incidencias_servicio(repo = Depends(get_incidencias_repositorio)):
    return IncidenciasServicio(repo)

@router.get("/", response_model=list[obtenerIncidenciasResponse])
def obtener_incidencias(
    nombre: str = None,
    tipo: str = None,
    servicio: IncidenciasServicio = Depends(get_incidencias_servicio)
):
    """Obtiene todas las incidencias, opcionalmente filtradas por nombre y/o tipo"""
    request = obtenerIncidenciasRequest(
        nombre=nombre if nombre else None,
        tipo=tipo if tipo else None
    )
    return servicio.get_incidencias(request)

@router.post("/", response_model=guardarIncidenciaResponse)
def guardar_incidencia(
    incidencia: guardarIncidenciaRequest,
    servicio: IncidenciasServicio = Depends(get_incidencias_servicio)
):
    """Guarda una nueva incidencia"""
    return servicio.save_incidencias(incidencia)

@router.delete("/{id}")
def eliminar_incidencia(
    id: int,
    servicio: IncidenciasServicio = Depends(get_incidencias_servicio)
):
    """Elimina una incidencia por ID"""
    request = eliminarIncidenciaRequest(id=id)
    servicio.delete_incidencia(request)
    return {"mensaje": "Incidencia eliminada correctamente"}
