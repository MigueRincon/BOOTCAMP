from flask import Flask,

app = Flask(__name__)  #1. Crear la aplicacion

@app.route('/') #1. Definir un endpoint en la ruta "/"
def inicio(): #3. Funcion que maneja esa ruta
    return '¡Hola, mundo!' #4. Lo que devuelve

if __name__ == '__main__':
    app.run(debug=True) #5. encender el servidor


from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: ruta raiz
@app.route('/')
def inicio():
    return jsonify({ 'mensaje': 'API funcionando' })

# Endpoint 2: lista de usuarios
@app.route('/usuarios')
def obtener_usuarios():
    usuarios = [
        { 'id':1, 'nombre': 'Ana' },
        { 'id':2, 'nombre': 'Luis' },
    ]
    return jsonify(usuarios)

# Endpoint 3: un usuario por ID (Parametro dinamico)
@app.route('/usuarios/<int:id>')
def obtener_usuario(id):
    return jsonify({ 'id': id, 'nombre': 'Ana' })

@app.route('/productos')
def listar_productos(): # Este es el controlador
    
    #1. obtener datos (simulando base de datos)
    productos = [
        { 'id': 1, 'nombre': 'Laptop', 'precio': 999.99 },
        { 'id': 2, 'nombre': 'Smartphone', 'precio': 499.99 },
    ]
    #2. preparar y retornar la respuesta
    return jsonify(productos)