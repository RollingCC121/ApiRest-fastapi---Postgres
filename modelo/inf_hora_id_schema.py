from pydantic import BaseModel
from datetime import time

class InformeHoraId(BaseModel):
    id_horario: int
    hora_pico: str
    hora_inicio: time
    hora_fin: time
