from fastapi import FastAPI
from model.connection import Connection
from schemas.Autobus_schema import AutobusSchema
from schemas.Cargador_schema import CargadorSchema
from schemas.Horario_schema import HorarioSchema
from schemas.Programacion_autobuses_schema import ProgramacionAutobusesSchema
from schemas.Programacion_cargadores_schema import ProgramacionCargadoresSchema 

app = FastAPI()
conn = Connection()

@app.get("/")
def root():
    conn
    return "en linea" 

#ruta para las crud de autobus
@app.post("/api/autobus")
def insert (Autobus_data:AutobusSchema):
    data = Autobus_data.dict()
    #print(data)
    conn.AutobusWrite(data)

#ruta para las crud de cargador
@app.post("/api/cargador")
def insert (Cargador_data:CargadorSchema):
    data = Cargador_data.dict()
    print(data)
    conn.CargadorWrite(data)

#ruta para las crud de horario
@app.post("/api/horario")
def insert (Horario_data:HorarioSchema):
    data = Horario_data.dict()
    print(data)
    conn.HorarioWrite(data)

#ruta para las crud de prog_autobus
@app.post("/api/prog_autobus")
def insert (ProgAutobus_data:ProgramacionAutobusesSchema):
    data = ProgAutobus_data.dict()
    print(data)
    conn.Programacion_autobusesWrite(data)

#ruta para las crud de prog_cargador
@app.post("/api/prog_cargador")
def insert (ProgCargador_data:ProgramacionCargadoresSchema):
    data = ProgCargador_data.dict()
    print(data)
    conn.Programacion_cargadoresWrite(data)