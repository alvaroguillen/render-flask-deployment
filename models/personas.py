from database.db import db

class Personas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    fecha_nacimiento = db.Column(db.String(20), nullable = False)
    numero_cedula = db.Column(db.String(20), nullable = False)
    grupo_sanguineo = db.Column(db.String(7), nullable = False)
    alergias = db.Column(db.Text, nullable = False)
    enfermedades_cronicas = db.Column(db.Text, nullable = False)
    medicamentos_actuales = db.Column(db.Text, nullable = True)
    contacto_emergencia = db.Column(db.String(15), nullable = False)
    codigo_qr = db.Column(db.Text, nullable = False)