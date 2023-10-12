from pydantic import BaseModel
from typing import Optional

class UsoCargadorBusSchema(BaseModel):
    #id_uso_cargador: Optional[int]
    horario_fk: int
    cargador_fk: int
    autobus_fk: int