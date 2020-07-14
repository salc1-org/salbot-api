"""
Created by Epic at 7/13/20
"""
from datetime import datetime

from datadriver import DatabaseClient, models
from flask import Blueprint, current_app, jsonify, request
from app.utilities import require_authentication

blueprint = Blueprint("bans", __name__, url_prefix="/bans")


@blueprint.route("/get")
def get_bans():
    db: DatabaseClient = current_app.db
    bans = []
    for ban in db.session.query(models.Ban).all():
        bans.append(models.jsonify_ban(ban))
    return jsonify(bans)


@blueprint.route("/edit", methods=["PUT"])
@require_authentication
def add_ban():
    db: DatabaseClient = current_app.db
    data = request.json
    try:
        db.session.add(models.Ban(id=data["id"], banned_at=datetime.fromtimestamp(data["banned_at"]),
                                  expires_at=datetime.fromtimestamp(data.get("expires_at", 0))))
        db.save()
        return jsonify(success=True)
    except KeyError:
        db.session.rollback()
        return jsonify(success=False, message="Invalid request"), 400
