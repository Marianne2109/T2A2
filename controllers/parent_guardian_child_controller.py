from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.parent_guardian_child import ParentGuardianChild, parent_guardian_child_schema, parents_guardians_children_schema
from models.child import Child
from models.parent_guardian import ParentGuardian
from utils import role_required #import role_required decorator
from marshmallow.exceptions import ValidationError


parent_guardian_child_bp = Blueprint("parent_guardian_child", __name__, url_prefix="/children/<int:child_id>/parents_guardians_children")  


#GET - /parent_guardian_child/<int:id> - get particular parent_guardian relationship 
@parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["GET"])
@jwt_required()
@role_required("staff")
def get_parent_guardian(child_id, parent_guardian_child_id):
    stmt = db.select(ParentGuardianChild).filter_by(id=parent_guardian_child_id, child_id=child_id)
    parent_guardian_child = db.session.scalar(stmt)
    if parent_guardian_child:
        return parent_guardian_child_schema.dump(parent_guardian_child), 201
    else:
        return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"},  404
    
# # POST - /children/<int:child_id>/parents_guardians_children - create new parent_guardian_child relationship for a child
# @parent_guardian_child_bp.route("/", methods=["POST"])
# @jwt_required()
# @role_required("admin")
# def create_parent_guardian_child_relationship(child_id):
#     try:
#         body_data = parent_guardian_child_schema.load(request.get_json())
#     except ValidationError as err:
#         return{"error": err.messages}, 400

#     #fetch the child
#     child = db.session.get(Child, child_id)
#     if not child:
#             return {"error": f"Child with id '{child_id}' not found"}, 404
        
#     #fetch parent/guardian
#     parent_guardian_id = body_data.get("parent_guardian_id")
#     parent_guardian = db.session.get(ParentGuardian, parent_guardian_id)
#     if not parent_guardian:
#         return {"error": f"Parent or Guardian with id '{parent_guardian_id}' not found"}, 404
    
#     #create the relationship
#     parent_guardian_child = ParentGuardianChild(
#         child_id=child.id,
#         parent_guardian_id=parent_guardian.id,
#         relationship_to_child=body_data.get["relationship_to_child"] #Includes relationship to the child
#     )
    
#     db.session.add(parent_guardian_child)
#     db.session.commit()
    
#     return parent_guardian_child_schema.dump(parent_guardian_child), 201



# #DELETE - /children/<int:child_id>/parents_guardians_children/<int:parent_guardian_child_id> - delete parent_guardian relationship for a child
# @parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["DELETE"])
# @jwt_required()
# @role_required("admin")
# def delete_parent_guardian_child_relationship(child_id, parent_guardian_child_id):
#     stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
#     parent_guardian_child = db.session.scalar(stmt)
#     if parent_guardian_child:
#         db.session.delete(parent_guardian_child)
#         db.session.commit()
#         return {"message": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' deleted successfully"}
#     else:
#         return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"}, 404
    
# #PUT, PATCH - /children/<int:child_id>/parents_guardians_children/<int:parent_guardian_child_id> - update/edit a parent_guardian relationship for a child
# @parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["PUT", "PATCH"])
# @jwt_required()
# @role_required("admin")
# def update_parent_guardian_child_relationship(child_id, parent_guardian_child_id):
#     body_data = parent_guardian_child_schema.load(request.get_json())
#     stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
#     parent_guardian_child =db.session.scalar(stmt)
#     if parent_guardian_child:
#         parent_guardian_child.relationship_to_child = body_data.get("relationship_to_child") or parent_guardian_child.relationship_to_child
        
#         db.session.commit()
        
#         return parent_guardian_child_schema.dump(parent_guardian_child)
    
#     else:
#         return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"}, 404