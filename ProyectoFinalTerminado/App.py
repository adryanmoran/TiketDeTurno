from flask import Flask, render_template, request, redirect, url_for, session, make_response,jsonify
from io import BytesIO
from PIL import Image
import qrcode
from Models.models import Alumno, Solicitud, Nivel, Municipio, Asunto,Usuario
from Models.database import DBSingleton, db
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from sqlalchemy import func 

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
db_singleton = DBSingleton(app)
db = db_singleton.db

@app.route('/')
def inicio():
    return render_template('menu.html')

@app.route('/registrar_alumno', methods=['POST'])
def registrar_alumno():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        curp = request.form['curp']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        telefono = request.form['telefono']
        celular = request.form['celular']
        correo = request.form['correo']
        nivel_id = request.form['nivel_id']
        municipio_id = request.form['municipio_id']
        asunto_id = request.form['asunto_id']

        alumno = Alumno(Nombre_completo=nombre_completo, Curp=curp, nombre=nombre, paterno=paterno, materno=materno, telefono=telefono, celular=celular, correo=correo, nivel_id=nivel_id, municipio_id=municipio_id, asunto_id=asunto_id)
        db.session.add(alumno)
        db.session.flush()

        max_turno = db.session.query(db.func.max(Solicitud.Turno)).filter(Solicitud.id_municipio == municipio_id).scalar() or 0
        nuevo_turno = max_turno + 1

        solicitud = Solicitud(Turno=nuevo_turno, id_municipio=municipio_id, id_alumno=alumno.idAlumno, id_asunto=asunto_id, Proceso='Pendiente')
        db.session.add(solicitud)
        db.session.commit()

        return redirect(url_for('registro_alumno_view'))

@app.route('/registro_alumno_view')
def registro_alumno_view():
    niveles = Nivel.query.all()
    municipios = Municipio.query.all()
    asuntos = Asunto.query.all()
    return render_template('registro_alumno_view.html', niveles=niveles, municipios=municipios, asuntos=asuntos)

@app.route('/buscar_alumno', methods=['GET', 'POST'])
def buscar_alumno():
    if request.method == 'POST':
        curp_buscar = request.form['curp_buscar']
        alumno = Alumno.query.filter_by(Curp=curp_buscar).first()
        if alumno:
            solicitud = Solicitud.query.filter_by(id_alumno=alumno.idAlumno).first()
            if solicitud:
                return render_template('detalle_alumno.html', alumno=alumno, solicitud=solicitud)
            else:
                return render_template('sin_solicitud.html', alumno=alumno)
        else:
            return render_template('alumno_no_encontrado.html')
    return render_template('buscar_alumno.html')

@app.route('/generar_comprobante/<int:id_solicitud>', methods=['GET'])
def generar_comprobante(id_solicitud):
    solicitud = Solicitud.query.get_or_404(id_solicitud)
    alumno = Alumno.query.get_or_404(solicitud.id_alumno)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(alumno.Curp)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.drawString(100, 750, 'Comprobante de Solicitud')
    pdf.drawString(100, 730, f'Turno de Solicitud: {solicitud.Turno}')
    pdf.drawString(100, 710, f'Nombre Completo: {alumno.Nombre_completo}')
    pdf.drawString(100, 690, f'CURP: {alumno.Curp}')
    pdf.drawString(100, 670, f'Asunto: {solicitud.id_asunto}')

    pdf.drawString(100, 650, f'Fecha de Solicitud: {solicitud.fecha}')
    pdf.drawString(100, 630, f'Proceso: {solicitud.Proceso}')

    qr_pil = qr_img.convert('RGB')
    img_tmp = BytesIO()
    qr_pil.save(img_tmp, format='PNG')
    img_tmp.seek(0)
    qr_img = Image.open(img_tmp)
    qr_img = qr_img.resize((100, 100))
    pdf.drawInlineImage(qr_img, 400, 600)

    pdf.save()
    buffer.seek(0)

    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=comprobante_{id_solicitud}.pdf'

    return response

