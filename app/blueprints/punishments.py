"""
Created by Epic at 7/13/20
"""
from datetime import datetime

from datadriver import DatabaseClient, models
from flask import Blueprint, current_app, jsonify, request
from app.utilities import require_authentication
from uuid import uuid4

blueprint = Blueprint("bans", __name__, url_prefix="/punishments")


@blueprint.route("/get")
def get_punishments():
    db: DatabaseClient = current_app.db
    bans = []
    for ban in db.session.query(models.Punishment).all():
        bans.append(models.jsonify_punishment(ban))
    return jsonify(bans)


@blueprint.route("/add", methods=["PUT"])
@require_authentication
def add_punishment():
    db: DatabaseClient = current_app.db
    data = request.json
    try:
        punishment_id = str(uuid4())
        punishment_type = data["punishment_type"]
        punished_id = int(data["punished_id"])
        moderator_id = int(data["moderator_id"])

        punished_at = datetime.fromtimestamp(int(data["punished_at"]))
        expires_at = datetime.fromtimestamp(int(data["expires_at"]))

        punishment_reason = data["reason"]

        db.session.add(
            models.Punishment(punishment_id=punishment_id, punishment_type=punishment_type, expired=False,
                              punished_id=punished_id, moderator_id=moderator_id, punished_at=punished_at,
                              expires_at=expires_at, reason=punishment_reason))
        db.save()
        return jsonify(success=True)
    except (KeyError, TypeError):
        db.session.rollback()
        return jsonify(success=False, message="Invalid request"), 400


@blueprint.route("/expire", methods=["POST"])
def mark_punishment_as_expired():
    db: DatabaseClient = current_app.db
    data = request.json

    try:
        punishment_id = data["punishment_id"]
    except KeyError:
        return jsonify(success=False, message="Invalid body."), 400

    try:
        db.session.query(models.Punishment).filter(models.Punishment.punishment_id == punishment_id).update(
            {"expired": True})
        db.save()
        return jsonify(success=True)
    except:
        db.session.rollback()
        return jsonify(success=False, message="Invalid body.")
