from init import db, ma
from marshmallow import fields

class HealthRecord(db.Model):
    __tablename__ = "health_record"
    
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"), nullable=False) #must belong to a child
    immunisation_status = db.Column(db.String, nullable=False) #Ex. up to date, missing _months, missing_vaxx name
    allergies = db.Column(db.String) #Ex, peanuts anaphylaxis, gluten sensitivity, nuts allergies, kiwi 
    health_condition = db.Column(db.String) #cognitive delays, visual impairment, epilepsy, dermatitis, eczma
    GP = db.Column(db.String) #Ex. Dr Kaur - Chelsea Medical, Dr Smith - Arcade at Colins
    medicare_number = db.Column(db.String) #Ex. 456523697 1, 45896214 3, na
    ambulance_cover= db.Column(db.String) #A123H656, D274645, na

    
    #define relationship to child (change to - SINGLE)
    child = db.relationship("Child", back_populates="health_record")
    
    #create schema
class HealthRecordSchema(ma.Schema):
       child = fields.Nested("ChildSchema", only=["name"])
       
       class Meta:
           fields = ("id", "child_id", "immunisation_status", "allergies", "health_condition", "GP", "medicare_number", "ambulance_cover")
           
health_record_schema = HealthRecordSchema()
health_records_schema = HealthRecordSchema(many=True)
    