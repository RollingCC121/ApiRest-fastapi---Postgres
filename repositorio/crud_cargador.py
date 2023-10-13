import psycopg
from contexto.conexion import Connection


class CrudCargador():
    asos = Connection()
    conn = asos.conn

    def CargadorWrite(self,data):
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT insertar_cargador(%(estado)s);", {'estado': data})
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error al insertar en la tabla 'cargador': {e}")
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
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                # Utiliza cur.execute para ejecutar una sentencia SQL DELETE
                cur.execute("CALL delete_from_cargador(%(id_cargador)s);", (id))
            conn.commit()
            return {"message": f"Registro de cargador con ID {id} eliminado"}
        except Exception as e:
            return {"error": str(e)}

    def update_cargador(self, data):
        with self.conn.cursor() as cur:
            cur.execute("SELECT actualizar_cargador(%(id_cargador)s,%(estado)s);", (data))#{'id_autobus':data,'estado': data})
            self.conn.commit()