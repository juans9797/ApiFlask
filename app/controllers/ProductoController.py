from app import app,db
from flask import request
from app.Models.ProductoModel import ProductoModel,ProductoSchema


@app.route('/crearProducto',methods=['POST'])
def crearProducto():
    producto = ProductoSchema().load(request.get_json())
    db.session.add(producto)
    db.session.commit()
    return "OK",201


@app.route('/todosProductos')
def todosProductos():
    productos = ProductoModel.query.all()
    for p in productos:
        print(p.Referencia, p.Ubicacion.lugar)
    return "OK"