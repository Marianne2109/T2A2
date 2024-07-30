
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, bcrypt
from models.staff import Staff, staff_schema, staffs_schema
from utils import role_required 
from marshmallow.exceptions import ValidationError

staffs_bp = Blueprint("staffs", __name__, url_prefix="/staffs")

#GET - /staffs - get all staff 
@staffs_bp.route("/", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_staffs():
    stmt = db.select(Staff)
    staffs = db.session.scalars(stmt).all()
    return staffs_schema.dump(staffs), 200

#GET - /staffs/<id> - get single staff info
@staffs_bp.route("/<int:staff_id>", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_staff(staff_id):
    stmt = db.select(Staff).filter_by(id=staff_id)
    staff = db.session.scalar(stmt)
    if staff:
        return staff_schema.dump(staff), 200
    else:
        return {"error": f"Staff with id '{staff_id}' not found"}, 404


