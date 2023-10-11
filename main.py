from fastapi import FastAPI
from model.connection import Connection
from schemas.Autobus_schema import AutobusSchema
from schemas.Cargador_schema import CargadorSchema
from schemas.Horario_schema import HorarioSchema
from schemas.Programacion_autobuses_schema import ProgramacionAutobusesSchema
from schemas.Programacion_cargadores_schema import ProgramacionCargadoresSchema 

app = FastAPI()
conn = Connection()

@app.get("/api")
def root():
    data = conn.read_all()
    return conn.read_all()
    '''
    items = []
        for data in conn.read_all():
            dictionary = {}
            dictionary = {"id_autobus": data[0]}
            dictionary = {"placa": data[1]}
            dictionary = {"marca": data[2]}
            dictionary = {"ruta": data[3]}
            items.append(dictionary)
        return items
    '''
    

#ruta para las crud de autobus
@app.post("/api/autobus")
def insert (Autobus_data:AutobusSchema):
    data = Autobus_data.dict()
    #print(data)
    conn.AutobusWrite(data)

@app.get("/api/autobus")
def read():
    data = conn.read_autobus()
    return conn.read_autobus()

#ruta para las crud de cargador
@app.post("/api/cargador")
def insert (Cargador_data:CargadorSchema):
    data = Cargador_data.dict()
    print(data)
    conn.CargadorWrite(data)

@app.get("/api/cargador")
def read():
    data = conn.read_cargador()
    return conn.read_cargador()

#ruta para las crud de horario
@app.post("/api/horario")
def insert (Horario_data:HorarioSchema):
    data = Horario_data.dict()
    print(data)
    conn.HorarioWrite(data)

@app.get("/api/horario")
def read():
    data = conn.read_horario()
    return conn.read_horario()

#ruta para las crud de prog_autobus
@app.post("/api/prog_autobus")
def insert (ProgAutobus_data:ProgramacionAutobusesSchema):
    data = ProgAutobus_data.dict()
    print(data)
    conn.Programacion_autobusesWrite(data)

@app.get("/api/prog_autobus")
def read():
    data = conn.read_programacion_autobuses()
    return conn.read_programacion_autobuses()

#ruta para las crud de prog_cargador
@app.post("/api/prog_cargador")
def insert (ProgCargador_data:ProgramacionCargadoresSchema):
    data = ProgCargador_data.dict()
    print(data)
    conn.Programacion_cargadoresWrite(data)

@app.get("/api/prog_caragdor")
def read():
    data = conn.read_programacion_cargadores()
    return conn.read_programacion_cargadores()