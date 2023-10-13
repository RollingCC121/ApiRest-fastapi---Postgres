import psycopg
from contexto.conexion import Connection


class CrudInfoUtilCargHora():
    asos = Connection()
    conn = asos.conn

    def read_infocarghora(self):
        
        with self.conn.cursor() as cur:
                data = cur.execute("SELECT  informe_utilizacion_cargadores_por_hora()")
                return data.fetchall()