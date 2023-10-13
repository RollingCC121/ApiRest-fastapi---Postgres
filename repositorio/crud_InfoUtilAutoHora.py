import psycopg
from contexto.conexion import Connection


class CrudInfoUtilAutoHora():
    asos = Connection()
    conn = asos.conn

    def read_infoautohora(self):
        
        with self.conn.cursor() as cur:
                data = cur.execute("SELECT  generar_informe_utilizacion_autobuses()")
                return data.fetchall()