from app import db

class Especificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    cilindrada = db.Column(db.Integer, nullable=False)
    potencia = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    tipo_motor = db.Column(db.String(50), nullable=False)
    capacidad_tanque = db.Column(db.Float, nullable=False)
    transmision = db.Column(db.String(50), nullable=False)
    suspension_delantera = db.Column(db.String(100), nullable=False)
    suspension_trasera = db.Column(db.String(100), nullable=False)
    freno_delantero = db.Column(db.String(50), nullable=False)
    freno_trasero = db.Column(db.String(50), nullable=False)
    neumatico_delantero = db.Column(db.String(50), nullable=False)
    neumatico_trasero = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Moto {self.marca} {self.modelo}>'
