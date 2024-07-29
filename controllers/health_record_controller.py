from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.health_record import HealthRecord, health_record_schema, health_records_schema
from models.child import Child
from controllers.auth_controller import role_required
from marshmallow.exceptions import ValidationError

#health record blueprint registered to the children_bp because it is part of a child record 
health_records_bp = Blueprint("health_records", __name__, url_prefix="/<int:child_id>/health_records")


#GET - /children/<int:child_id>/health_records/<int:health_record_id> - get health record of a child    
@health_records_bp.route("/<int:health_record_id>", methods=["GET"])
@jwt_required()
@role_required("staff")
def get_health_record(child_id, health_record_id):
    # stmt = db.select(HealthRecord).filter_by(child_id=child_id).order_by(HealthRecord.date.desc())
    health_record  = db.session.query(HealthRecord).filter_by(id=health_record_id, child_id=child_id).first()
    if health_record:
        return health_record_schema.dump(health_record)  
    else:
        return {"error": f"Health Record with id '{health_record_id}' not found for child '{child_id}'"}, 404    
 
#POST - /<int:child_id>/health_records - create a new health record
@health_records_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_health_record(child_id):
    try:
        body_data = health_record_schema.load(request.get_json())
    except ValidationError as err:
        return{"error": err.messages}, 400
    #fetch child with specific id         
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    #if child exists
    if child:
        health_record = HealthRecord(
            child_id=child.id,
            immunisation_status=body_data.get("immunisation_status"),
            allergies=body_data.get("allergies"),
            health_condition=body_data.get("healt_condition"),
            GP=body_data.get("GP"),
            medicare_number=body_data.get("medicare_number"),
            ambulance_cover=body_data.get("ambulance_cover")            
        )
        
        db.session.add(health_record)
        db.session.commit()
        return health_record_schema.dump(health_record), 201
    else:
        return {"error": f"Child with id '{child_id}' not found"}, 404
    
#DELETE - /children/child_id/health_records/health_record_id
@health_records_bp.route("/<int:health_record_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_health_record(child_id, health_record_id):
    stmt = db.select(HealthRecord).filter_by(id=health_record_id)
    health_record = db.session.scalar(stmt)
    if health_record:
        db.session.delete(health_record)
        db.session.commit()
        return {"message": f"Health Record '{health_record_id}' deleted successfully"}
    else:
        return {"error": f"Health Record with id '{health_record_id}' not found"}, 404
    
#PUT, PATCH - /children/child_id/health_records/health_record_id
@health_records_bp.route("/<int:health_record_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("admin") 
def edit_health_record(child_id, health_record_id):
    try:
        body_data = health_record_schema.load(request.get_json())
    except ValidationError as err:
        return{"error": err.messages}, 400
    #fetch health record           
    body_data = health_record_schema.load(request.get_json(), partial=True)
    stmt = db.select(HealthRecord).filter_by(id=health_record_id)
    health_record = db.session.scalar(stmt)
    if health_record:
        health_record.immunisation_status=body_data.get("immunisation_status") or health_record.immunisation_status
        health_record.allergies=body_data.get("allergies") or health_record.allergies
        health_record.health_condition=body_data.get("health_condition") or health_record.health_condition
        health_record.GP=body_data.get("GP") or health_record.GP    
        health_record.medicare_number=body_data.get("medicare_number") or health_record.medicare_number
        health_record.ambulance_cover=body_data.get("ambulance_cover") or health_record.ambulance_cover 
        
        db.session.commit()
        return health_record_schema.dump(health_record)
    else:
        return {"error": f"Health Record with id '{health_record_id}' not found"}, 404      

