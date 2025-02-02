
from init import db, ma 

from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

#create the model Staff that extends from the SQLAlchemy class Model so the class Staff becomes a model
#staff model will allow to create register and login staff members into the database
class Staff(db.Model):
    #name of the table
    __tablename__ = "staff"
    
    #attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)    
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default="staff")
    is_admin = db.Column(db.Boolean, default=False)
    
    #define relationship to daily checklist table
    daily_checklists = db.relationship("Dailychecklist", back_populates="staff")
    
#create schema - extends from the Schema class provided by marshmallow
class StaffSchema(ma.Schema):
    #indicate to marshmallow to use Daily_checklist schema
    daily_checklists = fields.List(fields.Nested("DailychecklistSchema", only=["staff_id"]))
        
    #add validation details
    name = fields.String(required=True, validate=Length(min=4, error="Name must contain minimum four characters long"))
    position = fields.String(required=True)
    username = fields.String(required=True, validate=And(
                        Length(min=3),
                         Regexp("^[a-zA-Z]+$", error="Username must contain only letters and minimum three characters long")
                         ))
    password = fields.String(required=True, validate=And(
                             Length(min=6),
                             Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error="Minimum six characters, at least one letter and one number")))
    role = fields.String(required=True)
    is_admin = fields.Boolean(default=False)

    
    class Meta:
        fields = ("id", "name", "position", "username", "password", "role", "is_admin")
        

#define the staff_schema is an instance of StaffSchema:
#schema for a single staff object
staff_schema = StaffSchema(exclude=["password"])

#schema for a list of staff objects 
staffs_schema = StaffSchema(many=True, exclude=["password"])