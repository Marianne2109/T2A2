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

#GET - /<int:child_id>/daily_checklists - create a new daily checklist
@daily_checklists_bp.route("/", methods=["POST"])
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
