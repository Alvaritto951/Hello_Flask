from flask import Flask, render_template #De la librería importo la clase (aplicación)

app = Flask(__name__) #__name__ -> Variable que da nombre al fichero. Es una instancia de Flask

@app.route("/hola") #Decorador de app. Función de python que a la funcion primeraentrada la hace accesible desde el servidor
def primeraentrada():
    return "Hola, mundo"


@app.route("/adios")
def ultimaentrada():
    return "Hasta luego, Mari Carmen"

#Se utiliza la variable de entorno FLASK_APP -> set FLASK_APP=hello.py -> dónde voy a encontrar el punto de entrada de mi aplicación
#Se utiliza la variable de entorno FLASK_DEBUG=development (definir entorno en el que estoy trabajando -> Es para que se actualice automáticamente -> set FLASK_DEBUG=True
#Para evitar tener que indicar los dos set FLASK_APP/DEBUG, se utiliza el python_dotenv (pip install) y creo el archivo .env
#Se lanza el comando flask run en el terminal -> flask run

@app.route("/doble/<int:numero>") #Variable se convierte en parámetro de la función. Solo admite cadenas detrás de doble, compatibles con un entero
def doble(numero): #Aquí, numero es el parámetro de la función
    return str(numero * 2)

@app.route("/primerhtml")
def primerhtml():
    return render_template("hola.html")
