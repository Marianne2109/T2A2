from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.staff import Staff
from models.child import Child
from models.parent_guardian import ParentGuardian
from models.daily_checklist import Dailychecklist
from models.parent_guardian_child import ParentGuardianChild

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
           is_admin=True,
           ),
       
        Staff(
           name="Casey Hendrics",
           position="Center Coordinator",
           username="caseyh",
           password=bcrypt.generate_password_hash("789789").decode("utf-8"),
           is_admin=True,
           ),
        
        Staff(
           name="Penny Fisherman",
           position="Assistant Center Coordinator",
           username="pennyf",
           password=bcrypt.generate_password_hash("123123").decode("utf-8"),
           is_admin=True,
           ),   

        Staff(
           name="Sandy Salas",
           position="Lead Educator",
           username="sandys",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           ),    

        Staff(
           name="La Karp",
           position="Educator",
           username="lak",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           ),

        Staff(
           name="Tyra King",
           position="Educator",
           username="tyrak",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           ),  
        
        Staff(
           name="Sara Clark",
           position="Food Services",
           username="sarac",
           password=bcrypt.generate_password_hash("456456").decode("utf-8"),
           )
   ]
   
   db.session.add_all(staffs)
   
   #create a list instances for Child
   children = [
        Child(
         name="Eve Bandicoot",
         dob="01-01-2021", 
         emergency_contact_1="Will Bandicoot",
         emergency_contact_2="Mary Bandicoot",
      ),
        Child(
         name="Rose Bandicoot",
         dob="19-03-2023", 
         emergency_contact_1="Will Bandicoot",
         emergency_contact_2="Mary Bandicoot",
      ),
        Child(
         name="Cooper Smith",
         dob="26-12-2020", 
         emergency_contact_1="Jack Smith",
         emergency_contact_2="Carol Smith",
      ),
        Child(
         name="Hunter Smith",
         dob="06-01-2023", 
         emergency_contact_1="Jack Smith",
         emergency_contact_2="Carol Smith",
      ),
        Child(
         name="Isobel Harrison",
         dob="26-07-2022", 
         emergency_contact_1="Bec Harrison",
         emergency_contact_2="Luka Jones",
      ),
        Child(
         name="Frankie Kloss",
         dob="06-05-2021", 
         emergency_contact_1="Erin Kloss",
         emergency_contact_2="Sandra Kloss",
      )        
   ]
   
   db.session.add_all(children)
   
   db.session.commit()
   
   print("Tables Seeded")