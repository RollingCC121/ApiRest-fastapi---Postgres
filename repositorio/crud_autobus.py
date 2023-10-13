import psycopg
from contexto.conexion import Connection


class CrudAutobus():
    asos = Connection()
    conn = asos.conn

    def AutobusWrite(self,data):
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT insertar_autobus(%(estado)s);", {'estado': data})
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error al insertar en la tabla 'autobus': {e}")
    
    def read_autobus(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus"
                                """)
            return data.fetchall()
        
    def read_one_autobus(self, id):
        asos = Connection()
        conn = asos.conn
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "autobus" WHERE id_autobus = %s
                                """, (id,))
            return data.fetchone()
    
    def delete_autobus(self, id):
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                # Utiliza cur.execute para ejecutar una sentencia SQL DELETE
                cur.execute("CALL delete_from_autobus(%(id_autobus)s);", (id))
            conn.commit()
            return {"message": f"Registro de autobus con ID {id} eliminado"}
        except Exception as e:
            return {"error": str(e)}
    
    def update_autobus(self, data):
        with self.conn.cursor() as cur:
            cur.execute("SELECT actualizar_autobus(%(id_autobus)s,%(estado)s);", (data))#{'id_autobus':data,'estado': data})
            self.conn.commit()
