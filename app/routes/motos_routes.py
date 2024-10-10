from flask import Blueprint, render_template

bp = Blueprint('motos', __name__)

@bp.route('/motos/yz_250')
def yz_250_view():
    return render_template('motos/yz_250.html')

@bp.route('/motos/rx_115')
def rx_115_view():
    return render_template('motos/rx_115.html')

@bp.route('/motos/dt_175')
def dt_175_view():
    return render_template('motos/dt_175.html')

bp.route('/motos/fz_250')
def fz_250_view():
    return render_template('motos/fz_250.html')
