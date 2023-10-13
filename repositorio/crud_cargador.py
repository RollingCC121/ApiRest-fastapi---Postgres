import psycopg
from contexto.conexion import Connection


class CrudCargador():
    asos = Connection()
    conn = asos.conn

    def CargadorWrite(self,data):
            with self.conn.cursor() as cur:
                cur.execute("""
                        INSERT INTO "cargador"(estado) VALUES(%(estado)s) 
                            """, data)
                self.conn.commit()

    def read_cargador(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "cargador"
                                """)
            return data.fetchall()
        
    def read_one_cargador(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "cargador" WHERE id_cargador = %s
                                """, (id,))
            return data.fetchone()
        
    def delete_cargador(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "cargador" WHERE id_cargador = %s
                        """, (id,))
        self.conn.commit()

    def update_cargador(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "cargador" SET estado = %(estado)s WHERE id_cargador = %(id_cargador)s
                        """, data)
        self.conn.commit()