from app import db, ma
from app.Models.ProductoModel import ProductoModel


class UbicacionModel(db.Model):
    __tablename__ = "Ubicacion"
    idUbicacion = db.Column(db.Integer,primary_key=True)
    lugar = db.Column(db.String(30))
    productos = db.relationship('ProductoModel',backref='Ubicacion',lazy='dynamic')
    # Modelo a utilizar


class UbicacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UbicacionModel
