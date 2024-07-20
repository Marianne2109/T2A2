from init import db, ma

from marshmallow import fields

class ParentGuardian(db.Model):
    __tablename__ = "parent_guardian"
    
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    relationship_to_child =  db.Column(db.String, nullable=False) #mother, father, aunt, sister, legal guardian
    
    #define relationship to parent_guardian_child junction table
    parents_guardians_children = db.relationship("ParentGuardianChild", back_populates="parent_guardian")
    
#create schema
class ParentGuardianSchema(ma.Schema):
    #nested field schema - relationship to junction table
    parents_guardians_children = fields.List(fields.Nested("ParentGuardianChildSchema", exclude=["parent_guardian"]))
    
    class Meta:
        fields = ("id", "name", "phone", "email", "relationship_to_child")

parent_guardian_schema = ParentGuardianSchema()
parents_guardians_schema = ParentGuardianSchema(many=True)