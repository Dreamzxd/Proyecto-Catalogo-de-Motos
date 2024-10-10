from flask import Blueprint, render_template

bp = Blueprint('motos', __name__)

@bp.route('/motos/yz_250')
def yz_250_view():
    return render_template('motos/yz_250.html')

@bp.route('/motos/rx_115')
def rx_115_view():
    return render_template('motos/rx_115.html')
