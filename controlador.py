from fastapi import FastAPI
from repositorio.connection import Connection
from modelo.Autobus_schema import AutobusSchema
from modelo.Cargador_schema import CargadorSchema
from modelo.Horario_schema import HorarioSchema
from modelo.Uso_cargador_schema import UsoCargadorBusSchema

app = FastAPI()
conn = Connection()

@app.get("/api")
def root():
    #data = conn.read_all()
    #return conn.read_all()
    return "en linea"
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

@app.get("/api/autobus/{id}")
def det_one(id:int):
    return conn.read_one_autobus(id)

@app.delete("/api/autobus/{id}")
def delete(id:int):
    conn.delete_autobus(id)

@app.put("/api/autobus/{id}")
def update(Autobus_data:AutobusSchema, id:int):
    data = Autobus_data.dict()
    data["id_autobus"] = id
    print(data)
    conn.update_autobus(data)

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

@app.get("/api/cargador/{id}")
def det_one(id:int):
    return conn.read_one_cargador(id)

@app.delete("/api/cargador/{id}")
def delete(id:int):
    conn.delete_cargador(id)

@app.put("/api/cargador/{id}")
def update(Cargador_data:CargadorSchema, id:int):
    data = Cargador_data.dict()
    data["id_cargador"] = id
    print(data)
    conn.update_cargador(data)

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

@app.get("/api/horario/{id}")
def det_one(id:int):
    return conn.read_one_horario(id)

@app.delete("/api/horario/{id}")
def delete(id:int):
    conn.delete_horario(id)

@app.put("/api/horario/{id}")
def update(Horario_data:HorarioSchema, id:int):
    data = Horario_data.dict()
    data["id_horario"] = id
    print(data)
    conn.update_horario(data)

#ruta para las crud de prog_autobus
@app.post("/api/uso_cargador_bus")
def insert (ProgAutobus_data:UsoCargadorBusSchema):
    data = ProgAutobus_data.dict()
    print(data)
    conn.UsoCargadorBusWrite(data)

@app.get("/api/uso_cargador_bus")
def read():
    data = conn.read_uso_cargador_bus()
    return conn.read_uso_cargador_bus()

@app.get("/api/uso_cargador_bus/{id}")
def det_one(id:int):
    return conn.read_one_uso_cargador_bus(id)

@app.delete("/api/uso_cargador_bus/{id}")
def delete(id:int):
    conn.delete_uso_cargador_bus(id)

@app.put("/api/uso_cargador_bus/{id}")
def update(progauto_data:UsoCargadorBusSchema, id:int):
    data = progauto_data.dict()
    data["id_uso_cargador"] = id
    print(data)
    conn.update_uso_cargador_bus(data)

