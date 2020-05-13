from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:desarrollo@127.0.0.1:8070/ApiFlask"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
ma = Marshmallow(app)

from app.controllers import Example,UbicacionController, ProductoController
from app.Models import UbicacionModel, ProductoModel