from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    contraseña = db.Column(db.String(150), nullable=False)

with app.app_context():
    db.drop_all()  
    db.create_all() 
    
    usuarios = [
        {"nombre": "yuver carreño", "contraseña": generate_password_hash("password1")},
        {"nombre": "sebastian contreras", "contraseña": generate_password_hash("password2")},
        {"nombre": "pablo gallegos", "contraseña": generate_password_hash("password3")},
        {"nombre": "daniel rojas", "contraseña": generate_password_hash("password4")}
    ]
    for user in usuarios:
        nuevo_usuario = Usuario(nombre=user["nombre"], contraseña=user["contraseña"])
        db.session.add(nuevo_usuario)
    db.session.commit()
    print("Base de datos creada y usuarios insertados con éxito.")
