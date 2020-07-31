"""
Created by Epic at 7/31/20
"""
from flask import Blueprint, request, current_app, jsonify
from datadriver import DatabaseClient, models
from app.utilities import require_authentication

blueprint = Blueprint("faq", __name__, url_prefix="/faq")


@blueprint.route("/", methods=["GET"])
def get_faq():
    data = request.json
    db: DatabaseClient = current_app.db

    query = db.session.query(models.Faq).get(data["search"])
    if query is None:
        return jsonify(None)
    else:
        return jsonify(query.description)


@blueprint.route("/", methods=["PUT"])
def add_faq():
    data = request.json
    db: DatabaseClient = current_app.db

    try:
        name = data["name"]
        description = data["description"]
    except KeyError:
        return jsonify(success=False, message="Invalid body"), 400

    try:
        db.session.add(models.Faq(name=name, description=description))
        db.save()
    except:
        db.session.rollback()
        return jsonify(success=False, message="Invalid body"), 400
    return jsonify(success=True)
