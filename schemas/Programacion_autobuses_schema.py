from pydantic import BaseModel
from typing import Optional

class ProgramacionAutobusesSchema(BaseModel):
    #id_: Optional[int]
    horario_fk: int
    autobus_fk: int