from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column
from sqlalchemy import Integer
from typing import Annotated

intpk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]

class BaseModel(DeclarativeBase):
    __abstract__ = True

    id: MappedColumn[intpk]
