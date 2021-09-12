# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:25:46 2021

@author: jmgar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
from flask import jsonify


## Instanciamos la clase Flask
app = Flask(__name__) #app es la aplicación servidor
       
        
# @app.route('/')
# def hola_mundo():
#     return "Hola mundo"

@app.route('/prueba')
def hola_mundo():
    return "Hola mundo"

@app.route('/json')
def ej_json():
    return jsonify(id = 1, nombre = "Jose", email = "jgarcia111@us.es")

@app.route('/listado_usr')
def ej_json2():

    results =[
        {"id" : 1,
         "nombre": "Jose",
         "email": "jgarcia111@us.es"
            },
        {
        "id" : 2,
        "nombre": "Maria",
        "email" : "maria@us.es"
            }]
    
    return jsonify(results)

@app.route('/parametros/<param>')
def ej_parametros(param):
    return param

if __name__ == '__main__':
    #Inicializamos el servidor
    app.run(debug=True, port=5002) 
    
    

    
    