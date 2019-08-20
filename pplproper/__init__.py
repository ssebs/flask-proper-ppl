'''
# pplproper/__init__.py - init flask / sql
'''
import datetime
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
jwt = JWTManager()

test_db_name = "test.db"
production_db_name = "prod.db"


def create_app(config):
    if config == "test":
        # import os
        # try:
        #     os.remove(f"{__name__}/{test_db_name}")
        # except:
        #     pass
        uri = f"sqlite:///{test_db_name}"
    else:
        uri = f"sqlite:///{production_db_name}"

    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = str(uri)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "foobar123"
    # app.config["SQLALCHEMY_ECHO"] = True
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=14)
    db.init_app(app)
    jwt.init_app(app)

    # Need to import later due to circular import issues
    from .routes.people import user_routes  # noqa
    from .routes.auth import auth_routes  # noqa

    app.register_blueprint(user_routes)
    app.register_blueprint(auth_routes)

    @app.route("/")
    def test():
        return "Server up and running"

    return app
# create_app
