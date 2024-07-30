from datetime import datetime
from functools import wraps

from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity 
from models.staff import Staff
from marshmallow.exceptions import ValidationError

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



#create validation function for dob input not future date
def validate_date_not_future(date):
    if date > datetime.today().date():
        raise ValidationError("Date of birth cannot be in the future.")
