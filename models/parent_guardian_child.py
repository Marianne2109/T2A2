from init import db, ma

from marshmallow import fields
from marshmallow.validate import Length


#create model for junction table parent_guardian_child
class ParentGuardianChild(db.Model):
    __tablename__ = "parent_guardian_child" 
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"), nullable=False)
    parent_guardian_id = db.Column(db.Integer, db.ForeignKey("parent_guardian.id"), nullable=False)
    relationship_to_child =  db.Column(db.String, nullable=False) #mother, father, aunt, sister, legal guardian    
    
    #adding UniqueConstraint method to avoid data duplication and ensuring that child-parent_guardian relationship remains unique
    __table_args__ = (db.UniqueConstraint("child_id", "parent_guardian_id", name="_child_parent_uc"),)
    
    #define relationship to child table and parent_guardian table 
    child = db.relationship("Child", back_populates="parents_guardians_children")
    parent_guardian = db.relationship("ParentGuardian", back_populates="parents_guardians_children")

#create schema
class ParentGuardianChildSchema(ma.Schema):
    #nested fields to include fields from the related schemas - in this case name only 
    child = fields.Nested("ChildSchema", only=["name"], required=True)
    parent_guardian = fields.Nested("ParentGuardianSchema", only=["name"], required=True)

    #add length validation for relationship to child
    relationship_to_child = fields.String(required=True, validate=Length(min=3))
    
    class Meta:
        fields = ("id", "child", "parent_guardian", "relationship_to_child")

parent_guardian_child_schema = ParentGuardianChildSchema()
parents_guardians_children_schema = ParentGuardianChildSchema(many=True)