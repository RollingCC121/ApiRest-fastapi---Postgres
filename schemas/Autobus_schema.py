from pydantic import BaseModel
from typing import Optional

class AutobusSchema(BaseModel):
    #id_autobus: Optional[int]
    placa: str
    marca: str
    ruta: str