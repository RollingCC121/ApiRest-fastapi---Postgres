import psycopg
from contexto.conexion import Connection


class CrudHorario():
    asos = Connection()
    conn = asos.conn   

    def HorarioWrite(self,data):
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT insertar_horario(%(hora_pico)s,%(hora_inicio)s,%(hora_fin)s);", (data))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error al insertar en la tabla 'horario': {e}")
    

    def read_horario(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "horario"
                                """)
            return data.fetchall()
        
    def read_one_horario(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                    SELECT * FROM "horario" WHERE id_horario = %s
                                """, (id,))
            return data.fetchone()
        
    def delete_horario(self, id):
        asos = Connection()
        conn = asos.conn
        try:
            with conn.cursor() as cur:
                # Utiliza cur.execute para ejecutar una sentencia SQL DELETE
                cur.execute("CALL delete_from_horario(%(id_horario)s);", (id))
            conn.commit()
            return {"message": f"Registro de horario con ID {id} eliminado"}
        except Exception as e:
            return {"error": str(e)}

    def update_horario(self, data):
        with self.conn.cursor() as cur:
            cur.execute("SELECT actualizar_horario(%(id_horario)s,%(hora_pico)s,%(hora_inicio)s,%(hora_fin)s);", (data))#{'id_autobus':data,'estado': data})
            self.conn.commit()