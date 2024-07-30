from datetime import timedelta


from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import bcrypt, db
from models.staff import Staff, staff_schema, StaffSchema
from utils import role_required #import role_required decorator

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

#def function to handle integrity error
def handle_integrity_error(err):
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Username already in use"}, 409
        

#create route to register staff member to the database - this route will also handle create staff record. 
@auth_bp.route("/register", methods=["POST"])
def register_staff():
    try:    #get data from the body of the request
        body_data = request.get_json()
        #create an instance of the staff model
        staff = Staff(
            name=body_data.get("name"),
            position=body_data.get("position"),
            username=body_data.get("username"),
            role=body_data.get("role"),
            is_admin=body_data.get("is_admin")
        )
        #extract tha password from the body
        password=body_data.get("password")
    
        #hash the password
        if password: #if the password exists, create password attribute and pass password and hash
            staff.password = bcrypt.generate_password_hash(password).decode("utf-8") 
            
        #add and commit to the DB
        db.session.add(staff)        
        db.session.commit()
        
        #respond back - return created staff info to the frontend
        return staff_schema.dump(staff), 201
    
    except IntegrityError as err:
        return handle_integrity_error(err)


#login staff route. Use POST request due to data in body requirements. 
@auth_bp.route("/login", methods=["POST"])
def login_staff():
    #get data from the body of the request
    body_data = request.get_json()
    
    #find username in the database with that username
    stmt = db.select(Staff).filter_by(username=body_data.get("username")) #filter by column name
    staff = db.session.scalar(stmt)
    #if username exists and if password is same as database - staff object fetched from database and if password matched with password hashed in database
    if staff and bcrypt.check_password_hash(staff.password, body_data.get("password")):
        #create jwt - access token will need identity, this is the staff id. Token will use timedelta for time expiry 
        token = create_access_token(identity=str(staff.id), expires_delta=timedelta(days=1))
        #response back
        return {"username": staff.username, "is_admin": staff.is_admin, "token": token}, 200
    #else - if the staff doesn't exist or wrong password
    else:
        return {"error": "Invalid username or password"}, 401
    
#DELETE staff login details   
@auth_bp.route("/staffs/<int:staff_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_staff(staff_id):
    #fetch staff with staff id from db
    stmt = db.select(Staff).filter_by(id=staff_id)
    staff = db.session.scalar(stmt)
    #if staff exists
    if staff:
        #delete and commit
        db.session.delete(staff)
        db.session.commit()
        return {"message": f"Staff with id '{staff_id}' successfully deleted"}, 200
    #else
    else:
        #return error
        return {"error": f"Staff with id '{staff_id}' not found"}, 404
    
#PUT, PATCH - update staff login details
@auth_bp.route("/staffs/<int:staff_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("admin")
def update_staff(staff_id):
    try:
        #get fields from body of the request
        body_data = StaffSchema().load(request.get_json(), partial=True)
        password = body_data.get("password")
        #fetch staff from the database
        stmt = db.select(Staff).filter_by(id=staff_id)
        staff = db.session.scalar(stmt)
        #if staff exists
        if staff:
            #update fields provided in the request
            staff.name = body_data.get("name") or staff.name
            staff.position=body_data.get("position") or staff.position
            staff.username = body_data.get("username") or staff.username
            staff.role=body_data.get("role") or staff.role
            staff.is_admin=body_data.get("is_admin") or staff.is_admin
            
            #if password if provided update and hashh
            if password in body_data:
                staff.password = bcrypt.generate_password_hash(body_data["password"]).decode("utf-8")
            #commit to db
            db.session.commit()
            #return response
            return staff_schema.dump(staff), 200
        #return error if staff does not exist
        return {"error": "Staff does not exist"}, 404
    except IntegrityError as err:
        return handle_integrity_error(err)

    
        

