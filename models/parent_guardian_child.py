from init import db, ma

from marshmallow import fields



class ParentGuardianChild(db.Model):
    __tablename__ = "parent_guardian_child" 
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"))
    parent_guardian_id = db.Column(db.Integer, db.ForeignKey("parent_guardian.id"))
    relationship_to_child =  db.Column(db.String, nullable=False) #mother, father, aunt, sister, legal guardian    
    
    #define relationship to child table and parent_guardian table (SINGULAR)
    child = db.relationship("Child", back_populates="parents_guardians_children")
    parent_guardian = db.relationship("ParentGuardian", back_populates="parents_guardians_children")
    
#create schema
class ParentGuardianChildSchema(ma.Schema):

    child = fields.Nested("ChildSchema", only=["name"])
    parent_guardian = fields.Nested("ParentGuardianSchema", only=["name"])
    
    class Meta:
        fields = ("id", "child", "parent_guardian", "relationship_to_child")

parent_guardian_child_schema = ParentGuardianChildSchema()
parents_guardians_children_schema = ParentGuardianChildSchema(many=True)