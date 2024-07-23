from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.staff import Staff
from models.child import Child
from models.parent_guardian import ParentGuardian
from models.parent_guardian_child import ParentGuardianChild
from models.daily_checklist import Dailychecklist
from models.health_record import HealthRecord


db_commands = Blueprint("db", __name__)

#create cli commands
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
   #create a list instances for Staff
   staffs = [
       Staff(
           name="Amanda Harrison",
           position="Center Manager",
           username="amandah",
           password=bcrypt.generate_password_hash("123456").decode("utf-8"),
           role="admin",
           is_admin=True
           ),
       
        Staff(
           name="Casey Hendrics",
           position="Center Coordinator",
           username="caseyh",
           password=bcrypt.generate_password_hash("789789").decode("utf-8"),
           role="admin",
           is_admin=True
           ),
        
        Staff(
           name="Penny Fisherman",
           position="Assistant Center Coordinator",
           username="pennyf",
           password=bcrypt.generate_password_hash("123123").decode("utf-8"),
           role="admin",
           is_admin=True
           ),   

        Staff(
           name="Sandy Salas",
           position="Lead Educator",
           username="sandys",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           role="staff"
           ),    

        Staff(
           name="La Karp",
           position="Educator",
           username="lak",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           role="staff"
           ),

        Staff(
           name="Tyra King",
           position="Educator",
           username="tyrak",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           role="staff"
           ),  
        
        Staff(
           name="Sara Clark",
           position="Food Services",
           username="sarac",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           role="staff"
           )
   ]
   
   db.session.add_all(staffs)
   
   #create a list instances for Child
   children = [
        Child(
         name="Eve Bandicoot",
         dob="2021-01-01", 
         emergency_contact_1="Will Bandicoot",
         emergency_contact_2="Mary Bandicoot"   
      ),
        Child(
         name="Rose Bandicoot",
         dob="2023-03-19", 
         emergency_contact_1="Will Bandicoot",
         emergency_contact_2="Mary Bandicoot"
      ),
        Child(
         name="Cooper Smith",
         dob="2020-12-26", 
         emergency_contact_1="Jack Smith",
         emergency_contact_2="Carol Smith"
      ),
        Child(
         name="Hunter Smith",
         dob="2023-01-06", 
         emergency_contact_1="Jack Smith",
         emergency_contact_2="Carol Smith"
      ),
        Child(
         name="Isobel Harrison",
         dob="2022-07-26", 
         emergency_contact_1="Bec Harrison",
         emergency_contact_2="Luka Jones"
      ),
        Child(
         name="Frankie Kloss",
         dob="2021-05-06", 
         emergency_contact_1="Erin Kloss",
         emergency_contact_2="Sandra Kloss"
      )        
   ]
   
   db.session.add_all(children)
   
   parents_guardians = [
        ParentGuardian(
           name="Mary Bandicoot",
           phone="0424167460",
           email="marybandicoot@email.com"
        ),
        ParentGuardian(
           name="Carol Smith",
           phone="0456896321",
           email="smithcarol@email.com"
        ),
        ParentGuardian(
           name="Erin Kloss",
           phone="234963458",
           email="erinkloss@email.com"
        ),
        ParentGuardian(
           name="Luka Jones",
           phone="0495633145",
           email="lukajones@email.com"
        ),
   ]
   
   db.session.add_all(parents_guardians)
   
   parents_guardians_children = [
        ParentGuardianChild(
           child=children[0],
           parent_guardian=parents_guardians[0],
           relationship_to_child="mother"
        ),
        ParentGuardianChild(
           child=children[1],
           parent_guardian=parents_guardians[0],
           relationship_to_child="mother"
        ),
        ParentGuardianChild(
           child=children[2],
           parent_guardian=parents_guardians[1],
           relationship_to_child="mother"
        ),
        ParentGuardianChild(
           child=children[3],
           parent_guardian=parents_guardians[1],
           relationship_to_child="mother"
        ),
        ParentGuardianChild(
           child=children[4],
           parent_guardian=parents_guardians[3],
           relationship_to_child="father"
        ),
        ParentGuardianChild(
           child=children[5],
         parent_guardian=parents_guardians[2],
           relationship_to_child="step-mother"
        )
   ]
   
   db.session.add_all(parents_guardians_children)
   
   daily_checklists = [
      Dailychecklist(
           child=children[0],
           date=date.today(),
           sunscreen="am and pm",
           sleep="12.50pm-2pm",
           nappies="na",
           bottles="na",
           breakfast="na",
           morning_tea="all",
           lunch="all",
           afternoon_tea="all",
           comments="Eve has a great day!",
           staff=staffs[4]
        ),
      Dailychecklist(
           child=children[5],
           date=date.today(),
           sunscreen="am and pm",
           sleep="na",
           nappies="na",
           bottles="na",
           breakfast="all",
           morning_tea="all",
           lunch="all",
           afternoon_tea="all",
           comments="Frankie loved painting outside!",
           staff=staffs[3]
        ),
      Dailychecklist(
           child=children[3],
           date=date.today(),
           sunscreen="na",
           sleep="11am-12.30pm, 2.45pm-4pm",
           nappies="2 wet, 1 soiled",
           bottles="2",
           breakfast="half",
           morning_tea="all",
           lunch="all",
           afternoon_tea="na",
           comments="Hunter was happy and loved story time",
           staff=staffs[3]
        )
   ]
   
   db.session.add_all(daily_checklists)
   
   health_records = [
      HealthRecord(
         child=children[0],
         immunisation_status="up to date",
         allergies="not known",
         health_condition="",
         GP="Dr.Kaur at Chelsea Arcade",
         medicare_number="4561235 1",
         ambulance_cover="7894562K" 
      ),
      HealthRecord(
         child=children[1],
         immunisation_status="up to date",
         allergies="peanut",
         health_condition="anaphylaxis to peanuts",
         GP="Dr Smith",
         medicare_number="456236 3",
         ambulance_cover="7894562gf"        
      ),
      HealthRecord(
         child=children[2],
         immunisation_status="missing 6 months",
         allergies="not known",
         health_condition="",
         GP="Dr Griss at Family Practice Carrum",
         medicare_number="4563254 2",
         ambulance_cover="45628784klo"         
      ),
      HealthRecord(
         child=children[3],
         immunisation_status="up to date",
         allergies="gluten",
         health_condition="caeliac disease",
         GP="Dr Griss at Family Practice Carrum",
         medicare_number="4563254 3",
         ambulance_cover="45628784klokk"         
      ),
      HealthRecord(
         child=children[4],
         immunisation_status="up to date",
         allergies="no",
         health_condition="hard of hearing, use of hearing aid",
         GP="Dr Chen at Local medical center",
         medicare_number="569852 1",
         ambulance_cover="nckueghr768769"         
      ),
      HealthRecord(
         child=children[5],
         immunisation_status="up to date",
         allergies="no",
         health_condition="asthma",
         GP="Dr Chen at Local medical center",
         medicare_number="558995464",
         ambulance_cover="65659dff"         
      )
      ]

   db.session.add_all(health_records)
   
   db.session.commit()
   
   print("Tables Seeded")