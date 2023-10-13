from pydantic import BaseModel
from datetime import time

class InfoUtilCargHora(BaseModel):
    hora: str
    total_cargadores: int
    cargadores_ocupados: int