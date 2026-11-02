from flask import Flask, render_template, session, redirect, url_for, request, flash
from dotenv import load_dotenv
import os
from utils.db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_secreta_zenflow_2026")

@app.route('/')
def index():
    # Renderiza la página de inicio principal
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action_type = request.form.get('action_type')
        correo = request.form.get('correo')
        password = request.form.get('password')
        
        conexion = get_db_connection()
        if not conexion:
            flash("Error de conexión con la base de datos", "danger")
            return redirect(url_for('login'))
        
        cursor = conexion.cursor(dictionary=True)
        
        # CASO 1: REGISTRO DE NUEVO USUARIO
        if action_type == 'register':
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            cedula = request.form.get('cedula')
            telefono = request.form.get('telefono')
            
            # Verificar si el correo o la cédula ya existen
            cursor.execute("SELECT * FROM usuarios WHERE correo = %s OR cedula = %s", (correo, cedula))
            usuario_existente = cursor.fetchone()
            
            if usuario_existente:
                flash("El correo o la cédula ya se encuentran registrados.", "danger")
                cursor.close()
                conexion.close()
                return redirect(url_for('login'))
            
            # Hashear contraseña
            password_hash = generate_password_hash(password)
            
            # Insertar nuevo usuario con todos los campos nuevos
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellido, cedula, telefono, correo, password, rol) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (nombre, apellido, cedula, telefono, correo, password_hash, 'yogui')
            )
            conexion.commit()
            
            flash("¡Registro exitoso! Se ha simulado el envío del correo de verificación.", "success")
            cursor.close()
            conexion.close()
            return redirect(url_for('login'))
        
        # CASO 2: INICIO DE SESIÓN
        elif action_type == 'login':
            cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
            usuario = cursor.fetchone()
            
            # Validación de credenciales
            if usuario and check_password_hash(usuario['password'], password):
                session['login'] = 'true'
                session['nombre'] = usuario['nombre']
                
                # Diferenciar roles según tu base de datos
                rol = usuario.get('rol', 'yogui')
                session['is_yogui'] = 'true' if rol == 'yogui' else 'false'
                session['is_instructor'] = 'true' if rol == 'instructor' else 'false'
                session['is_admin'] = 'true' if rol == 'admin' else 'false'
                
                flash(f"¡Bienvenido de nuevo, {usuario['nombre']}!", "success")
                cursor.close()
                conexion.close()
                return redirect(url_for('index'))
            else:
                flash("Correo o contraseña incorrectos.", "danger")
                cursor.close()
                conexion.close()
                return redirect(url_for('login'))

    # Método GET: Muestra la vista de login/registro
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    # Limpia la sesión para probar el cierre de sesión del script
    session.clear()
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)