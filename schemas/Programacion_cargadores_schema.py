from pydantic import BaseModel
from typing import Optional

class ProgramacionCargadoresSchema(BaseModel):
    #id_: Optional[int]
    horario_fk: int
    autobus_fk: int