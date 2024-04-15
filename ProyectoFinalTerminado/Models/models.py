# Archivo: models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .database import db

class Alumno(db.Model):
    idAlumno = db.Column(db.Integer, primary_key=True)
    Nombre_completo = db.Column(db.String(100), nullable=False)
    Curp = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    paterno = db.Column(db.String(100), nullable=False)
    materno = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.idNivel'), nullable=False)
    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.idmunicipio'), nullable=False)
    asunto_id = db.Column(db.Integer, db.ForeignKey('asunto.idAsunto'), nullable=False)

class Solicitud(db.Model):
    idSolicitud = db.Column(db.Integer, primary_key=True)
    Turno = db.Column(db.Integer, nullable=False)
    id_municipio = db.Column(db.Integer, db.ForeignKey('municipio.idmunicipio'), nullable=False)
    id_alumno = db.Column(db.Integer, db.ForeignKey('alumno.idAlumno'), nullable=False)
    id_asunto = db.Column(db.Integer, db.ForeignKey('asunto.idAsunto'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.now())
    Proceso = db.Column(db.String(255))

class Nivel(db.Model):
    idNivel = db.Column(db.Integer, primary_key=True)
    NombreNivel = db.Column(db.String(45), nullable=False)

class Municipio(db.Model):
    idmunicipio = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String(100), nullable=False)

class Asunto(db.Model):
    idAsunto = db.Column(db.Integer, primary_key=True)
    NombreAsunto = db.Column(db.String(100), nullable=False)


class Usuario(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True)
    Usuario = db.Column(db.String(100), nullable=False)
    Contraseña = db.Column(db.String(100), nullable=False)
    nombre_completo = db.Column(db.String(100), nullable=False)
    Puesto = db.Column(db.String(45), nullable=False)

    def __init__(self, usuario, contraseña, nombre_completo, puesto):
        self.Usuario = usuario
        self.Contraseña = contraseña
        self.nombre_completo = nombre_completo
        self.Puesto = puesto

    def __repr__(self):
        return f"Usuario('{self.Usuario}', '{self.nombre_completo}', '{self.Puesto}')"


