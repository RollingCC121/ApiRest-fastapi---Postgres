import psycopg
from repositorio.connection import get_conn

conn = get_conn

#conn = psycopg.connect("dbname=examen_03 user=pollito password=daniel12345 host=localhost port=5432")


class HorarioValidator:
    def __init__(self, conn):
        self.conn = conn

    def validar_horario(self, hora_pico, hora_inicio, hora_fin):
        if hora_pico:
            # Validar que ningún cargador esté siendo utilizado en el horario pico
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM cargador WHERE estado = 'ocupado';")
                ocupados = cursor.fetchone()[0]
                if ocupados > 0:
                    return "No se puede declarar el horario pico si hay cargadores ocupados."

            # Validar que todos los autobuses estén en operación en el horario pico
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM autobus WHERE estado != 'operando';")
                no_operando = cursor.fetchone()[0]
                if no_operando > 0:
                    return "No se puede declarar el horario pico si hay autobuses que no están en operación."

        # Si se pasan todas las validaciones, retornar los datos
        return {
            "hora_pico": hora_pico,
            "hora_inicio": hora_inicio,
            "hora_fin": hora_fin
        }

# Uso de la clase
if __name__ == "__main__":
    try:
        conn = psycopg.connect("dbname=examen_03 user=pollito password=daniel12345 host=localhost port=5432")
        validator = HorarioValidator(conn)
        hora_pico = True
        hora_inicio = "05:00:00"
        hora_fin = "09:00:00"
        
        resultado = validator.validar_horario(hora_pico, hora_inicio, hora_fin)
        if isinstance(resultado, str):
            print("Error:", resultado)
        else:
            print("Datos válidos:", resultado)

    except psycopg.OperationalError as err:
        print(err)
    finally:
        conn.close()
