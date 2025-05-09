from database.db import db
class Personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.String(25), nullable=False)
    correo = db.Column(db.String(100), nullable=True)
    contacto_emergencia = db.Column(db.String(100), nullable=True)
    enfermedad_cronica = db.Column(db.String(50), nullable=True)
    alergia = db.Column(db.String(50), nullable=True)
    medicamento = db.Column(db.String(50), nullable=True)
    comentarios = db.Column(db.Text, nullable=True)
    tipo_de_sangre = db.Column(db.String(20), nullable=True)
    codigo_qr = db.Column(db.Text, nullable = False)


    