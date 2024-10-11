from app import db

class Mantenimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cambio_aceite = db.Column(db.String(100), nullable=False)
    filtro_aire = db.Column(db.String(100), nullable=False)
    cadena = db.Column(db.String(100), nullable=False)
    bujia = db.Column(db.String(100), nullable=False)
    carburador = db.Column(db.String(100), nullable=False)
    frenos = db.Column(db.String(100), nullable=False)
    aceite_horquilla = db.Column(db.String(100), nullable=False)
    rodamientos = db.Column(db.String(100), nullable=False)
    suspension = db.Column(db.String(100), nullable=False)
    piston_aros = db.Column(db.String(100), nullable=False)
    sistema_electrico = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Mantenimiento {self.id}>'
