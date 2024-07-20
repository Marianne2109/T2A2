from datetime import date

from init import db, ma
from marshmallow import fields 
from sqlalchemy.ext.hybrid import hybrid_property
from models.parent_guardian_child import ParentGuardianChild


class Child(db.Model):
    __tablename__ = "child"
     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    emergency_contact_1 = db.Column(db.String, nullable=False)
    emergency_contact_2 = db.Column(db.String)
    
    #change dob format to dd-mm-yyyy
    @hybrid_property
    def dob_formatted(self):
         return self.dob.strftime("%d/%m/%Y")
    
    
      #define relationship to parent_guardian_child junction table (PLURAL)
    parents_guardians = db.relationship("ParentGuardian", back_populates="child")
    #define relationship to daily_checklist table (plural)
    daily_checklists = db.relationship("Dailychecklist", back_populates="child")
    
  
    
#create child schema
class ChildSchema(ma.Schema):
    #nested field schema - relationship to daily_checklist table
    daily_checklists = fields.List(fields.Nested("DailychecklistSchema", exclude=["child"]))
    
    #nested field schema - relationship to junction table
    parents_guardians_children = fields.List(fields.Nested("ParentGuardianChildSchema", exclude=["child"]))
    
    class Meta:
        fields = ("id", "name", "dob", "emergency_contact_1", "emergency_contact_2")

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)