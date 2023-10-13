import psycopg
from contexto.conexion import Connection


class CrudHorario():
    asos = Connection()
    conn = asos.conn   

    def HorarioWrite(self,data):
                with self.conn.cursor() as cur:
                    cur.execute("""
                            INSERT INTO "horario"(hora_pico,hora_inicio,hora_fin) VALUES(%(hora_pico)s, %(hora_inicio)s, %(hora_fin)s) 
                                """, data)
                    self.conn.commit()

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
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "horario" WHERE id_horario = %s
                        """, (id,))
        self.conn.commit()

    def update_horario(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "horario" SET hora_pico = %(hora_pico)s, hora_inicio = %(hora_inicio)s, hora_fin = %(hora_fin)s WHERE id_horario = %(id_horario)s
                        """, data)
        self.conn.commit()