from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    contraseña = db.Column(db.String(150), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre = data['nombre']
    contraseña = data['contraseña']
    usuario = Usuario.query.filter_by(nombre=nombre).first()
    if usuario and check_password_hash(usuario.contraseña, contraseña):
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'mensaje': 'Nombre de usuario o contraseña incorrectos'}), 401

if __name__ == '__main__':
    app.run(port=7500)
