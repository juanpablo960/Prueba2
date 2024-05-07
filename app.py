from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)

#Configuración de la conexion a la  base de datos
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'database': 'pruebas'

}


# Crear la conexión a la base de datos
conn = mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro.html')  # Ruta para el formulario de registro
def registro():
    return render_template('registro.html')

@app.route('/submit_registro', methods=['POST'])
def submit_registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        password = request.form['password']
        
        try:
            # Guardar los datos en la base de datos
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email, telefono, password, direccion) VALUES (%s, %s, %s, %s, %s)", (nombre, email, telefono, password, direccion))
            conn.commit()
            cursor.close()
            
            mensaje = "¡Registro exitoso!"
        except Exception as e:
            mensaje = f"Error al registrar: {str(e)}"
        
        return render_template('mensaje.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)