from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.daily_checklist import Dailychecklist, daily_checklist_schema, daily_checklists_schema
from models.child import Child
from models.staff import Staff
from controllers.auth_controller import role_required
from marshmallow.exceptions import ValidationError
from datetime import datetime



#daily_checklists blueprint registered to the children_bp because it is part of a child record 
daily_checklists_bp = Blueprint("daily_checklists", __name__, url_prefix="/<int:child_id>/daily_checklists")

#Create CRUD operations
#GET - get all daily checklists for a child
@daily_checklists_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_daily_checklists(child_id):
    stmt = db.select(Dailychecklist).filter_by(child_id=child_id).order_by(Dailychecklist.date.desc())
    daily_checklists = db.session.scalars(stmt)
    return daily_checklists_schema.dump(daily_checklists), 200

#GET - /<int:child_id>/daily_checklists/filter_date?date= - get a daily checklist of child for a particular date by pre filtering data in the URL
@daily_checklists_bp.route("/filter_date", methods=["GET"])
@jwt_required()
@role_required("staff")
def get_daily_checklist(child_id):
    #get data from query
    date_str = request.args.get("date")
    
    #if date is not provided
    if not date_str:
        return {"error": "Date is required"}, 400
    
    #convert date string to object 
    try:
        filter_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
            return {"error": "Invalid date format. Use YYYY-MM-DD"}, 400

    #fetch data from daily checklist
    stmt = db.select(Dailychecklist).filter_by(child_id=child_id, date=filter_date)
    daily_checklist = db.session.scalar(stmt)
    #if daily checklist exists for child id and date
    if daily_checklist:
        return daily_checklist_schema.dump(daily_checklist), 200
    else:
        return {"error": f"No checklist found for child '{child_id}' on date '{filter_date}'"},400
        
#POST - /<int:child_id>/daily_checklists - create a new daily checklist
@daily_checklists_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("staff")
def create_daily_checklist(child_id):
    try:
        body_data = daily_checklist_schema.load(request.get_json())
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    #get the child with a particular id - child_id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child exists
    if child:
        #get id of staff member logged in
        staff_id = get_jwt_identity()
        #create an instance of the Dailychecklist model
        daily_checklist = Dailychecklist(
            child=child,
            date=body_data.get("date", date.today()), #if not provided default date to today
            sunscreen=body_data.get("sunscreen"),
            sleep=body_data.get("sleep"),
            nappies=body_data.get("nappies"),
            bottles=body_data.get("bottles"),
            breakfast=body_data.get("breakfast"),
            morning_tea=body_data.get("morning_tea"),
            lunch=body_data.get("lunch"),
            afternoon_tea=body_data.get("afternoon_tea"),
            comments=body_data.get("comments"),
            entered_by=staff_id
        )
        
        #add and commit the session to the db
        db.session.add(daily_checklist)
        db.session.commit()
        #return created commit
        return daily_checklist_schema.dump(daily_checklist), 201
    #else
    else:
        #return an error
        return {"error": f"Child with id '{child_id}' not found"}, 404 
    
#DELETE  - /children/child_id/daily_checklists/daily_checklist_id - delete a daily checklist
@daily_checklists_bp.route("/<int:daily_checklist_id>", methods=["DELETE"])
@jwt_required()
@role_required("staff")
def delete_daily_checklist(child_id, daily_checklist_id):
    #get daily_checklist from db with daily_checklist is
    stmt = db.select(Dailychecklist).filter_by(id=daily_checklist_id)
    daily_checklist = db.session.scalar(stmt)
    #if daily_checklist exists
    if daily_checklist:
        #delete and commit
        db.session.delete(daily_checklist)
        db.session.commit()
        #return
        return {"message": f"Daily Checklist '{daily_checklist_id}' deleted successfully"}   
    #else
    else:
        return {"error": f"Daily Checklist with id '{daily_checklist_id}' not found"}, 404
    
#PUT, PATCH - /children/child_id/daily_checklists/daily_checklist_id - update/edit daily checklist
@daily_checklists_bp.route("/<int:daily_checklist_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("staff")
def edit_daily_checklist(child_id, daily_checklist_id):
    try:
        body_data = daily_checklist_schema.load(request.get_json(), partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    #fetch daily checklist for a specific child id
    stmt = db.select(Dailychecklist).filter_by(id=daily_checklist_id, child_id=child_id)
    daily_checklist = db.session.scalar(stmt)
    if daily_checklist:
    #update fields
        daily_checklist.sunscreen=body_data.get("sunscreen") or daily_checklist.sunscreen
        daily_checklist.sleep=body_data.get("sleep") or daily_checklist.sleep
        daily_checklist.nappies=body_data.get("nappies") or daily_checklist.nappies
        daily_checklist.bottles=body_data.get("bottles") or daily_checklist.bottles
        daily_checklist.breakfast=body_data.get("breakfast") or daily_checklist.breakfast
        daily_checklist.morning_tea=body_data.get("morning_tea") or daily_checklist.morning_tea
        daily_checklist.lunch=body_data.get("lunch") or daily_checklist.lunch    
        daily_checklist.afternoon_tea=body_data.get("afternoon_tea") or daily_checklist.afternoon_tea 
        daily_checklist.comments=body_data.get("comments") or daily_checklist.comments
        #commit
        db.session.commit()
        return daily_checklist_schema.dump(daily_checklist)
    else:
        return {"error": f"Daily Checklist with id '{daily_checklist_id}' not found"}, 404
        
    

