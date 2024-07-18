from init import db, ma 

#create the model Staff that extends from the SQLAlchemy class Model so the class Staff becomes a model
class Staff(db.Model):
    #name of the table
    __tablename__ = "staff"
    
    #attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)    
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
#create schema - extends from the Schema class provided by marshmallow
class StaffSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "position", "username", "password", "is_admin")
        

#define the staff_schema using the class StaffSchema:
#schema for a single staff object
staff_schema = StaffSchema(exclude=["password"])

#schema for a list of staff objects 
staffs_schema = StaffSchema(many=True, exclude=["password"])