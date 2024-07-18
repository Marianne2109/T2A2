from flask import Blueprint

from init import db, bcrypt
from models.staff import Staff

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
   #create a list of Staff instances
   staffs = [
       Staff(
           name="Amanda Harrison",
           position="Center Manager",
           username="amandah",
           password=bcrypt.generate_password_hash("123456").decode("utf-8"),
           is_admin=True
           ),
       
        Staff(
           name="Casey Hendrics",
           position="Center Coordinator",
           username="caseyh",
           password=bcrypt.generate_password_hash("789789").decode("utf-8"),
           is_admin=True
           ),
        
        Staff(
           name="Penny Fisherman",
           position="Assistant Center Coordinator",
           username="pennyf",
           password=bcrypt.generate_password_hash("123123").decode("utf-8"),
           is_admin=True
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
           ), 
   ]
   
   db.session.add_all(staffs)
   
   db.session.commit()
   
   print("Tables Seeded")