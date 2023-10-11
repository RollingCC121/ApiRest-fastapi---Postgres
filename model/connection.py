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

    def read_autobus(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus"
                                """)
            return data.fetchall()
    
    def read_cargador(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "cargador"
                                """)
            return data.fetchall()
    
    def read_horario(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "horario"
                                """)
            return data.fetchall()
    
    def read_programacion_autobuses(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "programacion_autobuses"
                               """)
            return data.fetchall()
    
    def read_programacion_cargadores(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "programacion_cargadores"
                                """)
            return data.fetchall()
    
    def read_one_autobus(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus" WHERE id_autobus = %s
                                """, (id,))
            return data.fetchone()
        
    def read_one_cargador(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "cargador" WHERE id_cargador = %s
                                """, (id,))
            return data.fetchone()
        
    def read_one_horario(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "horario" WHERE id_horario = %s
                                """, (id,))
            return data.fetchone()
        
    def read_one_prog_autobus(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "programacion_autobuses" WHERE id_programacion_autobuses = %s
                                """, (id,))
            return data.fetchone()
        
    def read_one_prog_cargador(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "programacion_cargadores" WHERE id_programacion_cargadores = %s
                                """, (id,))
            return data.fetchone()

    def delete_autobus(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "autobus" WHERE id_autobus = %s
                        """, (id,))
        self.conn.commit()

    def delete_cargador(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "cargador" WHERE id_cargador = %s
                        """, (id,))
        self.conn.commit()

    def delete_horario(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "horario" WHERE id_horario = %s
                        """, (id,))
        self.conn.commit()

    def delete_prog_autobus(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "programacion_autobuses" WHERE id_programacion_autobuses = %s
                        """, (id,))
        self.conn.commit()
    
    def delete_prog_cargador(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "programacion_cargadores" WHERE id_programacion_cargadores = %s
                        """, (id,))
        self.conn.commit()



    def __def__(self):
        self.conn.close()
        
