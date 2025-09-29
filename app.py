from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail (CAMBIÁ ESTO)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'clubunidosmtb@gmail.com'     # ← TU EMAIL DEL CLUB
app.config['MAIL_PASSWORD'] = 'pemakbierxxkqecw'         # ← APP PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = 'clubunidosmtb@gmail.com'

app.secret_key = 'clave_secreta_para_flash'

mail = Mail(app)

info_evento = {
    1: {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades: 30km (corta) y 80km (larga).",
        "fecha": "24 de Octubre de 2025",
        "horario": "8:00 AM",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB rural",
        "modalidad_costo": {
            1: {"nombre": "Corta", "valor": "100"},
            2: {"nombre": "Larga", "valor": "200"}
        },
        "Auspiciantes": {
            "Manaos": "manaos.png",
            "Trek Bikes": "trek_bikes.png",
            "Red Bull": "red_bull.png",
            "Decathlon": "decathlon.png"
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html', evento=info_evento[1])

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        modalidad = request.form.get('modalidad')

        msg = Message(
            subject="Nueva Inscripción - Rally MTB 2025",
            recipients=[app.config['MAIL_USERNAME']],
            body=f"""
            Nueva inscripción recibida:

            Nombre: {nombre}
            Email: {email}
            Teléfono: {telefono}
            Modalidad: {modalidad}
            """
        )
        try:
            mail.send(msg)
            flash("¡Inscripción enviada con éxito! Pronto nos contactaremos contigo.", "success")
        except Exception as e:
            flash("Error al enviar la inscripción. Inténtalo más tarde.", "error")
            print(e)

        return redirect(url_for('registration'))

    return render_template('registration.html', evento=info_evento[1])

if __name__ == '__main__':
    app.run(debug=True)