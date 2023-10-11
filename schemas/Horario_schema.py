from pydantic import BaseModel
from typing import Optional
from datetime import time

class HorarioSchema(BaseModel):
    #id_horario: Optional[int]
    hora: time
    hora_pico: str
    