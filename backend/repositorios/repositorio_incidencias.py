from sqlalchemy import select
from sqlalchemy.orm import Session
from db.models.incidencia import Incidencias
from db.models.usuario import Usuario
from dominio.incidencia_dom import IncidenciaDom
from dominio.usuario_dom import UsuarioDom
from typing import Optional

class RepositorioIncidencias:

    def __init__(self, db: Session):
        self.db = db

    def get_incidencias(self, nombre: Optional[str], tipo: Optional[str]) -> list[IncidenciaDom]:
        query = select(Incidencias)

        if nombre:
            query = query.where(Incidencias.nombre.ilike(f"%{nombre}%"))

        if tipo:
            query = query.where(Incidencias.tipo == tipo)

        query = query.distinct()
        incidencias = list(self.db.execute(query).scalars().all())
        return [self._to_dominio(incidencia) for incidencia in incidencias]

    def save_incidencia(
        self,
        obj: IncidenciaDom
    ) -> IncidenciaDom:
        curr_incidencia = self._to_model(obj)

        self.db.add(curr_incidencia)
        self.db.commit()
        self.db.refresh(curr_incidencia)

        return self._to_dominio(curr_incidencia)

    def delete_incidencia(
        self,
        id: int
    ) -> None:
        query = select(Incidencias).where(Incidencias.id == id)
        curr_incidencia = self.db.execute(query).scalar_one_or_none()
        if curr_incidencia:
            self.db.delete(curr_incidencia)
            self.db.commit()


    def _to_dominio(self, obj: Incidencias) -> IncidenciaDom :
        temp_usuario = UsuarioDom(
            nombre = obj.ciudadano.nombre,
            email = obj.ciudadano.email
        )
        return IncidenciaDom(
            id=obj.id,
            nombre=obj.nombre,
            descripcion=obj.descripcion,
            tipo=obj.tipo,
            fecha_regisro=obj.fecha_registro,
            usuario_data=temp_usuario
        )

    def _to_model(self, obj: IncidenciaDom) -> Incidencias:
        saved_user = self._resolve_usuario(obj.usuario_data)
        return Incidencias(
            nombre=obj.nombre,
            descripcion=obj.descripcion,
            tipo=obj.tipo,
            fecha_registro=obj.fecha_regisro,
            id_ciudadano=saved_user.id
        )

    def _resolve_usuario(self, obj: UsuarioDom) -> Usuario:
        query = select(Usuario).where(Usuario.nombre == obj.nombre, Usuario.email == obj.email).distinct()
        result = self.db.execute(query).scalar_one_or_none()
        if not result:
            result = Usuario(nombre = obj.nombre, email = obj.email)
            self.db.add(result)
            self.db.commit()
            self.db.refresh(result)
        return result
