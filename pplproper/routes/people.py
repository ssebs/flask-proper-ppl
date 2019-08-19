'''
# pplproper/routes/people.py - routes for people
'''
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
# from ..util import clean_update
from ..models import Person
from .. import db  # noqa


user_routes = Blueprint("people", __name__)


@user_routes.route("/people/", methods=["GET"])
def all_ppl():
    ppl = []
    for p in Person.query.filter_by(active=1):
        ppl.append(p.as_dict())
    return jsonify({"Status": "OK", "People": ppl}), 200
# all_ppl


@user_routes.route("/people/", methods=["POST"])
def create_person():
    req_data = request.json
    if not req_data["email"]:
        return jsonify({"Status": "No Email provided"})
    new_person = Person(
        first_name=req_data["first_name"],
        last_name=req_data["last_name"],
        password=req_data["password"],
        email=req_data["email"],
        active=1
    )
    db.session.add(new_person)
    db.session.commit()

    return jsonify({"Status": "Created", "Person": new_person.as_dict()}), 201
# create_person


@user_routes.route("/people/<id>", methods=["GET"])
def one_person(id):
    try:
        person = Person.query.filter_by(active=1, id=id).one().as_dict()
        return jsonify({"Status": "OK", "People": person}), 200
    except:
        return jsonify({"Status": "Person not found"}), 404
# one_person


@user_routes.route("/people/<id>", methods=["PUT"])
def update_person(id):
    req_data = request.json
    try:
        person = Person.query.filter_by(id=id).one()

        person.first_name = req_data["first_name"]
        person.last_name = req_data["last_name"]
        person.password = req_data["password"]
        person.email = req_data["email"]

        db.session.commit()
        return jsonify({"Status": "OK", "People": person.as_dict()}), 200
    except:
        return jsonify({"Status": "Person not found"}), 404
# update_person


@user_routes.route("/people/<id>", methods=["DELETE"])
def delete_person(id):
    try:
        person = Person.query.filter_by(id=id).one()
        person.active = 0
        db.session.commit()
        return jsonify({"Status": "Deleted"}), 200
    except:
        return jsonify({"Status": "Person not found"}), 404
# delete_person
