from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.child import Child, child_schema, children_schema
from models.parent_guardian import ParentGuardian, parent_guardian_schema
from models.parent_guardian_child import ParentGuardianChild
from utils import role_required #import role_required decorator
from marshmallow.exceptions import ValidationError

parents_guardians_bp = Blueprint("parents_guardians", __name__, url_prefix="/children/<int:child_id>/parents_guardians")

#Define routes for parent_guardian
    
#POST - /children/<int:child_id>/parents_guardians - create new parent_guardian record
@parents_guardians_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_parent_guardian_child_relationship(child_id):
    body_data = parent_guardian_schema.load(request.get_json())
    #fetch child with particular id - child_id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child exists:
    if child:
        #create an instance of the ParentGuardian model
        parent_guardian = ParentGuardian(
            name=body_data.get("name"),
            phone=body_data.get("phone"),
            email=body_data.get("email")
        )
        #add and commit the session to the db
        db.session.add(parent_guardian)
        db.session.commit()
        #return created commit
        return parent_guardian_schema.dump(parent_guardian), 201
    #else
    else:
        #return error
        return {"error": f"Child with id '{child_id}' not found"}, 404
    
#DELETE - /children/child_id/parents_guardians/parent_guardian_id - delete parent_guardian record
@parents_guardians_bp.route("/<int:parent_guardian_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_parent_guardian(child_id, parent_guardian_id):
    #get parent_guardian from db
    stmt = db.select(ParentGuardian).filter_by(id=parent_guardian_id)
    parent_guardian = db.session.scalar(stmt)
    #if parent_guardian exists
    if parent_guardian:
        #delete and commit
        db.session.delete(parent_guardian)
        db.session.commit()
        return {"message": f"Parent or Guardian '{parent_guardian_id}' deleted successfully"}
    else:
        return {"error": f"Parent or Guardian with id '{parent_guardian_id}' not found"}, 404
    
#PUT, PATCH - /children/child_id/parents_guardians/parent_guardian_id - update/edit parent/guardian
@parents_guardians_bp.route("/<int:parent_guardian_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("admin")
def edit_parent_guardian(child_id, parent_guardian_id):
    body_data = parent_guardian_schema.load(request.get_json(), partial=True)
    stmt = db.select(ParentGuardian).filter_by(id=parent_guardian_id)
    parent_guardian = db.session.scalar(stmt)
    if parent_guardian:
        parent_guardian.name=body_data.get("name") or parent_guardian.name
        parent_guardian.phone=body_data.get("phone") or parent_guardian.phone
        parent_guardian.email=body_data.get("email") or parent_guardian.email
        
        db.session.commit()
        
        return parent_guardian_schema.dump(parent_guardian), 201
    else:
        return {"error": f"Parent or Guardian with id '{parent_guardian_id}' not found"}, 404



    


