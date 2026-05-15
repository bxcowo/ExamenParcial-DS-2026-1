from repositorios.repositorio_incidencias import RepositorioIncidencias
from fastapi import Depends
from db.conexion import get_db

def get_incidencias_repositorio(
    db = Depends(get_db)
):
    return RepositorioIncidencias(db)
