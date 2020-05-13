from app import ma,db
from marshmallow import post_load


class ProductoModel(db.Model):
    idProducto = db.Column(db.Integer,primary_key=True)
    Referencia = db.Column(db.String(30))
    Precio = db.Column(db.Numeric)
    Tamano = db.Column(db.Numeric)
    Unidad = db.Column(db.String(30))
    idCategoria = db.Column(db.Integer)
    idEstadoProducto = db.Column(db.Integer)
    idUbicacion = db.Column(db.Integer,db.ForeignKey('Ubicacion.idUbicacion'))
    # Tabla.PrimaryKey


class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        include_fk = True

    @post_load
    def make_producto(self,data,**kwargs):
        return ProductoModel(**data)