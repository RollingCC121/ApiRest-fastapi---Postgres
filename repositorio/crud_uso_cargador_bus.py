import psycopg
from contexto.conexion import Connection


class CrudUsoCargadorBus():
    asos = Connection()
    conn = asos.conn

    def UsoCargadorBusWrite(self,data):
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT insertar_uso_cargador_bus(%(horario_fk)s,%(cargador_fk)s,%(autobus_fk)s);", (data))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error al insertar en la tabla 'uso_cargador_autobus': {e}")
    

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
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                # Utiliza cur.execute para ejecutar una sentencia SQL DELETE
                cur.execute("CALL delete_from_uso_cargador_bus(%(id_uso_cargador_bus)s);", (id))
            conn.commit()
            return {"message": f"Registro de uso_cargador_bus con ID {id} eliminado"}
        except Exception as e:
            return {"error": str(e)}

    def update_uso_cargador_bus(self, data):
        with self.conn.cursor() as cur:
            cur.execute("SELECT actualizar_uso_cargador_bus(%(id_uso_cargador_bus)s,%(horario_fk)s,%(cargador_fk)s,%(autobus_fk)s);", (data))
            self.conn.commit()


    