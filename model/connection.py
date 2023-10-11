import psycopg

class Connection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=examen_03 user=pollito password=daniel12345 host=localhost port=5432")

        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def AutobusWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "autobus"(placa,marca,ruta) VALUES(%(placa)s, %(marca)s, %(ruta)s) 
                        """, data)
            self.conn.commit()
    
    def CargadorWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "cargador"(autobus_fk) VALUES(%(autobus_fk)s) 
                        """, data)
            self.conn.commit()

    def HorarioWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "horario"(hora,hora_pico) VALUES(%(hora)s, %(hora_pico)s) 
                        """, data)
            self.conn.commit()

    def Programacion_autobusesWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "programacion_autobuses"(autobus_fk,horario_fk) VALUES(%(autobus_fk)s, %(horario_fk)s) 
                        """, data)
            self.conn.commit()

    def Programacion_cargadoresWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "programacion_cargadores"(autobus_fk,horario_fk) VALUES(%(autobus_fk)s, %(horario_fk)s) 
                        """, data)
            self.conn.commit()

    def __def__(self):
        self.conn.close()
        
