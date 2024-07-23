from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.child import Child, child_schema, children_schema
from models.staff import Staff, staff_schema, staffs_schema
from controllers.auth_controller import role_required #import role_required decorator

children_bp = Blueprint("children", __name__, url_prefix="/children")

#Create CRUD operations for child/children:
#GET - /children - fetch all children
@children_bp.route("/")
def get_all_children():
    stmt = db.select(Child).order_by(Child.name.desc())
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
@role_required("admin") #only admin can create child record
def create_child():
    body_data = request.get_json()
    child = Child(
        name=body_data.get("name"),
        dob=body_data.get("dob"),
        emergency_contact_1=body_data.get("emergency_contact_1"),
        emergency_contact_2=body_data.get("emergency_contact_2"),
    )
    
    db.session.add(child)
    db.session.commit()
    
    return child_schema.dump(child)

#DELETE - /children/<id> - delete a child
@children_bp.route("/<int:child_id>", methods=["DELETE"])
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
@role_required("admin") #only admin can delete child record
def update_child(child_id):
    #get data from body of the request
    body_data = request.get_json()
    #get child from database
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child
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
    

    
    