from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Ruta del archivo JSON
RUTA_JSON = r"C:\Users\espan\Documentos\Proyecto_SGT\registro.json"

# Cargar registros si existe
if os.path.exists(RUTA_JSON):
    with open(RUTA_JSON, "r") as f:
        dict_reg = json.load(f)
else:
    dict_reg = {}

# Función para guardar un nuevo registro
def guardar_registro(nombre, apellidos, email, user, passw):
    dict_reg[user] = {
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Email": email,
        "User": user,
        "Password": passw
    }
    with open(RUTA_JSON, "w") as f:
        json.dump(dict_reg, f, indent=4)
    print("Registro actualizado:", dict_reg)

# Función para validar ingreso
def ingreso(user, passw):
    if dict_reg.get(user) and dict_reg[user]["Password"] == passw:
        print("Ingreso exitoso")
        return True
    else:
        print("Ingreso fallido")
        return False

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')  # Tu registro.html también incluye ingreso

@app.route('/registro', methods=['GET'])
def mostrar_registro():
    return render_template('registro.html')

# Ruta de registro (POST)
@app.route('/registro', methods=['POST'])
def registro_post():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    user = request.form['username']
    passw = request.form['password']
    
    guardar_registro(nombre, apellidos, email, user, passw)
    return f"Usuario {user} registrado con éxito"

@app.route('/ingreso', methods=['GET'])
def mostrar_ingreso():
    return render_template('ingreso.html')

# Ruta de ingreso (POST)
@app.route('/ingreso', methods=['POST'])
def ingreso_post():
    user = request.form['username']
    passw = request.form['password']
    if ingreso(user, passw):
        return f"Bienvenido {user}"
    else:
        return "Usuario o contraseña incorrectos"

if __name__ == '__main__':
    app.run(debug=True)
