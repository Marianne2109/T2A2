from datetime import datetime

from init import db, ma
from utils import validate_date_not_future #Import validation function for DOB not in the future
from marshmallow import fields 
from marshmallow.validate import Length, And, Regexp



#Create Child model 
class Child(db.Model):
    __tablename__ = "child"
     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    emergency_contact_1 = db.Column(db.String, nullable=False)
    emergency_contact_2 = db.Column(db.String)    
    
    #define relationship to parent_guardian_child junction table (PLURAL), cascade delete setup to automatically detele other records if child is deleted
    parents_guardians_children = db.relationship("ParentGuardianChild", back_populates="child", cascade="all, delete-orphan")
    #define relationship to daily_checklist table (plural)
    daily_checklists = db.relationship("Dailychecklist", back_populates="child", cascade="all, delete-orphan")
    #define relationship to health_record(single)
    health_record = db.relationship("HealthRecord", back_populates="child", cascade="all, delete-orphan")
  
    
#create child schema
class ChildSchema(ma.Schema):
    #nested field schema - relationship to daily_checklist table
    daily_checklists = fields.List(fields.Nested("DailychecklistSchema", exclude=["child"]))
    
    #nested field schema - relationship to junction table
    parents_guardians_children = fields.List(fields.Nested("ParentGuardianChildSchema", exclude=["child"]))
    
    health_record = fields.Nested("HealthRecordSchema", exclude=["child"])
    
    #add validation for length and alphanumeric values for name 
    name = fields.String(required=True, validate=And(
                         Length(min=3, error="Name must be at least three characters long"),
                         Regexp("^[a-zA-Z0-9 ]+$", error="Name must contain alphanumeric characters only")
                         ))
    #add validation for dob, date should not be in the future
    dob = fields.Date(required=True, validate=validate_date_not_future)
    
    #add validation for length and alphanumeric values for emergency_contact
    emergency_contact_1 = fields.String(required=True, validate=
                         Length(min=4, error="Name must be at least four characters long"))
    
    class Meta:
        fields = ("id", "name", "dob", "emergency_contact_1", "emergency_contact_2")

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)