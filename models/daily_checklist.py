from datetime import date

from init import db, ma
from marshmallow import fields

class Daily_checklist(db.Model):
    __tablename__ = "daily_checklist"
     
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    sunscreen = db.Column(db.String) #Ex. Applied am, applied pm, na
    sleep = db.Column(db.String) #Ex. 1 hour, half hour
    nappies = db.Column(db.String) #Ex. wet nappy changed, soiled nappy changed
    bottles = db.Column(db.Integer) #Ex. 1, 2
    breakfast = db.Column(db.String) #Ex. all, half, touched, na
    morning_tea = db.Column(db.String) #Ex. not touched, half, all, na
    lunch = db.Column(db.String) #Ex. not touched, half, all, na
    afternoon_tea = db.Column(db.String) #Ex. not touched, half, all, na
    comments = db.Column(db.String) #Ex. child_name had a good day, child_name had a hard time in the arvo
    entered_by = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"), nullable=False)
    
    #define relationship to staff table
    staff = db.relationship("Staff", back_populates="daily_checklists")
    #define relationship to child
    children = db.relationship("Child", back_populates="daily_checklists")
    
    
#create daily_checklist schema
class Daily_checklistSchema(ma.Schema):
    #indicate to marshmallow that the staff field is a nested field and to use the StaffSchema and only take name field. Same for child relationship
    staff = fields.Nested("StaffSchema", only="name")
    child = fields.Nested("ChildSchema", only="name")
    
    class Meta:
        fields = {"id", "date", "sunscreen", "sleep", "nappies", "bottles", "breakfast", "morning_tea", "lunch", "afternoon_tea", "comments", "entered_by", "child", "staff", "child"}

daily_checklist_schema = Daily_checklistSchema()
daily_checklists_schema = Daily_checklistSchema(many=True)