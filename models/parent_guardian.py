from init import db, ma

from marshmallow import fields

class Parent_Guardian(db.Model):
    __tablename__ = "parent_guardian"
    
    id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    
    #define relationship to parent_guardian_child junction table
    parent_guardian_child = db.relationship("Parent_Guardian_Child", back_populates="parent_guardian")
    
#create schema
class Parent_GuardianSchema(ma.Schema):
    #nested field schema - relationship to junction table
    parents_guardians_children = fields.List(fields.Nested("Parent_Guardian_ChildSchema", exclude=["parent_guardian"]))
    
    class Meta:
        fields = {"id", "name", "phone", "email"}

parent_guardian_schema = Parent_GuardianSchema()
parents_guardians_schema = Parent_GuardianSchema(many=True)