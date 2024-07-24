
from init import db, ma 

from marshmallow import fields 

#create the model Staff that extends from the SQLAlchemy class Model so the class Staff becomes a model
#staff model will allow to create register and login staff members into the database
class Staff(db.Model):
    #name of the table
    __tablename__ = "staff"
    
    #attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)    
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default="staff")
    is_admin = db.Column(db.Boolean, default=False)
    
    #define relationship to daily checklist table
    daily_checklists = db.relationship("Dailychecklist", back_populates="staff")
    
#create schema - extends from the Schema class provided by marshmallow
class StaffSchema(ma.Schema):
    #indicate to marshmallow to use Daily_checklist schema, exclude staff
    daily_checklists = fields.List(fields.Nested("DailychecklistSchema", only=["staff_id"]))
    
    class Meta:
        fields = ("id", "name", "position", "username", "password", "role", "is_admin")
        

#define the staff_schema using the class StaffSchema:
#schema for a single staff object
staff_schema = StaffSchema(exclude=["password"])

#schema for a list of staff objects 
staffs_schema = StaffSchema(many=True, exclude=["password"])