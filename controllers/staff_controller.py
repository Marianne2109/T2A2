
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.staff import Staff, staff_schema, staffs_schema
from controllers.auth_controller import role_required #import role_required decorator
from utils import is_username_unique, role_required 
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

#POST - create staff - /staffs
@staffs_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_staff():
    try:
        body_data = staff_schema.load(request.get_json())
    except ValidationError as err:
        return{"error": err.messages}, 400
    
    #if username is not unique
    if not is_username_unique(body_data.get("username")):
        return{"error": "Username already exists, try a different username"}, 400
    
    staff = Staff(
        name=body_data.get("name"),
        position=body_data.get("position"),
        username=body_data.get("username"),
        password=body_data.get("password"),
        role=body_data.get("role"),
        is_admin=body_data.get("is_admin", False)     
    )
   
    #add to the database
    db.session.add(staff)
    db.session.commit()
    
    return staff_schema.dump(staff), 201

#DELETE - delete staff - /staffs/staff_id
@staffs_bp.route("/staffs/<int:staff_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_staff(staff_id):
     #get staff info from database
    stmt = db.select(Staff).filter_by(id=staff_id)
    staff = db.session.scalar(stmt)
    #if staff
    if staff:
        #delete staff
        db.session.delete(staff)
        db.session.commit()
        return {"message": f"Staff '{staff_id}' deleted successfully"}, 200
    #else
    else:
        #return error
        return {"error": f"Staff with id '{staff_id}' not found"}, 404
    
#PUT, PATCH - update staff details - /staffs/staff_id
@staffs_bp.route("/staffs/<int:staff_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("admin") 
def update_staff(staff_id):
    #get data from body of the request
    try:
        body_data = staff_schema.load(request.get_json(), partial=True)
    except ValidationError as err:
        return{"error": err.messages}, 400
    #get staff info from database
    stmt = db.select(Staff).filter_by(id=staff_id)
    staff = db.session.scalar(stmt)
    #if staff found
    if staff:
        #update fields 
        staff.name = body_data.get("name") or staff.name
        staff.position = body_data.get("position") or staff.position
        staff.username = body_data.get("username") or staff.username
        staff.role = body_data.get("role") or staff.role
        staff.is_admin = body_data.get("is_admin") or staff.is_admin
        if "password" in body_data:
            staff.password = body_data.get("password")
 
        #commit to db
        db.session.commit()
        #return response
        return staff_schema.dump(staff), 200
    else:
        return {"error": f"Staff with id '{staff_id}' not found"}, 404
    

    
    
    
    
