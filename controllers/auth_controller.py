from datetime import timedelta
from functools import wraps

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import bcrypt, db
from models.staff import Staff, staff_schema, StaffSchema

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

#define role structure/hierarchy
role_access = {
    "admin": 2,
    "staff": 1
}

#create decorator function for role based authorisation
def role_required(required_role):
    def role_decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_staff_id = get_jwt_identity()
            current_staff = Staff.query.get(current_staff_id)
            if not current_staff or role_access.get(current_staff.role,0) < role_access.get(required_role, 0):
                return {"error": "Access denied"}, 403
            return fn(*args, **kwargs)
        return wrapper
    return role_decorator
    

#create route to register staff member to the database
@auth_bp.route("/register", methods=["POST"])
def register_staff():
    try:    #get data from the body of the request
        body_data = request.get_json()
        #create an instance of the staff model
        staff = Staff(
            name=body_data.get("name"),
            username=body_data.get("username")
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
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE.VIOLATION:
            return {"error": "Username already in use"}, 409

#login user route. Use POST request due to data in body requirements. 
@auth_bp.route("/login", methods=["POST"])
def login_user():
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
        return {"username": staff.username, "is_admin": staff.is_admin, "token": token}
    #else - if the staff doesn't exist or wrong password
    else:
        return {"error": "Invalid username or password"}, 401
