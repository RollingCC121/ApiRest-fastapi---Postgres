from pydantic import BaseModel
from typing import Optional

class CargadorSchema(BaseModel):
    #id_cargador: Optional[int]
    autobus_fk: int