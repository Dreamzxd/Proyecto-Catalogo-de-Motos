from flask import Blueprint,render_template, redirect, url_for, flash
from app import db
from app.models.especificaciones import Especificacion
from app.models.mantenimiento import Mantenimiento
from app.models.rendimiento import Rendimiento

bp = Blueprint('vistad', __name__)

@bp.route('/vistad/especif', methods=['GET', 'POST'])
def agregar_especificacion():
    form = EspecificacionForm()
    if form.validate_on_submit():
        nueva_especificacion = Especificacion(
            marca=form.marca.data,
            modelo=form.modelo.data,
            año=form.año.data,
            cilindrada=form.cilindrada.data,
            potencia=form.potencia.data,
            peso=form.peso.data,
            tipo_motor=form.tipo_motor.data,
            capacidad_tanque=form.capacidad_tanque.data,
            transmision=form.transmision.data,
            suspension_delantera=form.suspension_delantera.data,
            suspension_trasera=form.suspension_trasera.data,
            freno_delantero=form.freno_delantero.data,
            freno_trasero=form.freno_trasero.data,
            neumatico_delantero=form.neumatico_delantero.data,
            neumatico_trasero=form.neumatico_trasero.data
        )
        db.session.add(nueva_especificacion)
        db.session.commit()
        flash('Especificaciones agregadas correctamente!')
        return redirect(url_for('agregar_especificacion'))
    return render_template('especificaciones.html', form=form)

@bp.route('/vistad/mantenim', methods=['GET', 'POST'])
def agregar_mantenimiento():
    form = MantenimientoForm()
    if form.validate_on_submit():
        nuevo_mantenimiento = Mantenimiento(
            cambio_aceite=form.cambio_aceite.data,
            filtro_aire=form.filtro_aire.data,
            cadena=form.cadena.data,
            bujia=form.bujia.data,
            carburador=form.carburador.data,
            frenos=form.frenos.data,
            aceite_horquilla=form.aceite_horquilla.data,
            rodamientos=form.rodamientos.data,
            suspension=form.suspension.data,
            piston_aros=form.piston_aros.data,
            sistema_electrico=form.sistema_electrico.data
        )
        db.session.add(nuevo_mantenimiento)
        db.session.commit()
        flash('Mantenimiento agregado exitosamente!')
        return redirect(url_for('agregar_mantenimiento'))
    return render_template('mantenimiento.html', form=form)

@bp.route('/vistad/rendimiento', methods=['GET', 'POST'])
def agregar_rendimiento():
    form = RendimientoForm()
    if form.validate_on_submit():
        nuevo_rendimiento = Rendimiento(
            velocidad_maxima=form.velocidad_maxima.data,
            aceleracion=form.aceleracion.data,
            consumo=form.consumo.data,
            autonomia=form.autonomia.data,
            capacidad_todoterreno=form.capacidad_todoterreno.data,
            maniobrabilidad=form.maniobrabilidad.data,
            frenado=form.frenado.data
        )
        db.session.add(nuevo_rendimiento)
        db.session.commit()
        flash('Rendimiento agregado exitosamente!')
        return redirect(url_for('agregar_rendimiento'))
    return render_template('rendimiento.html', form=form)
