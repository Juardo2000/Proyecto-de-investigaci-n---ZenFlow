from flask import Flask, render_template, session, redirect, url_for
from dotenv import load_dotenv
import os
from utils.db import get_db_connection

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_secreta_zenflow_2026")

@app.route('/')
def index():
    # Renderiza la página de inicio principal
    return render_template('index.html')

@app.route('/login')
def login():
    # Ruta temporal para simular un inicio de sesión y probar el header dinámico
    session['login'] = 'true'
    session['is_yogui'] = 'true'
    session['nombre'] = 'Juan Rivas'
    return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    # Limpia la sesión para probar el cierre de sesión del script
    session.clear()
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)