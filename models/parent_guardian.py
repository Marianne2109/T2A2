from init import db, ma

from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class ParentGuardian(db.Model):
    __tablename__ = "parent_guardian"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
   
    
    #define relationship to parent_guardian_child junction table
    parents_guardians_children = db.relationship("ParentGuardianChild", back_populates="parent_guardian")
    
#create schema
class ParentGuardianSchema(ma.Schema):
    #nested field schema - relationship to junction table
    parents_guardians_children = fields.List(fields.Nested("ParentGuardianChildSchema", exclude=["parent_guardian"]))
    
    #add validation for name, phone, email
    name = fields.String(required=True, validate=And(
                         Length(min=4, error="Name must be at least four characters long"), 
                         Regexp("^[a-zA-Z0-9 ]+$", error="Name must contain alphanumeric characters only")
                         ))
    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid Email Format"))

    class Meta:
        fields = ("id", "name", "phone", "email")

parent_guardian_schema = ParentGuardianSchema()
parents_guardians_schema = ParentGuardianSchema(many=True)