from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.daily_checklist import Dailychecklist, daily_checklist_schema, daily_checklists_schema
from models.child import Child
from models.staff import Staff
from controllers.auth_controller import role_required


#daily_checklists blueprint registered to the children_bp because it is part of a child record 
daily_checklists_bp = Blueprint("daily_checklists", __name__, url_prefix="/<int:child_id>/daily_checklists")

#Create CRUD operations
#Getting all the checklists wouldn't make much sense as most likely we'd need to get a checklist for a particular child. No need to create a GET method to retrieve all the checklists


# @daily_checklists_bp.route("/", methods=["GET"])
# def get_all_daily_checklists(daily_checklists):
#     stmt = db.select(Dailychecklist).order_by(Dailychecklist.date.desc())
#     daily_checklits = db.session.scalars(stmt)
#     return daily_checklists_schema.dump(daily_checklists)

#GET - /<int:child_id>/daily_checklists - create a new daily checklist
@daily_checklists_bp.route("/", methods=["POST"])
@jwt_required()
def create_daily_checklist(child_id):
    body_data = request.get_json()
    #get the child with a particular id - child_id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child exists
    if child:
        #get id of staff member logged in
        staff_id = get_jwt_identity()
        #create an instance of the Dailychecklist model
        daily_checklist = Dailychecklist(
            child_id=child.id,
            date=date.today(),
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
    
#DELETE - delete a daily checklist - /children/child_id/daily_checklists/daily_checklist_id
@daily_checklists_bp.route("/<int:daily_checklist_id>", methods=["DELETE"])
@role_required("admin")
def delete_daily_checklist(child_id, daily_checklist_id):
    #get daily_checklist from db with daily_checklist is
    stmt = db.select(Dailychecklist).filter_by(id=daily_checklist_id)
    daily_checklist = db.session.scalar(stmt)
    #if daily_checklist exists
    if daily_checklist:
        #delete
        db.session.delete(daily_checklist)
        db.session.commit()
        #return
        return {"message": f"Comment '{daily_checklist}' deleted successfully"}   
    #else
    else:
        return {"error": f"Daily Checklist with id '{daily_checklist_id}' not found"}, 404
    
#PUT, PATCH - update/edit daily checklist - /children/child_id/daily_checklists/daily_checklist_id
@daily_checklists_bp.route("/<int:daily_checklist_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_daily_checklist(child_id, daily_checklist_id):
    body_data = request.get_json()
    stmt = db.select(Dailychecklist).filter_by(id=daily_checklist_id)
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
        
    

