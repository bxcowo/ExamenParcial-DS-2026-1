from db.core import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Usuario(BaseModel):

    __tablename__ = "usuarios"

    nombre: Mapped[str] = mapped_column(String(35))
    email: Mapped[str] = mapped_column(String(40))
