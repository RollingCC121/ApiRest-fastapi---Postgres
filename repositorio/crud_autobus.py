import psycopg
from contexto.conexion import Connection


class CrudAutobus():
    asos = Connection()
    conn = asos.conn

    def AutobusWrite(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO "autobus"(estado) VALUES(%(estado)s) 
                        """, data)
            self.conn.commit()
    
    def read_autobus(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus"
                                """)
            return data.fetchall()
        
    def read_one_autobus(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus" WHERE id_autobus = %s
                                """, (id,))
            return data.fetchone()
    
    def delete_autobus(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "autobus" WHERE id_autobus = %s
                        """, (id,))
        self.conn.commit()
    
    def update_autobus(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "autobus" SET estado = %(estado)s WHERE id_autobus = %(id_autobus)s
                        """, data)
        self.conn.commit()
