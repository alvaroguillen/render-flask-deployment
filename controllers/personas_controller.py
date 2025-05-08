from models.personas import Personas
from database.db import db
from flask import request, redirect, render_template
import qrcode
import io
import base64

#Crea la base de datos la primera vez que se ejecuta, si ya esta creada accede a ella
def obtener_personas():
    persona = Personas.query.all()
    return render_template("index.html", persona = persona)

#Esta funcion se encarga de crear una nuevo registro(persona)
def crear_registro():
    # texto_qr = f"""
    #     nombre = {request.form["nombre"]}
    #     apellido = {request.form["apellido"]}
    #     fecha_nacimiento = {request.form["fecha_nacimiento"]}
    #     numero_cedula = {request.form["numero_cedula"]}
    #     grupo_sanguineo = {request.form["grupo_sanguineo"]}
    #     alergias = {request.form["alergia"]}
    #     enfermedades_cronicas = {request.form["enfermedades_cronicas"]}
    #     medicamentos_actuales = {request.form["medicamentos_actuales"]}
    #     contacto_emergencia = {request.form["contacto_de_emergencia"]}
    # """
    texto_qr = (
    f"Nombre completo: {request.form['nombre']} {request.form['apellido']}\n"
    f"Fecha de nacimiento: {request.form['fecha_nacimiento']}\n"
    f"Número de cédula: {request.form['numero_cedula']}\n"
    f"Grupo sanguíneo: {request.form['grupo_sanguineo']}\n"
    f"Alergias: {request.form['alergia']}\n"
    f"Enfermedades crónicas: {request.form['enfermedades_cronicas']}\n"
    f"Medicamentos actuales: {request.form['medicamentos_actuales']}\n"
    f"Contacto de emergencia: {request.form['contacto_de_emergencia']}")

    imagen_qr = qrcode.make(texto_qr)
    buffer = io.BytesIO()
    imagen_qr.save(buffer, format="PNG")
    buffer.seek(0)
    imagen_base64 =  base64.b64encode(buffer.read()).decode("utf-8")
    codigo_qr = f"data:image/png;base64,{imagen_base64}"

    nuevo_registro_persona = Personas(
        nombre = request.form["nombre"],
        apellido = request.form["apellido"],
        fecha_nacimiento = request.form["fecha_nacimiento"],
        numero_cedula = request.form["numero_cedula"],
        grupo_sanguineo = request.form["grupo_sanguineo"],
        alergias = request.form["alergia"],
        enfermedades_cronicas = request.form["enfermedades_cronicas"],
        medicamentos_actuales = request.form["medicamentos_actuales"],
        contacto_emergencia = request.form["contacto_de_emergencia"],
        codigo_qr = codigo_qr
    )
    db.session.add(nuevo_registro_persona)
    db.session.commit()
    return redirect("/")

#Esta funcion se encarga de eliminar una tarea
def eliminar_registro(id):
    persona = Personas.query.filter_by(id = id).first()
    db.session.delete(persona)
    db.session.commit()
    return redirect("/")