@app.route('/editar_alumno/<int:id_alumno>', methods=['GET', 'POST'])
def editar_alumno(id_alumno):
    alumno = Alumno.query.get_or_404(id_alumno)
    niveles = Nivel.query.all()
    municipios = Municipio.query.all()
    asuntos = Asunto.query.all()
    if request.method == 'POST':
        alumno.Nombre_completo = request.form['nombre_completo']
        alumno.nombre = request.form['nombre']
        alumno.paterno = request.form['paterno']
        alumno.materno = request.form['materno']
        alumno.telefono = request.form['telefono']
        alumno.celular = request.form['celular']
        alumno.correo = request.form['correo']
        alumno.nivel_id = request.form['nivel_id']
        alumno.municipio_id = request.form['municipio_id']
        alumno.asunto_id = request.form['asunto_id']
        db.session.commit()
        return redirect(url_for('inicio'))
    return render_template('editar_alumno.html', alumno=alumno, niveles=niveles, municipios=municipios, asuntos=asuntos)

@app.route('/eliminar_alumno/<int:id_alumno>', methods=['POST'])
def eliminar_alumno(id_alumno):
    alumno = Alumno.query.get_or_404(id_alumno)
    Solicitud.query.filter_by(id_alumno=id_alumno).delete()
    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for('inicio'))

####Login###################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        user = Usuario.query.filter_by(Usuario=usuario, Contraseña=contraseña).first()
        if user:
            session['usuario'] = user.Usuario
            return redirect(url_for('perfil'))
        else:
            return 'Credenciales inválidas. Inténtalo de nuevo.'
    return render_template('login.html')

