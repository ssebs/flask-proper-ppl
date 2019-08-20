'''
# pplproper/__init__.py - init flask / sql
'''
import datetime
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


uri = "sqlite:///test.db"

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = str(uri)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "foobar123"
# app.config["SQLALCHEMY_ECHO"] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=14)
db = SQLAlchemy(app)
db.init_app(app)
jwt = JWTManager(app)

# Need to import later due to circular import issues
from .routes.people import user_routes  # noqa
from .routes.auth import auth_routes  # noqa

app.register_blueprint(user_routes)
app.register_blueprint(auth_routes)


@app.route("/")
def test():
    return "Server up and running"
