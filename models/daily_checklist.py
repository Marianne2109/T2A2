from datetime import date

from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp, And, Length


class Dailychecklist(db.Model):
    __tablename__ = "daily_checklist"
     
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"), nullable=False) #must belong to a child
    date = db.Column(db.Date, default=date.today, nullable=False)
    sunscreen = db.Column(db.String) #Ex. Applied am, applied pm, na
    sleep = db.Column(db.String) #Ex. 1 hour, half hour
    nappies = db.Column(db.String) #Ex. wet nappy changed, soiled nappy changed
    bottles = db.Column(db.String) #Ex. 1, 2, na
    breakfast = db.Column(db.String) #Ex. all, half, touched, na
    morning_tea = db.Column(db.String) #Ex. not touched, half, all, na
    lunch = db.Column(db.String) #Ex. not touched, half, all, na
    afternoon_tea = db.Column(db.String) #Ex. not touched, half, all, na
    comments = db.Column(db.String) #Ex. child_name had a good day, child_name had a hard time in the arvo
    
    entered_by = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=False) #must be entered by a staff member

    
    #define relationship to child (change to - SINGLE)
    child = db.relationship("Child", back_populates="daily_checklists")
    #define relationship to staff table
    staff = db.relationship("Staff", back_populates="daily_checklists")

alphanumeric = Regexp("^[a-zA-Z0-9 ]+$", error="Include only letter and numbers.")   
    
#create daily_checklist schema
class DailychecklistSchema(ma.Schema):
    #indicate to marshmallow that the staff field is a nested field and to use the StaffSchema and only take name field. Same for child relationship
    child = fields.Nested("ChildSchema", only=["name"])
    staff = fields.Nested("StaffSchema", only=["name"])
    
    sunscreen = fields.String(required=True, validate=And(
                              Length(max=15, error="Number of characters exceed the limit [15 characters]"), alphanumeric))
    sleep = fields.String(required=True, validate=And(
                              Length(max=15, error="Number of characters exceed the limit [15 characters]"), alphanumeric))
    nappies = fields.String(required=True, validate=And(
                              Length(max=20, error="Number of characters exceed the limit [20 characters]"), alphanumeric))
    bottles = fields.String(required=True, validate=And(
                              Length(max=10, error="Number of characters exceed the limit [10 characters]"), alphanumeric))
    breakfast = fields.String(required=True, validate=And(
                              Length(max=10, error="Number of characters exceed the limit [10 characters]"), alphanumeric))
    morning_tea = fields.String(required=True, validate=And(
                              Length(max=10, error="Number of characters exceed the limit [10 characters]"), alphanumeric))
    lunch = fields.String(required=True, validate=And(
                              Length(max=10, error="Number of characters exceed the limit [10 characters]"), alphanumeric))
    afternoon_tea = fields.String(required=True, validate=And(
                              Length(max=10, error="Number of characters exceed the limit [10 characters]"), alphanumeric))
    comments = fields.String(required=True, validate=And(
                              Length(max=50, error="Number of characters exceed the limit [50 characters]"), alphanumeric))
    
    class Meta:
        fields = ("id", "child_id", "date", "sunscreen", "sleep", "nappies", "bottles", "breakfast", "morning_tea", "lunch", "afternoon_tea", "comments", "entered_by")

daily_checklist_schema = DailychecklistSchema()
daily_checklists_schema = DailychecklistSchema(many=True)