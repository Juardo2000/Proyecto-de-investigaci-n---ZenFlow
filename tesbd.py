import os
import mysql.connector
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def probar_conexion():
    try:
        # Establecer la conexión usando las variables locales
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "zenflowbd"),
            port=int(os.getenv("DB_PORT"))
        )
        
        if conexion.is_connected():
            db_info = conexion.get_server_info()
            print(f"¡Conexión exitosa a la base de datos local de MySQL! Versión del servidor: {db_info}")
            
            # Probar una consulta rápida para verificar la tabla de usuarios
            cursor = conexion.cursor()
            cursor.execute("SHOW TABLES;")
            tablas = cursor.fetchall()
            print("Tablas encontradas en 'zenflowbd':")
            for tabla in tablas:
                print(f" - {tabla[0]}")
                
            cursor.close()
            conexion.close()
            print("Conexión cerrada correctamente.")
            
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    probar_conexion()