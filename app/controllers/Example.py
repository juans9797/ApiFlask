from app import app
from flask import request


@app.route('/')
def test():
    return "Hello World Moviles"


@app.route('/param/<p1>')
def test2(p1):
    return str(p1)


@app.route('/qparam')
def test3():
    valor = request.args.get("p")
    return str(valor)


@app.route('/status')
def test4():
    return "Recibido"


@app.route('/post',methods=["POST"])
def test5():
    print(request.get_json())
    return str(request.get_json())