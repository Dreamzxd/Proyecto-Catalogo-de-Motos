from app import db

class Rendimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    velocidad_maxima = db.Column(db.Float, nullable=False)
    aceleracion = db.Column(db.Float, nullable=False)
    consumo = db.Column(db.Float, nullable=False)
    autonomia = db.Column(db.Integer, nullable=False)
    capacidad_todoterreno = db.Column(db.String(50), nullable=False)
    maniobrabilidad = db.Column(db.String(50), nullable=False)
    frenado = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Rendimiento {self.id}>'
