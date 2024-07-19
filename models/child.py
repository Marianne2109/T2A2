from datetime import date

from init import db, ma
from marshmallow import fields 

class Child(db.Model):
    __tablename__ = "child"
     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    room = db.Column(db.String)
    emergency_contact_1 = db.Column(db.String, nullable=False)
    emergency_contact_2 = db.Column(db.String)
    
    #define relationship to daily_checklist table
    daily_checklists = db.relationship("Daily_checklist", back_populates="staff")
    
#create child schema
class ChildSchema(ma.Schema):
    daily_checklists = fields.List(fields.Nested("Daily_checklistSchema", exclude=["child"]))
    
    class Meta:
        fields = {"id", "name", "dob", "room", "emergency_contact_1", "emergency_contact_2"}

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)