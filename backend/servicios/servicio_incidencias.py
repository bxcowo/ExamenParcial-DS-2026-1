from api.dto.obtenerIncidenciasRequest import obtenerIncidenciasRequest
from api.dto.obtenerIncidenciasResponse import obtenerIncidenciasResponse
from api.dto.guardarIncidenciaRequest import guardarIncidenciaRequest
from api.dto.guardarIncidenciaResponse import guardarIncidenciaResponse
from api.dto.eliminarIncidenciaRequest import eliminarIncidenciaRequest
from dominio.incidencia_dom import IncidenciaDom
from dominio.usuario_dom import UsuarioDom
from repositorios.repositorio_incidencias import RepositorioIncidencias

class IncidenciasServicio:
    def __init__(self, incidencias_repositorio: RepositorioIncidencias):
        self.repo = incidencias_repositorio

    def get_incidencias(self, params: obtenerIncidenciasRequest) -> list[obtenerIncidenciasResponse]:
        incidencias = self.repo.get_incidencias(nombre=params.nombre, tipo=params.tipo)
        return [self._to_response(inc) for inc in incidencias]

    def save_incidencias(self, params: guardarIncidenciaRequest) -> guardarIncidenciaResponse:
        curr_usuario = UsuarioDom(
            nombre=params.nombre_usuario,
            email=params.correo_usuario
        )
        curr_incidencia = IncidenciaDom(
            id=0,
            nombre=params.nombre,
            descripcion=params.descripcion,
            tipo=params.tipo,
            fecha_regisro=params.fecha_registro,
            usuario_data=curr_usuario
        )
        result = self.repo.save_incidencia(obj = curr_incidencia)
        return self._to_guardar_response(result)

    def delete_incidencia(self, params: eliminarIncidenciaRequest) -> None:
        self.repo.delete_incidencia(params.id)

    def _to_response(self, incidencia: IncidenciaDom) -> obtenerIncidenciasResponse:
        return obtenerIncidenciasResponse(
            id=incidencia.id,
            nombre=incidencia.nombre,
            descripcion=incidencia.descripcion,
            tipo=incidencia.tipo,
            fecha_registro=incidencia.fecha_regisro,
            nombre_usuario=incidencia.usuario_data.nombre
        )

    def _to_guardar_response(self, incidencia: IncidenciaDom) -> guardarIncidenciaResponse:
        return guardarIncidenciaResponse(
            id=incidencia.id,
            nombre=incidencia.nombre,
            descripcion=incidencia.descripcion,
            tipo=incidencia.tipo,
            fecha_registro=incidencia.fecha_regisro,
            nombre_usuario=incidencia.usuario_data.nombre,
            correo_usuario=incidencia.usuario_data.email
        )
