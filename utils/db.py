import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            # Parámetros estrictos para manejar SSL en Aiven de forma local:
            ssl_disabled=False,
            ssl_verify_cert=False # Evita que falle si tu PC no tiene instalado el certificado raíz de Aiven
        )
        
        if connection.is_connected():
            return connection
            
    except Error as e:
        print(f"❌ Error al conectar con SSL: {e}")
        return None