@app.route('/perfil')
def perfil():
    if 'usuario' in session:
        usuario = session['usuario']
        return render_template('perfil.html', usuario=usuario) 
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('inicio'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        nombre_completo = request.form['nombre_completo']
        puesto = request.form['puesto']

        # Verificar si el usuario ya existe en la base de datos
        existing_user = Usuario.query.filter_by(Usuario=usuario).first()
        if existing_user:
            return 'El usuario ya existe. Por favor, elige otro.'

        # Crear un nuevo usuario y guardarlo en la base de datos
        new_user = Usuario(usuario=usuario, contraseña=contraseña, nombre_completo=nombre_completo, puesto=puesto)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('registro.html')

#########login################################

#############Admin crud#######################

# Ruta para buscar alumnos por nombre
@app.route('/editar_solicitud/<int:id_solicitud>', methods=['GET', 'POST'])
def editar_solicitud(id_solicitud):
    solicitud = Solicitud.query.get_or_404(id_solicitud)
    municipios = Municipio.query.all()  # Obtener todos los municipios
    asuntos = Asunto.query.all()  # Obtener todos los asuntos
    if request.method == 'POST':
        solicitud.Turno = request.form['turno']
        solicitud.id_municipio = request.form['id_municipio']
        solicitud.id_asunto = request.form['id_asunto']
        solicitud.fecha = request.form['fecha']
        solicitud.Proceso = request.form['proceso']
        db.session.commit()
        return redirect(url_for('perfil'))
    return render_template('editar_solicitud.html', solicitud=solicitud, municipios=municipios, asuntos=asuntos)


@app.route('/eliminar_solicitud/<int:id_solicitud>', methods=['POST'])
def eliminar_solicitud(id_solicitud):
    solicitud = Solicitud.query.get_or_404(id_solicitud)
    # Obtener el ID del alumno asociado a la solicitud
    id_alumno = solicitud.id_alumno
    # Eliminar la solicitud
    db.session.delete(solicitud)
    # Buscar y eliminar al alumno asociado
    alumno = Alumno.query.get_or_404(id_alumno)
    db.session.delete(alumno)
    # Confirmar los cambios en la base de datos
    db.session.commit()
    # Redireccionar a la página de inicio
    return redirect(url_for('buscar_alumno_nombre'))


@app.route('/buscar_alumno_nombre', methods=['GET', 'POST'])
def buscar_alumno_nombre():
    if request.method == 'POST':
        nombre_buscar = request.form['nombre_buscar']
        alumno = Alumno.query.filter_by(Nombre_completo=nombre_buscar).first()
        if alumno:
            solicitud = Solicitud.query.filter_by(id_alumno=alumno.idAlumno).first()
            if solicitud:
                municipio = Municipio.query.get(solicitud.id_municipio)
                asunto = Asunto.query.get(solicitud.id_asunto)  # Obtener el objeto Asunto correspondiente
                if municipio and asunto:
                    municipio_nombre = municipio.municipio
                    asunto_nombre = asunto.NombreAsunto  # Obtener el nombre del asunto
                    return render_template('detalle_solicitud.html', alumno=alumno, solicitud=solicitud, municipio_nombre=municipio_nombre, asunto_nombre=asunto_nombre)
                else:
                    return "Error: El municipio o el asunto no fueron encontrados en la base de datos."
            else:
                return render_template('sin_solicitud.html', alumno=alumno)
        else:
            return render_template('alumno_no_encontrado.html')
    return render_template('buscar_alumno_nombre.html')


#############Admin crud#######################
#############curd nivel####################
@app.route('/crud_asunto')
def crud_asunto():
    asuntos = Asunto.query.all()
    return render_template('crud_asunto.html', asuntos=asuntos)

@app.route('/agregar', methods=['POST'])
def agregar_asunto():
    nombre = request.form['nombre']
    nuevo_asunto = Asunto(NombreAsunto=nombre)
    db.session.add(nuevo_asunto)
    db.session.commit()
    return redirect(url_for('crud_asunto'))

@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_asunto(id):
    asunto = Asunto.query.get_or_404(id)
    db.session.delete(asunto)
    db.session.commit()
    return redirect(url_for('crud_asunto'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_asunto(id):
    asunto = Asunto.query.get_or_404(id)
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        asunto.NombreAsunto = nuevo_nombre
        db.session.commit()
        return redirect(url_for('crud_asunto'))
    return render_template('editar_asunto.html', asunto=asunto)

##############crud nivel###################
@app.route('/crud_nivel')
def crud_nivel():
    niveles = Nivel.query.all()
    return render_template('crud_nivel.html', niveles=niveles)

@app.route('/agregar_nivel', methods=['POST'])
def agregar_nivel():
    nombre = request.form['nombre']
    nuevo_nivel = Nivel(NombreNivel=nombre)
    db.session.add(nuevo_nivel)
    db.session.commit()
    return redirect(url_for('crud_nivel'))

@app.route('/eliminar_nivel/<int:id>', methods=['GET', 'POST'])
def eliminar_nivel(id):
    nivel = Nivel.query.get_or_404(id)
    db.session.delete(nivel)
    db.session.commit()
    return redirect(url_for('crud_nivel'))

@app.route('/editar_nivel/<int:id>', methods=['GET', 'POST'])
def editar_nivel(id):
    nivel = Nivel.query.get_or_404(id)
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nivel.NombreNivel = nuevo_nombre
        db.session.commit()
        return redirect(url_for('crud_nivel'))
    return render_template('editar_nivel.html', nivel=nivel)

###############Dashboard############################

@app.route('/grafica')
def mostrar_grafica():
    return render_template('grafica.html')

@app.route('/data')
def data():
    # Obtenemos los datos de las solicitudes agrupados por municipio y estado
    datos = {}
    municipios = Municipio.query.all()
    for municipio in municipios:
        # Contamos el número de solicitudes resueltas y pendientes para este municipio
        resueltas = Solicitud.query.filter_by(id_municipio=municipio.idmunicipio, Proceso='Resuelto').count()
        pendientes = Solicitud.query.filter_by(id_municipio=municipio.idmunicipio, Proceso='Pendiente').count()
        datos[municipio.municipio] = {'Resuelto': resueltas, 'Pendiente': pendientes}

    return jsonify(datos)

########################################
#---Rest_APi---#

@app.route('/Niv')
def Niv():
    return render_template('Niv.html')

@app.route('/niveles', methods=['GET'])
def get_niveles():
    niveles = Nivel.query.all()
    return jsonify({'niveles': [{'idNivel': nivel.idNivel, 'NombreNivel': nivel.NombreNivel} for nivel in niveles]})

@app.route('/niveles', methods=['POST'])
def create_nivel():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
    else:
        data = request.form
    new_nivel = Nivel(NombreNivel=data['NombreNivel'])
    db.session.add(new_nivel)
    db.session.commit()
    return jsonify({'message': 'Nivel creado exitosamente'}), 201

@app.route('/niveles/<int:id>', methods=['PUT'])
def update_nivel(id):
    nivel = Nivel.query.get_or_404(id)
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
    else:
        data = request.form
    nivel.NombreNivel = data['NombreNivel']
    db.session.commit()
    return jsonify({'message': 'Nivel actualizado exitosamente'})

@app.route('/niveles/<int:id>', methods=['DELETE'])
def delete_nivel(id):
    nivel = Nivel.query.get_or_404(id)
    db.session.delete(nivel)
    db.session.commit()
    return jsonify({'message': 'Nivel eliminado exitosamente'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
