from datetime import datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.child import Child, child_schema, children_schema
from utils import role_required
from controllers.daily_checklist_controller import daily_checklists_bp 
from controllers.health_record_controller import health_records_bp
from controllers.parent_guardian_controller import parents_guardians_bp
from controllers.parent_guardian_child_controller import parent_guardian_child_bp
from marshmallow.exceptions import ValidationError

children_bp = Blueprint("children", __name__, url_prefix="/children")

#register other blueprints that are related and dependent of child with the children_bp
children_bp.register_blueprint(daily_checklists_bp, url_prefix="/<int:child_id>/daily_checklists")
children_bp.register_blueprint(health_records_bp, url_prefix="/<int:child_id>/health_records")
children_bp.register_blueprint(parents_guardians_bp, url_prefix="/<int:child_id>/parents_guardians")
children_bp.register_blueprint(parent_guardian_child_bp, url_prefix="/<int:child_id>/parent_guardian_child")

#Define routes for Children
#Create CRUD operations for child/children:
#GET - /children - get all children
@children_bp.route("/")
@jwt_required()
def get_all_children():
    stmt = db.select(Child).order_by(Child.name.desc())
    children = db.session.scalars(stmt)
    return children_schema.dump(children), 200

#GET - /children/<id> - get a single child information
@children_bp.route("/<int:child_id>")
@jwt_required()
def get_one_child(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    if child:
        return child_schema.dump(child), 200
    else:
        return {"error": f"Child with id {child_id} not found"}, 404

    
#POST - /children - create a new child
@children_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("admin") #only admin can create child record
def create_child():
    try:
        body_data = child_schema.load(request.get_json())
    except ValidationError as err:
        return{"error": err.messages}, 400
    
    child = Child(
        name=body_data.get("name"),
        dob=body_data.get("dob"),
        emergency_contact_1=body_data.get("emergency_contact_1"),
        emergency_contact_2=body_data.get("emergency_contact_2"),
    )
    
    db.session.add(child)
    db.session.commit()
    
    return child_schema.dump(child), 201

#DELETE - /children/<id> - delete a child
@children_bp.route("/<int:child_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin") #only admin can delete child record
def delete_child(child_id):
    #get child info from database
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child
    if child:
        #delete child
        db.session.delete(child)
        db.session.commit()
        return {"message": f"Child '{child_id}' deleted successfully"}, 200
    #else
    else:
        #return error
        return {"error": f"Child with id '{child_id}' not found"}, 404
    

#PUT, PATCH - /children/<id> - edit a child
@children_bp.route("/<int:child_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("admin") #only admin can delete child record
def update_child(child_id):
    #get data from body of the request
    try:
        body_data = child_schema.load(request.get_json(), partial=True)
    except ValidationError as err:
        return{"error": err.messages}, 400
    #get child from database
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child found
    if child:
        #update fields 
        child.name = body_data.get("name") or child.name
        child.dob = body_data.get("dob") or child.dob
        child.emergency_contact_1 = body_data.get("emergency_contact_1") or child.emergency_contact_1
        child.emergency_contact_2 = body_data.get("emergency_contact_2") or child.emergency_contact_2
        #commit to db
        db.session.commit()
        #return response
        return child_schema.dump(child)
    else:
        return {"error": f"Child with id '{child_id}' not found"}, 404
    

    
    