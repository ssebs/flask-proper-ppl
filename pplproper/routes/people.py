'''
# pplproper/routes/people.py - routes for people
'''
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from ..models import Person
from .. import db


user_routes = Blueprint("people", __name__)


@user_routes.route("/people/", methods=["GET"])
@jwt_required
def all_ppl():
    ppl = []
    for p in Person.query.filter_by(active=1):
        ppl.append(p.as_dict())
    return jsonify({"Status": "OK", "People": ppl}), 200
# all_ppl


@user_routes.route("/people/", methods=["POST"])
@jwt_required
def create_person():
    req_data = request.json
    if not req_data["email"]:
        return jsonify({"Status": "No Email provided"})

    new_person = Person(
        first_name=req_data["first_name"],
        last_name=req_data["last_name"],
        password=generate_password_hash(req_data["password"]),
        email=req_data["email"],
        active=1
    )
    db.session.add(new_person)
    db.session.commit()

    return jsonify({"Status": "Created", "Person": new_person.as_dict()}), 201
# create_person


@user_routes.route("/people/<id>", methods=["GET"])
@jwt_required
def one_person(id):
    try:
        person = Person.query.filter_by(id=id).one().as_dict()
        return jsonify({"Status": "OK", "People": person}), 200
    except:
        return jsonify({"Status": "Person not found"}), 404
# one_person


@user_routes.route("/people/<id>", methods=["PUT"])
@jwt_required
def update_person(id):
    fn = request.json.get("first_name", None)
    ln = request.json.get("last_name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    active = request.json.get("active", None)
    usr = None

    try:
        person = Person.query.filter_by(id=id).one()
    except:
        return jsonify({"Status": "Person not found"}), 404

    # set vars if they exist
    if fn:
        person.first_name = fn
    if ln:
        person.last_name = ln
    if email:
        person.email = email
    if active:
        person.active = active

    db.session.commit()
    return jsonify({"Status": "OK", "Person": person.as_dict()}), 200
# update_person


@user_routes.route("/people/<id>", methods=["DELETE"])
@jwt_required
def delete_person(id):
    try:
        person = Person.query.filter_by(id=id).one()
        person.active = 0
        db.session.commit()
        return jsonify({"Status": "Deleted"}), 200
    except:
        return jsonify({"Status": "Person not found"}), 404
# delete_person
