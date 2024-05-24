from flask import Flask, render_template, request, redirect, url_for
from models.user import UserModel

app = Flask(__name__)

# Diccionario para almacenar los datos del usuario
datos_usuario = {}

@app.route('/presentacion')
def present():
    return render_template('index.html', presentacion=True)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    global datos_usuario  # Acceder a la variable global

    if request.method == 'POST':
        if 'guardar' in request.form:
            guardar_datos()

    return render_template('formulario.html', datos=datos_usuario, mostrar_datos=bool(datos_usuario))

def guardar_datos():
    global datos_usuario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    profesion = request.form['profesion']
    usuario = UserModel(nombre, apellido, profesion)
    datos_usuario = usuario.viewUserData()  # Almacenar los datos en el diccionario

if __name__ == '__main__':
    app.run(debug=True)

