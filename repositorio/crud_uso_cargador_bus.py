import psycopg
from contexto.conexion import Connection


class CrudUsoCargadorBus():
    asos = Connection()
    conn = asos.conn

    def UsoCargadorBusWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "uso_cargador_bus"(horario_fk, cargador_fk, autobus_fk) VALUES(%(horario_fk)s, %(cargador_fk)s, %(autobus_fk)s) 
                        """, data)
            self.conn.commit()

    def read_uso_cargador_bus(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "uso_cargador_bus"
                               """)
            return data.fetchall()
        
    def read_one_uso_cargador_bus(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "uso_cargador_bus" WHERE id_uso_cargador_bus = %s
                                """, (id,))
            return data.fetchone()
        
    def delete_uso_cargador_bus(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "uso_cargador_bus" WHERE id_uso_cargador_bus = %s
                        """, (id,))
        self.conn.commit()

    def update_uso_cargador_bus(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "uso_cargador_bus" SET horario_fk = %(horario_fk)s, cargador_fk = %(cargador_fk)s, autobus_fk = %(autobus_fk)s WHERE id_uso_cargador_bus = %(id_uso_cargador_bus)s
                        """, data)
        self.conn.commit()


    