from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.parent_guardian_child import ParentGuardianChild, parent_guardian_child_schema, parents_guardians_children_schema
from models.child import Child
from models.parent_guardian import ParentGuardian
from controllers.auth_controller import role_required #import role_required decorator

parent_guardian_child_bp = Blueprint("parent_guardian_child", __name__, url_prefix="/children/<int:child_id>/parents_guardians_children")  

#GET - /parent_guardian - get all parent_guardian for a child
@parent_guardian_child_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_parents_guardians(child_id):
    stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id)
    parents_guardians = db.session.scalars(stmt).all()
    return parents_guardians_children_schema.dump(parents_guardians)

#GET - /parent_guardian_child/<int:id> - get particular parent_guardian relationship for a child
@parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["GET"])
@jwt_required()
def get_parent_guardian(child_id, parent_guardian_child_id):
    stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
    parent_guardian_child = db.session.scalar(stmt)
    if parent_guardian_child:
        return parent_guardian_child_schema.dump(parent_guardian_child)
    else:
        return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"},  404
    
#POST - /children/<int:child_id>/parents_guardians_children - create new parent_guardian_child relationship for a child
@parent_guardian_child_bp.route("/", methods=["POST"])
@role_required("admin")
def create_parent_guardian_child_relationship(child_id):
    body_data = request.get_json()
    #fetch the child
    child = db.session.get(Child, child_id)
    if not child:
        return {"error": f"Child with id '{child_id}' not found"}, 404
    #fetch parent_guardian
    parent_guardian_id = body_data.get("parent_guardian_id")
    parent_guardian = db.session.get(ParentGuardian, parent_guardian_id)
    if not parent_guardian:
        return {"error": f"Parent or Guardian with id '{parent_guardian_id}' not found"}, 404
    
    #create the relationship
    parent_guardian_child = ParentGuardianChild(
        child_id=child.id,
        parent_guardian_id=parent_guardian.id,
        relationship_to_child=body_data.get("relationship_to_child")
    )
    
    db.session.add(parent_guardian_child)
    db.session.commit()
    
    return parent_guardian_child_schema.dump(parent_guardian_child), 201

#DELETE - /children/<int:child_id>/parents_guardians_children/<int:parent_guardian_child_id> - delete parent_guardian relationship for a child
@parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["DELETE"])
@role_required("admin")
def delete_parent_guardian_child_relationship(child_id, parent_guardian_child_id):
    stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
    parent_guardian_child = db.session.scalar(stmt)
    if parent_guardian_child:
        db.session.delete(parent_guardian_child)
        db.session.commit()
        return {"message": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' deleted successfully"}
    else:
        return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"}, 404
    
#PUT, PATCH - /children/<int:child_id>/parents_guardians_children/<int:parent_guardian_child_id> - update/edit a parent_guardian relationship for a child
@parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["PUT", "PATCH"])
@role_required("admin")
def update_parent_guardian_child_relationship(child_id, parent_guardian_child_id):
    body_data = request.get_json()
    stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
    parent_guardian_child =db.session.scalar(stmt)
    if parent_guardian_child:
        parent_guardian_child.relationship_to_child = body_data.get("relationship_to_child") or parent_guardian_child.relationship_to_child
        
        db.session.commit()
        
        return parent_guardian_child_schema.dump(parent_guardian_child)
    else:
        return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"}, 404