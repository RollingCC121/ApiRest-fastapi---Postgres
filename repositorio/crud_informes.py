import psycopg
from contexto.conexion import Connection


class Informes():
    asos = Connection()
    conn = asos.conn

    def hora_id(self,id):
            with self.conn.cursor() as cur:
                data = cur.execute("CALL generar_informe_por_id(%s)",(id))
                data = cur.fetchall()
            return data
        
    def read_one_autobus(self, id):
        asos = Connection()
        conn = asos.conn
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus" WHERE id_autobus = %s
                                """, (id,))
            return data.fetchone()