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
                    INSERT INTO "autobus"(estado) VALUES(%(estado)s) 
                        """, data)
            self.conn.commit()
    
    def CargadorWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "cargador"(estado) VALUES(%(estado)s) 
                        """, data)
            self.conn.commit()

    def HorarioWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "horario"(hora_pico,hora_inicio,hora_fin) VALUES(%(hora_pico)s, %(hora_inicio)s, %(hora_fin)s) 
                        """, data)
            self.conn.commit()

    def UsoCargadorBusWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "uso_cargador_bus"(horario_fk, cargador_fk, autobus_fk) VALUES(%(horario_fk)s, %(cargador_fk)s, %(autobus_fk)s) 
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
    
    def read_uso_cargador_bus(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "uso_cargador_bus"
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
        
    def read_one_uso_cargador_bus(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "uso_cargador_bus" WHERE id_uso_cargador_bus = %s
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

    def delete_uso_cargador_bus(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "uso_cargador_bus" WHERE id_uso_cargador_bus = %s
                        """, (id,))
        self.conn.commit()
    

    def update_autobus(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "autobus" SET estado = %(estado)s WHERE id_autobus = %(id_autobus)s
                        """, data)
        self.conn.commit()

    def update_cargador(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "cargador" SET estado = %(estado)s WHERE id_cargador = %(id_cargador)s
                        """, data)
        self.conn.commit()

    def update_horario(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "horario" SET hora_pico = %(hora_pico)s, hora_inicio = %(hora_inicio)s, hora_fin = %(hora_fin)s WHERE id_horario = %(id_horario)s
                        """, data)
        self.conn.commit()

    def update_uso_cargador_bus(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "uso_cargador_bus" SET horario_fk = %(horario_fk)s, cargador_fk = %(cargador_fk)s, autobus_fk = %(autobus_fk)s WHERE id_uso_cargador_bus = %(id_uso_cargador_bus)s
                        """, data)
        self.conn.commit()

    def __def__(self):
        self.conn.close()
        
