from contexto.conexion import Connection
from fastapi import HTTPException
from datetime import datetime,time
from contexto.conexion import Connection  
from modelo.Horario_schema import HorarioSchema

class ServicioHorario:
    def __init__(self):
        self.asos = Connection()
        self.conn = self.asos.conn

    def validar_horario_pico(self, data: HorarioSchema):
        hora_pico = data.hora_pico
        hora_inicio = time(data.hora_inicio)
        hora_fin = time(data.hora_fin)

        # Verificar si estamos en horario pico (entre hora_inicio y hora_fin)
        es_horario_pico = (
            (hora_inicio >= datetime.strptime("05:00:00", "%H:%M:%S").time() and
             hora_fin <= datetime.strptime("09:00:00", "%H:%M:%S").time()) or
            (hora_inicio >= datetime.strptime("16:00:00", "%H:%M:%S").time() and
             hora_fin <= datetime.strptime("20:00:00", "%H:%M:%S").time())
        )

        if es_horario_pico:
            try:
                # Verificar que ningún cargador esté siendo utilizado
                with self.conn.cursor() as cur:
                    cur.execute("SELECT * FROM obtener_cargadores_en_uso();")
                    cargadores_en_uso = cur.fetchall()

                if cargadores_en_uso:
                    raise HTTPException(status_code=400, detail="No se puede utilizar un cargador en horario pico.")

                # Verificar que todos los autobuses estén en operación
                with self.conn.cursor() as cur:
                    cur.execute("SELECT * FROM obtener_autobuses_cargando_o_parqueados();")
                    autobuses_fuera_de_servicio = cur.fetchall()

                if autobuses_fuera_de_servicio:
                    raise HTTPException(status_code=400, detail="Todos los autobuses deben estar en operación en horario pico.")
                
                # Si todas las validaciones son exitosas, retornar los datos en su formato original (HorarioSchema)
                return data
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))


