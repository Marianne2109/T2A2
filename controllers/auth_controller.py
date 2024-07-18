from datetime import timedelta

from flask import Blueprint, request, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from init import bcrypt
from models.staff import Staff, staff_schema

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

#create routes
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
        if password: #if the password exists
            staff.password = bcrypt.generate_password_hash(password).decode("utf-8")
            
        #add and commit to the DB
        db.session.add(staff)        
        db.session.commit()
        
        #respond back - create the staff info to the frontend
        return staff_schema.dump(staff), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE.VIOLATION:
            return {"error": "Username already in use"}, 409
