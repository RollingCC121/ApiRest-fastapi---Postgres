from fastapi import FastAPI
from modelo.Autobus_schema import AutobusSchema
from modelo.Cargador_schema import CargadorSchema
from modelo.Horario_schema import HorarioSchema
from modelo.Uso_cargador_schema import UsoCargadorBusSchema
from contexto.conexion import Connection
from repositorio.crud_autobus import CrudAutobus
from repositorio.crud_cargador import CrudCargador
from repositorio.crud_horario import CrudHorario
from repositorio.crud_uso_cargador_bus import CrudUsoCargadorBus 


app = FastAPI()

crudautobus = CrudAutobus()
crudcargador = CrudCargador()
crudhorario = CrudHorario()
crudcargadorbus = CrudUsoCargadorBus()


#ruta para las crud de autobus
@app.post("/api/autobus")
def insert (Autobus_data:AutobusSchema):
    data = Autobus_data.dict()
    print(data)
    crudautobus.AutobusWrite(data)

@app.get("/api/autobus")
def read():
    data = crudautobus.read_autobus()
    return crudautobus.read_autobus()

@app.get("/api/autobus/{id}")
def det_one(id:int):
    return crudautobus.read_one_autobus(id)

@app.delete("/api/autobus/{id}")
def delete(id:int):
    crudautobus.delete_autobus(id)

@app.put("/api/autobus/{id}")
def update(Autobus_data:AutobusSchema, id:int):
    data = Autobus_data.dict()
    data["id_autobus"] = id
    print(data)
    crudautobus.update_autobus(data)

#ruta para las crud de cargador
@app.post("/api/cargador")
def insert (Cargador_data:CargadorSchema):
    data = Cargador_data.dict()
    print(data)
    crudcargador.CargadorWrite(data)

@app.get("/api/cargador")
def read():
    data = crudcargador.read_cargador()
    return crudcargador.read_cargador()

@app.get("/api/cargador/{id}")
def det_one(id:int):
    return crudcargador.read_one_cargador(id)

@app.delete("/api/cargador/{id}")
def delete(id:int):
    crudcargador.delete_cargador(id)

@app.put("/api/cargador/{id}")
def update(Cargador_data:CargadorSchema, id:int):
    data = Cargador_data.dict()
    data["id_cargador"] = id
    print(data)
    crudcargador.update_cargador(data)

#ruta para las crud de horario
@app.post("/api/horario")
def insert (Horario_data:HorarioSchema):
    data = Horario_data.dict()
    print(data)
    crudhorario.HorarioWrite(data)

@app.get("/api/horario")
def read():
    data = crudhorario.read_horario()
    return crudhorario.read_horario()

@app.get("/api/horario/{id}")
def det_one(id:int):
    return crudhorario.read_one_horario(id)

@app.delete("/api/horario/{id}")
def delete(id:int):
    crudhorario.delete_horario(id)

@app.put("/api/horario/{id}")
def update(Horario_data:HorarioSchema, id:int):
    data = Horario_data.dict()
    data["id_horario"] = id
    print(data)
    crudhorario.update_horario(data)

#ruta para las crud de prog_autobus
@app.post("/api/uso_cargador_bus")
def insert (ProgAutobus_data:UsoCargadorBusSchema):
    data = ProgAutobus_data.dict()
    print(data)
    crudcargadorbus.UsoCargadorBusWrite(data)

@app.get("/api/uso_cargador_bus")
def read():
    data = crudcargadorbus.read_uso_cargador_bus()
    return crudcargadorbus.read_uso_cargador_bus()

@app.get("/api/uso_cargador_bus/{id}")
def det_one(id:int):
    return crudcargadorbus.read_one_uso_cargador_bus(id)

@app.delete("/api/uso_cargador_bus/{id}")
def delete(id:int):
    crudcargadorbus.delete_uso_cargador_bus(id)

@app.put("/api/uso_cargador_bus/{id}")
def update(progauto_data:UsoCargadorBusSchema, id:int):
    data = progauto_data.dict()
    data["id_uso_cargador"] = id
    print(data)
    crudcargadorbus.update_uso_cargador_bus(data)

