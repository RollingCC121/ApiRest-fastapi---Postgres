from pydantic import BaseModel
from typing import Optional
from datetime import time,date

class HorarioSchema(BaseModel):
    #id_horario: Optional[int]
    hora_pico: str
    hora_inicio: time
    hora_fin: time
    
    