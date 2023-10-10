import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class conexion:
    def __init__(self, config_file_path="C:/Users/danie/Documents/tadb_202320_ex03/appsettings.json"):
        self.config_file_path = config_file_path

    def connect_and_get_session(self):
        try:
            # Cargar la configuración desde appsettings.json
            with open(self.config_file_path) as config_file:
                config = json.load(config_file)

            # Crear la cadena de conexión
            db_config = config["DatabaseSettings"]
            db_connection_string = f"postgresql://{db_config['DBUser']}:{db_config['DBPassword']}@{db_config['DBHost']}:{db_config['DBPort']}/{db_config['DBName']}"

            # Crear una instancia del motor SQLAlchemy
            engine = create_engine(db_connection_string)

            # Crear una sesión para interactuar con la base de datos
            Session = sessionmaker(bind=engine)
            session = Session()

            print("Conexión exitosa a la base de datos.")
            return session
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")
            return None

