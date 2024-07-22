from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.child import Child, child_schema, children_schema

children_bp = Blueprint("children", __name__, url_prefix="/children")

#Create CRUD operations for child/children

#DELETE - /children/<id> - delete a child
#PUT, PATCH - /children/<id> - edit a child

#GET - /children - fetch all children
@children_bp.route("/")
def get_all_children():
    stmt = db.select(Child)
    children = db.session.scalars(stmt)
    return children_schema.dump(children)

#GET - /children/<id> - fetch a single child
@children_bp.route("/<int:child_id>")
def get_one_child(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    if child:
        return child_schema.dump(child)
    else:
        return {"error": f"Child with id {child_id} not found"}, 404
    
#POST - /children - create a new child
@children_bp.route("/", methods=["POST"])
@jwt_required()
def create_child():
    body_data = request.get_json()
    child = Child(
        name=body_data.get("name"),
        dob=body_data.get("dob"),
        emergency_contact_1=body_data.get("emergency_contact_1"),
        emergency_contact_2=body_data.get("emergency_contact_2"),
        staff_id=get_jwt_identity()
    )
    
    db.session.add(child)
    db.session.commit()
    
    return child_schema.dump(child)
    