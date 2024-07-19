from init import db, ma

from marshmallow import fields


class Parent_Guardian_Child(db.Model):
    __tablename__ = "parent_guardian_child"
    
    #junction table - composite primary key and additional row for relationship_to_child information
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"), primary_key=True)
    parent_guardian_id = db.Column(db.Integer, db.ForeignKey("parent_guardian.id"), primary_key=True)
    relationship_to_child =  db.Column(db.String, nullable=False) #mother, father, aunt, sister, legal guardian
    
    #define relationship to child table and parent_guardian table
    children = db.relationship("child", back_populates="parent_guardian_child")
    parents_guardians = db.relationship("parent_guardian", back_populates="parent_guardian_child")
    
#create schema
class Parent_Guardian_ChildSchema(ma.Schema):

    child = fields.Nested("ChildSchema", only="name")
    parent_guardian = fields.Nested("StaffSchema", only="name")
    
    class Meta:
        fields = {"child", "parent_guardian", "relationship_to_child"}

parent_guardian__child_schema = Parent_Guardian_ChildSchema()
parents_guardians_children_schema = Parent_Guardian_ChildSchema(many=True)