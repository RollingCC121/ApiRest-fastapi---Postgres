from app.conexion import conexion

if __name__ == "__main__":
    
    db = conexion()
    session = db.connect_and_get_session()