from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

list_administradores = ["pedrito@gmail.com", "maria@gmail.com"]
list_usuarios = ["juanito@hotmail.com", "paola@hotmail.com"]
@app.route("/", methods=['GET', 'POST'])
def inicio():
    return render_template('login_register.html')

@app.route("/buscar-habitacion", methods=['GET', 'POST'])
def login():
    return render_template('buscar_habitacion.html')

@app.route("/inicio-admin", methods=['GET'])
def inicio_admin():
    return render_template('editar_habitacion.html')

@app.route("/inicio/<No_Habitacion>", methods=['GET'])
def habitacion(No_Habitacion):
    return f"Detalles habitación {No_Habitacion} seleccionada por el usuario"

@app.route("/inicio/contactanos", methods=['GET'])
def contactanos():
    return "Información de canales de comunicación"

if __name__ == "__main__":
    app.run(debug=True)