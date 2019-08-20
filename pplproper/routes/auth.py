'''
# pplproper/routes/auth.py - login stuff
'''
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_refresh_token_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token, create_refresh_token
from ..models import Person
from .. import db

auth_routes = Blueprint("auth", __name__)


@auth_routes.route("/password-reset/", methods=["POST"])
def password_reset():
    email = request.json.get('email', None)
    old = request.json.get('old', None)
    new = request.json.get('new', None)
    usr = None

    if not email or not old or not new:
        return jsonify({"Status": "Fill out the form properly..."}), 400

    # Validate user exists
    try:
        usr = Person.query.filter_by(email=email).first()
    except:
        return jsonify({"Status": "User does not exist"}), 400

    # Validate password is the same
    if not check_password_hash(usr.password, old):
        return jsonify({"Status": "Invalid password"}), 400

    usr.password = generate_password_hash(new)
    db.session.commit()
    return jsonify({"Status": "Updated Password"}), 200
# password_reset


@auth_routes.route("/login/", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    usr = None

    # Check for data
    if not email or not password:
        return jsonify({"Status": "Not enough data provided"}), 400

    # Validate user exists
    try:
        usr = Person.query.filter_by(email=email).one()
    except:
        return jsonify({"Status": "User does not exist"}), 400

    # Validate password is the same
    # if usr.password != password:
    if not check_password_hash(usr.password, password):
        return jsonify({"Status": "Invalid password"}), 400

    return jsonify({"Status": "Logged In",
                    "UserToken": "foo", "RefreshToken": "bar"})
# login


@auth_routes.route("/refresh/", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    tmp = get_jwt_identity()
    print(tmp)
    return "foo"
