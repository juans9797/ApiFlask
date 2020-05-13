from app import app,db
from app.Models.UbicacionModel import UbicacionModel,UbicacionSchema
from flask import jsonify


@app.route('/crearUbicacion')
def crearUbicacion():
    ubicacion = UbicacionModel(lugar="Bogota")
    db.session.add(ubicacion)
    db.session.commit()
    return "OK"


@app.route('/todasUbicaciones')
def todarUbicaciones():
    ubicaciones = UbicacionModel.query.all()
    json = UbicacionSchema(many=True).dump(ubicaciones)
    return jsonify(json)


@app.route('/ubicacion/<idUbicacion>')
def obtenerUbicacion(idUbicacion):
    ubicacion = UbicacionModel.query.get(idUbicacion)
    json = UbicacionSchema().dump(ubicacion)
    return jsonify(json)


@app.route('/actualizarUbicacion/<idUbicacion>')
def actualizarUbicacion(idUbicacion):
    ubicacion = UbicacionModel.query.get(idUbicacion)
    ubicacion.lugar = "Jamundi"
    db.session.commit()
    return "OK"


@app.route('/borrarUbicacion/<idUbicacion>')
def borrarUbicacion(idUbicacion):
    ubicacion = UbicacionModel.query.get(idUbicacion)
    db.session.delete(ubicacion)
    db.session.commit()
    return "OK"


@app.route('/productosUbicacion/<idUbicacion>')
def productosUbicacion(idUbicacion):
    ubicacion = UbicacionModel.query.get(idUbicacion)
    productos = ubicacion.productos.all()
    for p in productos:
        print(p.Referencia)
    return "OK"