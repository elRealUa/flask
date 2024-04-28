import string
from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

@app.route("/")
def texto():
    return '<h1>Hola.</h1><h2>intenta añadir esto a la url para otra parte de la web:</h2><h2>/randomFact</h2><h2>/coin</h2><h2>/passwordGenerator</h2>'

@app.route("/randomFact")
def facts():
    return f'<h1>{random.choice(facts_list)}</h1>'

@app.route("/coin")
def coin():
    randomC = ['si', 'no']
    choose = random.choice(randomC)
    if choose == 'si':
        return f'<h1>Cara</h1>'
    else:
        return f'<h1>Cruz</h1>'
    
@app.route("/passwordGenerator")
def password():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(10):
        contrasena += random.choice(caracteres)
    return f'<h1>La contraseña generada es: {contrasena}</h1>'

app.run(debug=True)