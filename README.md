# API Web Server Application

## Link
- GitHub repo:
- Trello board: ![Trello](https://trello.com/b/zp0dHkrS/a2t2-api-webserver)
  
###How to use
To operate this application follow the next steps:
1. Open the src folder in the Terminal
2. Create and launch a virtual enviroment for the application with the following command
  
   `python3 -m venv .venv && source .venv/bin/activate`

3. Clone this repository on your local machine
4. If it's not already installed, install PostgreSQL
 * Run PostgreSQL 
 * Create a database in PostgreSQL. I used _childcare_db_
 * Create a user called named as you like. I used _staff_childcare_ 
 * Grant all database privileges to the newly created user
5. Install the required libraries for the API into the virtual environment using the following command
   
    `pip3 install -r requirements.txt`
   
6. Create a .env file in the root directory and copy the variables from .envsample file into it
 * Set your own secret key, database URL with childcare_db and the username staff_childcare on your machine
   
    ```DATABASE_URI= "postgresql+psycopg2://{your_postgres_user}:{passowrd_of_user}@localhost:5000/{your_database}"
     JWT_SECRET_KEY="secret" ```
    
7. To create the database run `flask db create`
8. To seed the data from CLI commands into the database run `flask db seed`
9. To run the application use `flask run`
10. To delete the tables and reset the database run `flask db drop`

## R1. Explain the problem that this app will solve and explain how this app solves or addresses the problem. 
For this project, I am creating a basic API web application for the Management of a Childcare Center. 
It is designed to support administrators and educators by providing a simple way of accessing the information of a child, supporting easy day to day records such as feeding times, nappy changing, naps and more. 
Without a web application these daily tasks have to be recorded in pen and paper and kept in clipboards or binders. This application supports the workflow for all staff members by automating and organising these records.
It also provides access to important information about a child such as health records and carers details allowing for a deeper insight into the child in a holistic way. This in term would allow for educators to feel more connected to the children improving their capacity to be more present in the room and ultimately improve the overall quality of the care provided. 
This app will create a keep record for each child's details, their carers details, health record and daily checklist. Staff members have different levels of access depending on their role within the centre. 
Child Care Centers of varying sizes use third party softwares to support the management of the centre and to collect data that can be used for mandatory reporting to the State or Territory and Federal Government. The use of these platforms has a significant cost that at times small centres struggle to cover. Having a simple web application can assist with the overall efficiency of the centres’ management while assisting with data collection and data that can be extrapolated and used to secure funding (“Early Childhood Education and Care: Unit record level NMDS 2021)

## R2. Describe the way tasks are allocated and tracked in your project. 
For project management and task tracking I used ![Trello](https://trello.com/b/zp0dHkrS/a2t2-api-webserver)
I divided the tasks into 5 categories:
* Backlog
* To do
* Doing
* Testing
* Done

For each category I created cards and checklists within. The process was fluid and when I identified the need some elements in the checklists were transformed into its own card. I regularly updated these cards and checklists by adding items or ticking and unticking as I progressed through each task. I also made comments when needed to keep track of the progress or blocks along the way. At times I worked across elements in different cards which I expected to happen given that I was working by myself. I often referred back to the trello board to check for progress and task management.
I used a Kanban template from Trello that I edited to suit my project needs. Some of examples of the cards created in the photos below.

## R3. List and explain the third-party services, packages and dependencies used in this app.

* **Flask:** Flask is one of the most popular python-based web application frameworks that will be imlemented in this application. Known for its simplicity and extensibility from Flask libraries. Flask is based on Jinja2 template and Werkzeug WSGI toolkit which implements requests, responses and utility that are the base for the web frame to be built on. Often referred to as a microframework, Flask is designed to keep the base of an application simple and scalable by leveraging on extensions and libraries. 

* **SQLAlchemy**: SQLAlchemy SQL Toolkit and Object Relational Mapper (SQLAlchemy ORM) is a set of tools for working with databases and Python by translating classes to tables on relational databases and convert function calls to SQL statements. In my application it is used to interact with the PostgreSQL database and to perform CRUD operations through SQL statements.

* **Psycopg2**: Psycopg - currently in version 2.0 - is the PostgreSQL database adapter for Python allowing Python code to execute PostgreSQL commands in a database session. This allows for real time data synchronisation while maintaining the connection between Python and the database. In this application Psycopg2 is the adapter used to connect to PostgreSQL.

* **Marshmallow**: Marshmallow is an object serialisation and deserialisation library that converts complex datatypes to and from native Python datatypes. In this application, it is used to create the schemas in each model, serialisation using the dump method, filtering data using the only parameter or deserialisation using the load method and validation using schema.load. Flask_marshmallow adds features such as URL and hyperlinks. 

* **JWT Extended**: JWT Extended is a Python extension that allows the implementation of JSON Web Token (JWT) for authentication. In my application it is used to authenticate the admin for certain actions like create and delete.
 
* **Bcrypt**: Flask Bcrypt is an extension that provides hashing utilities. It is intentionally structured to be slow so it is hard to crack. Bcrypt is recommended to protect sensitive data such as passwords. In this application it is used to improve security of staffs’ passwords so they are not saved in plain text.

* **Python Dotenv**: Python Dotenv is a library  that allows setting and handling environment variables by storing them in a separate file called .env instead of hardcoding them. This prevents issues when different developers access the code by preventing issues caused by different settings. Therefore it keeps consistency across different environments. 

## R4. Explain the benefits and drawbacks of this app’s underlying database system.

The database system used for my API is PostgreSQL. PostgreSQL is a free, open-source database management system with a range of capabilities that makes it flexible and resilient. 
Its benefits include the possibility of adding custom data types, operators and functions to expand the database capabilities to store and manipulate complex data. 
PostgreSQL is ACID (Atomicity, Consistency, Isolation, Durability) compliant guaranteeing reliable transaction support.
It is considered highly secured as it has security features and the possibility of enhancing security through extensions or features like user and password authentication, role-based access control to name some. 

In regard to drawbacks, PostgreSQL  can be complex to manage particularly for users that are not experienced. For instance, compared to other database management systems such as MySQL, PostgreSQL can present a stepper learning curve given that it is comparatively more technical. 

Another disadvantage that can present in certain applications, is that PostgreSQL does not support NoSQL features which relate to storing unstructured data. This would be the case of applications that need flexible data models such as social media applications.

## R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

Object Relational Mapping (ORM) is a tool designed to help in the interaction of the object oriented language (in this case Python) with a relational database (in this case, PostgreSQL), creating a connection between them. Traditionally, interactions with a database involve writing extensive raw SQL queries that often turn repetitive and  error-prone. With ORM a developer creates an object and saves it, reducing repetitive code, the ORM translates the code to the relational model of the database. The developer is in control of the organisation and structure of the database while the library takes on automating redundant tasks.

The ORM used in my application is SQLAlchemy. The purpose of using SQLAlchemy is to define the database schema using Python classes with a clear syntax. Each class corresponds to a table in the database and each attribute represents a column in a table. The relationship between tables is handled through object properties. 
After the models and relationships are defined we can create CRUD operations which are fundamental operations for interacting with a database. CRUD stands for creating, reading, updating and deleting. The HTTP methods used are GET, POST, PUT/PATCH and DELETE, these are handled through requests.
* Create (POST): Used to insert records into the database. For example adding a new entry for "Child" would be POST operation.
* Read (GET): Used when we are wanting to retrieve data from the database. Based on our query we can retrieve a single entry or multiple entries. For example to retrieve the health record of a child would be a GET operation
* Update (POST/PATCH): Used to edit data in the database. PATCH updated part of the table and PUT replaces the whole table. For example to a POST/PAST operation would be used to change the email of a parent.
* Delete (DELETE): Removes data. For example to remove a staff from the database. 

The endpoints in the Flask application corresponds with these operations. 

My application uses SQLALchemy to define the models ("HealthRecord"), each instance of the class represents a row in the respective table ("health_record") in the database. The relationship between the tables or entities, like the relationship between Child and HealthRecord are manage by references. These references are what SQLAlchemy identify as foreign keys. 
Understanding the ORM of our application is essential to leverage from the power of SQLAlchemy and minimise issues that are related to the database.


## R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.

For my flask application, the Entity Relationship Diagram visually represents the five entities and one junction table. A total of six entities will make the structure of the database. 

![ERD-T2A2.]()

These are:
* **Staff = table name: staff:** This table stores information about staff members, including their role and access levels.
The attributes in this table are: is, name, position, username, password, role, is_admin

* **Parent Guardian = table name parent_guardian:** The purpose of this table is to store information about the parent or legal guardian. This table was purposely created to store the details of one parent or guardian.However, in a real life scenario, a Childcare Center will probably store information about two parents or one parent and one guardian. To keep the scope of the project manageable for me, I opted for having one parent or one legal guardian. 
The attributes in this table are: id, name, phone and email

* **Child = table name: child:** The purpose of this table is to store the information of the children enrolled in the Childcare Center. 
The attributes in this table are: id, name, date of birth (dob), emergency contact 1 and emergency contact 2

* **Health Record = table name: health_record:** This table contains the information related to a child's health and medical history.
The attributes in this table are: id, immunisation status, known allergies, health conditions, General Practitioner (GP), medicare number, ambulance cover. 

* **Daily Checklist = table name: daily_checklist:** This table tracks information relating to the care of a child daily including a comments column.
The attributes in this table are: id, date, sunscreen, sleep, bottles, breakfast, morning tea, lunch, afternoon tea, comments, entered by and child id

* **Parent Guardian Child = table name: parent_ guardian_child:** This is the junction table in my ERD. The purpose of this table is to manage the many-to-many relationship between parents/guardian and children. A child can have many parents/guardian and parents/guardian can have an association with many children. This table also stores the information related to the relationship of the parent/guardian to the child. This is because the guardian can be an aunt, grandparent, older siblings or a foster carer. 
The attributes in this table are: id, child id, parent or guardian id and relationship to the child.

The relationship present in the database are: 

* **Many-to-many:** previously described, this relationship is between parent/guardian and child and it is represented by the junction table “parent guardian child”.
* **One-to-one:** This is the relationship between a child and health record. One child can have only one health record and there is one health record per child.
* **One-to-many:** this is the relationship between child and daily checklist where a child can have multiple daily checklists, but each checklist is specific to a child
* **Many-to-one:** this is the relationship between staff and daily checklist. A checklist is completed or entered by a staff member but many staff members can enter checklists. This relationship helps with identifying which staff member entered the data for a particular checklist. 

In the design phase, the visual input provided by the ERD, helped me with making the association between the tables and with identifying the connection between the foreign key in one table that connects to a primary key in the other end of the relationship.

For example in my application, _“entered_by”_ in the Daily Checklist table is a foreign key that represents the _staff_id_ in the Staff table, this creates the connection between the daily checklist and the staff table by the staff completing the Daily checklist. 

Another example is the relationship between Health Record table and Child table, with this table structure, we ensure that the health information is related to the child directly which makes it easier to retrieve when required. When I was planning this application, my idea was that if a staff needs quick access to all the information related to a child, for contacting the parents or checking medical information, everything would be linked to a child therefore easy to access if needed. 

Initially the staff table was planned to be a stand alone table within the database, but after the first ERD was drawn, I realised that the daily checklist information was linked to a child but also to the staff member who completed the checklist. That created the relationship between child and staff tables. 

In relation to the data normalisation or the process of organising the data to minimise data redundancy to keep data integrity. This process is done through stages called Normal forms. 

The **_First Normal Form (1NF)_** eliminates repeating groups, this includes no duplicated rows or columns, a primary key must be present, each column must have one value per row and one value per cell.

The **_Second Normal Form (2NF)_** says that 1NF has been fulfilled and all the attributes are fully dependent on the primary key, so 2NF eliminates redundancy.

The **_Third Normal Form (3NF)_** says that 2NF has been fulfilled and that each attribute is independent of each other. There are more Normal Forms, but 1NF, 2NF and 3NF are the most important ones. 

In my application for example, if there was no normalisation at all, it would be one table with many columns, redundant and disorganised. 
Table name child with attributes: id, name, date of birth, parent-name, parent-phone, parent-email, health-immunisation status, health-allergies, checklist-date, checklist-sunscreen, staff-name, staff-role, staff-username, etc. 

Applying 1NF means that the attributes would be separated in different tables. For example: 
* Table - child: id, name, date of birth, etc
* Table - parent/guardian: id, name, phone, email, etc
* Table - health record: id, immunisation status, allergies, etc
* Table - staff: id, name, position, username, etc.

If tables are well defined then there is no need to make changes, but for example if the child table had information such as staff position or parent phone the 2NF would have to be applied because staff information is not directly dependent on the child's table primary key and neither is the parent phone number. Those attributes belong in the staff and parent tables respectively. 

## R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation. 

Based on the structure established in the ERD during the planning phase, the implementation of the models in my API that will define the structure of the database and how each model fits into the logic behind the database. 

The Child model is the most important or the base model because of its relationship to several other models. The fields in the child model are id, name, date of birth, emergency contact 1 and emergency contact 2. This model has a relationship with Health Record and Daily checklist models, represented by the foreign key “child_id” in the Health Record and Daily Checklist tables. A child can have one Health record (one-to-one) and a child can have many daily checklists (one-to-many). The Child model does not have any foreign keys but serves as a foreign key (child_id) to the tables mentioned above. The foreign key ensures that the connection between tables remains consistent; for example, a health record or a daily checklist cannot reference a child that does not exist.

![code snippet childclass]()

In the code above, the primary key in the child model is defined by the id, we specify that name, dob and emergency contact 1 cannot be null. Next we define the relationship of the child model to other models, in this case the relationship to the Parent Guardian Child, Daily checklist and health record models. We also add an additional setting `cascade=all, delete-orphan`, so if a child instance is deleted the other attributes associated with that child will automatically be deleted. This efficiently handles changes in the database keeping the integrity of the data. 
The Staff model relationship to the Daily checklist model is represented by the foreign key “entered_by” to connect with the staff member entering the data using the “staff_id”. This provides a way of tracking who made particular changes. The staff model does not have foreign key but it serves as a foreign key in the Daily checklist model.

![code snippet]()

In the code we can see that entered_by is a foreign key connecting to the staff model by the staff_id attribute and that is set to not null, therefore, the staff id must be included, the logic is that the daily checklist must be completed by a staff, without a staff member the checklist cannot be completed. 
The relationship between the Child and Parent Guardian models is many-to-many - parents can have many children and a child can have more than one parent. The relationship is facilitated by a junction table. 

![snippet parent guardian child]()

 The junction table turns a many-to-many relationship into two one-to-many relationships. The foreign key referencing in the Parent Guardian Child model are the primary keys of the Child and Parent Guardian models. In my application I included an attribute for the relationship to the child, which is an attribute exclusive to the unique relationship between the child_id and the parent_guardian_id hence its located in the junction table. This adds to the flexibility and scalability of the Parent Guardian Child model.
Because parents can have many children, in order to prevent data redundancy I added a UniqueConstraint so the relationship between one parent or guardian and one child remains unique. 

```
__table_args__ = (db.UniqueConstraint("child_id", "parent_guardian_id", name="_child_parent_uc"),)
```

Having clearly defined models and schemas was essential to create an application that can manage the data efficiently maintaining data integrity and consistency. 
There are other entities that could be added for example an entity for the staff member positions but I tried to create an application that was possible for me to handle effectively.

## R8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint
* HTTP verb
* Path or route
* Any required body or header data
* Response 

### Authentication Routes

### Staff registration: `POST - /auth/register`
This route handles creation and registration of staff members. For the purpose of this project this route will handle creating a new staff instance as well as the registration of the staff to the database.
* Request body data:
  * Name - name of the staff member
  * Position - position of the staff (Lead educator, Educator, Manager etc)
  * Username - unique username assigned to staff member
  * Password - staff members password        
  * Role - staff or admin
* Response:
  * Successfully created, 201: if successful a new staff member will be created and registered into the database 
  * Missing column, 409
  * Username not unique - error ”username already in use”

### Staff login - `POST - /auth/login`
This route allows staff to login after registration
* Request body data:
  * Username - unique username assigned to staff member
  * Password - staff members password
* Response:
  * Successful login, 201: allows a staff to login, it returns username, is_admin (true or false) and token
  * Invalid username or password, 401



### Delete staff - `DELETE - /auth/staffs/<int:staff_id>`
Route to delete a staff member. Requires to be logged in as an admin. The staff_id to be deleted is passed through the route.
* Request body data: not required. 
* Response:
  * Successfully deleted, 200:
  * Staff id not found, 404

### Update staff - `PUT/PATCH - /auth/staffs/<int:staff_id>`
This route allows updating a staff member's details. Requires to be logged in as an admin. 
* Request body data:
  * Name - staff members name
  * Position - staff member position
  * Username - unique username assigned to the staff member
  * Password - staff members password (optional)
  * Role - admin or staff
  * Is_admin - true or false
* Response:
  * Successful update, 200: update intended fields and save changes into the database
  * Staff does not exist, 404


### Staff Routes 

### Get all staff - `GET - /staffs`
This route was created to fetch all the staff members currently registered in the database. Requires to be logged in as an admin.
* Request body data: not required 
* Response:
  * Successful, 200: Returns the details of all staff members currently stored in the database

### Get single staff - `GET - /staffs/<int:staff_id>`
This route is to fetch the details of a particular staff member using the staff member id. Requires to be logged in as an admin.
* Request body data: not required 
* Response:
  * Successful, 200: Returns the details of a specific staff member.
  * Error, 404: Error message indicating staff member not found

### Child Routes 

### Get all children - `GET - /children`
This route is used to fetch all children from the database. Requires to be logged in as an admin.
* Request body data: not required 
* Response:
  * Successful, 200: Returns the details of all children members currently stored in the database

### Get a single child - `GET - /children/<int:child_id>`
This route is used to fetch the information of a child based on the ID. Requires to be logged in as an admin.
* Request body data: not required 
* Response:
  * Successful, 200: Returns the details of the child.
  * Error, 404: returns error message “child not found”.

### Create child - `POST - /children`
This route handles creation of a new child instance. Requires admin role to be logged in. 
* Request body data:
  * Name - name of the child
  * DOB - Date of birth in format YYYY-MM-DD
  * Emergency contact 1: Name of emergency contact 1 
  * Emergency contact 2: Name of emergency contact 2
* Response:
  * Successfully, 200: This will see a new child instance created and saved into the database

### Delete child - `DELETE - /children/<int:child_id>`
This route is used to delete child information. Requires to be logged in as an admin. The child_id to be deleted is passed through the route.
* Request body data: not required 
* Response:
  * Successfully deleted, 200
  * Child id not found, 404

### Update child - `PUT, PATCH - /children/<int:child_id>`
This route allows updating the information of a particular child. Requires to be logged in as an admin. 
* Request body data:
  * Name - name of the child
  * DOB - Date of birth in format YYYY-MM-DD
  * Emergency contact 1: Name of emergency contact 1 
  * Emergency contact 2: Name of emergency contact 2
* Response:
  * Successful update, 200: the updated fields will be saved to the database
  * Child id not found, 404

### ParentGuardian Routes 

### Get a single parent or guardian information - `GET - /children/<int:child_id>/parents_guardians/<int:parent_guardian_id>`
This route allows access to the details of a particular parent or guardian for a particular child. Required to be logged in as staff or admin 
* Body request: not required 
* Response: Returns the details of the parent or guardian

### Create parent or guardian - `POST - /children/<int:child_id>/parents_guardians`
This route handles creation of a new parent or guardian for a particular child. Requires admin role to be logged in. 
* Request body data:
  * Name - name of parent or guardian
  * email - parent or guardian email
  * Phone: phone number
* Response:
  * Successfully, 200: will create a new instance of the parent or guardian and saved it to the database 
  * Error,400: error message, child id not found

### Delete parent or guardian - `DELETE - /children/<int:child:id>/parents_guardians/<int:parent_guardian_id>`
This route allows deleting the record of a parent or guardian. Requires admin to be logged.
* Body of the request: not required. 
* Response:
  * Successful,201: parent or guardian successfully deleted
  * Error 404: Child id not found

### Update parent guardian - `PUT, PATCH - /children/<int:child_id>/parents_guardians/<int:parent_guardian_id>`
This route allows updating the parent or guardian details. It requires login as admin. 
* Request body data: 
  * name
  * email
  * phone
* Response:
  * Successful: update attributes accordingly 
  * Error 404, Returns error message, parent or guardian id not found. 

### ParentGuardianChild Routes 

#### Get a particular parent guardian relationship - `GET- /children/<int:child_id>/parents_guardians/<int:parent_guardian_id>`
This route allows access to the details of a particular parent or guardian for a particular child. Required to be logged in as staff or admin 
* Body request: not required 
* Response: Returns the details of the parent or guardian

**I spend tha majority of the time trying to debug the routes for POST, DELETE and PUT/PATCH. I could not get to retrieve the intended response. Possibly related to the schema, with a invalid input message. I tried everything and I kept on recieving errors. While it is not what is required in the question, I decided to copy my code and the Pseudocode as a way of explaining the logic used.** 


### Create parent guardian child relationship - POST 

```
# POST - /children/<int:child_id>/parents_guardians_children - create new parent_guardian_child relationship for a child
@parent_guardian_child_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_parent_guardian_child_relationship(child_id):
    try:
        body_data = parent_guardian_child_schema.load(request.get_json())
    except ValidationError as err:
        return{"error": err.messages}, 400

    #fetch the child
    child = db.session.get(Child, child_id)
    if not child:
            return {"error": f"Child with id '{child_id}' not found"}, 404
        
    #fetch parent/guardian
    parent_guardian_id = body_data.get("parent_guardian_id")
    parent_guardian = db.session.get(ParentGuardian, parent_guardian_id)
    if not parent_guardian:
        return {"error": f"Parent or Guardian with id '{parent_guardian_id}' not found"}, 404
    
    #create the relationship
    parent_guardian_child = ParentGuardianChild(
        child_id=child.id,
        parent_guardian_id=parent_guardian.id,
        relationship_to_child=body_data.get["relationship_to_child"] #Includes relationship to the child
    )
    
    db.session.add(parent_guardian_child)
    db.session.commit()
    
    return parent_guardian_child_schema.dump(parent_guardian_child), 201
``` 

Pseudocode: 
1. Define the function `create_parent_guardian_child_relationship` and pass the parameter `child_id`
2. Load the data from the JSON request to the parent_guardian_child schema
3. Try to deserialise the data if it fails return error message
4. Use child_if to fetch child from the database'
5. If child does not exist, return error
6. Use parent_guardian_id to fetch the parent_guardian from the database
7. If parent/guardian does not exist, return error
8. Create the new instance of the relationship in ParentGuardianChild
9. Use the child_id and parent_guardian id to create the parent_guardian_child_id
10. create the relationship from the data in the body of the request
11. Add the new instance parent_guardian_child_relationship to the session
12. Commit to the database
13. Return ParentGuardianInstance with status 201 successful. 


#### Delete parent guardian child relationship - DELETE

```
#DELETE - /children/<int:child_id>/parents_guardians_children/<int:parent_guardian_child_id> - delete parent_guardian relationship for a child
@parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_parent_guardian_child_relationship(child_id, parent_guardian_child_id):
    stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
    parent_guardian_child = db.session.scalar(stmt)
    if parent_guardian_child:
        db.session.delete(parent_guardian_child)
        db.session.commit()
        return {"message": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' deleted successfully"}
    else:
        return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"}, 404
```        
Pseudocode:
1. Define the function `delete_parent_guardian_child_relationship` and pass the parameters `child_id`and `parent_guardian_child_id`
2. Create the query statement `stmt` to find the relationship in ParentGuardianChild filtering by child_id and parent_guardian_child_id 
3. Retrive the specific instance of the parent_guardian_child_relationship
4. If the relationship exist, delete from the database
5. Saved the changes through commit 
6. Return message that the relationship was successfully deleted
7. Or else return message that the relationship was not found

#### Update parent guardian child relationship - PUT, PATCH

```
#PUT, PATCH - /children/<int:child_id>/parents_guardians_children/<int:parent_guardian_child_id> - update/edit a parent_guardian relationship for a child
@parent_guardian_child_bp.route("/<int:parent_guardian_child_id>", methods=["PUT", "PATCH"])
@jwt_required()
@role_required("admin")
def update_parent_guardian_child_relationship(child_id, parent_guardian_child_id):
    body_data = parent_guardian_child_schema.load(request.get_json())
    stmt = db.select(ParentGuardianChild).filter_by(child_id=child_id, id=parent_guardian_child_id)
    parent_guardian_child =db.session.scalar(stmt)
    if parent_guardian_child:
        parent_guardian_child.relationship_to_child = body_data.get("relationship_to_child") or parent_guardian_child.relationship_to_child
        
        db.session.commit()
        
        return parent_guardian_child_schema.dump(parent_guardian_child)
    
    else:
        return {"error": f"Parent or Guardian relationship with id '{parent_guardian_child_id}' for child with id '{child_id}' not found"}, 404
```
Pseudocode:
1. Define the function `update_parent_guardian_child_relationship` and pass the parameters `parent_guardian_child_id`
2. Load the data from the JSON request to the parent_guardian_child schema
3. Create the statement to deserialise from ParentGuardianChild using child_id and parent_guardian_child_id as filter.
4. Check if the relationship exists
5. If the relationship exists:
6. Update the required fields
7. Commit to save the changes in the database
8. Return the updated instance and serialise with `dump`
9. Or else, return error message that the particular relationship was not found. 


#### HealthRecord Routes 

#### Get child health record  - `GET - /children/<int:child_id>/health_records/<int:health_record_id>`
This route allows the retrieval of the health record of a child. The role requirement is for staff to be logged in.
* Request body data: not required
* Response:
  * Successful: it will return the information from the health record
  * Error: Health record id or child id not found.

### Create health record - `POST - /children/<int:child_id>/health_records`
This route allows the creation of the health record for a child. It requires the role of admin to be created.
* Request body data:
  * Immunisation status - if this is up to date or incomplete 
  * Allergies - indicates if the child is allergic by stating the allergen
  * Health conditions - this column will include any known medical conditions or health concerns
  * GP - include the general practitioner details 
  * Medicare - for the input of a child's medicare number 
  * Ambulance cover - for the record of an ambulance cover if needed
  * Child_id: this is the foreign key connecting the child with a health record
* Response: 
  * Successful, 201: if successful the data passed through the body of the request will be saved to the table in the database
  * Error, 404: if the child Id is not found

### Delete health record - `DELETE - /children/<int:child_id>/health_records/<int:health_record_id>`
This route allows you to delete a health record for a child (child_id). It requires an admin role.
* Body data request: Not required
* Response:
  * Successful, returns message “Health record (health_record_id) deleted successfully”
  * Error, 404: returns error message “Child (id) not found”

### Edit health  record - `PUT, PATCH - /children/<int:child_id>/health_records/<int:health_records_id>`
The purpose of this route is to edit the details of a child's health record. It requires admin authorisation level to perform the changes. 
* Body data request: This will include the attributes that will be edited
  * Immunisation status
  * Allergies
  * Health conditions
  * GP
  * Medicare
  * Ambulance Cover 
  * Child id
* Response:
  * Successful, 201: Returns the data reflecting field changes in the table saved into the database 
  * Error, 404: Returns error message “Health record for child id not found”

### Dailychecklist Routes

### Get all daily checklists for a particular child  - `GET - /children/<int:child_id>/daily_checklists`
This route has the intended purpose of retrieving all daily checklists for a particular child. Given that while developing this project, the tables were dropped several times along the way therefore there is no record of previous daily checklists other than the ones seeded into the project for testing purposes. I have no reason to believe that this route wouldn’t work as intended. 
* Request body data: not required.
* Response: 
  * Successful: returns the checklists for a particular child id. 

### Get a daily checklist for a child for a particular date - `GET - /children/<int:child_id>/daily_checklists/filter_date?date=<int:dateYYYY-MM-DD>`
This route is created with the purpose of retrieving a daily checklist for a particular child (child_id) by a particular date. Using a pre-filter method passed through the URL is possible to access a table based on a specific value, in this case, the date.  Both staff and admin have the required authorisation to action this. 
* Request body data: not required. The filter and date requires are passed through the URL filter_date?=<int:dateYYYY-MM-DD>’
* Response:
  * Successful: a successful response will see the retrieval of a particular daily checklist based on the date. Similar to the previous request, because the tables were dropped several times during the development stage I don’t have other data other than what’s been seeded into the database. The parameters  in the code are set for date.today for all new records
  * Error, 400: Returns error message “Daily checklist for child (child_id) for date (date_required) not found”

### Create daily checklist - `POST - /children/<int:child_id>/daily_checklists`
The purpose of this route is to create a daily checklist for a child. The date for each recorded date is set as date.today() so there is not need to enter that parameter when completing the checklist. Both staff and admin can create a new checklist.
* Request body data: the following parameters are part of the list are part of the list including examples of the expected responses
  * Date - set as date.today()
  * Sunscreen - Applied am, applied pm, na
  * Sleep - 1 hour, half hour
  * Nappies - wet nappy, soiled nappy changed
  * Bottles - 1, 2, na, 
  * Breakfast - half, all, touched, na
  * Morning tea - half, na, didn’t like it, etc
  * Lunch - all, half, etc  
  * Afternoon tea - na, all, half
  * Comments - “Child had a good day, was happy”, “Child was a bit sad today” 
* Response:
  * Successful: a successful response will see the information passed in the body request saved into the table in the database. We’ll see the data displayed adding fields like child_id, daily_checklist_id and entered_by indicating the staff member who completed the checklist.
  * Error, 400: Returns error message “Daily checklist for child (child_id) for date (date_required) not found”

### Delete daily checklist - `DELETE - /children/<int:child_id>/daily_checklists/<int:daily_checklists_id>`
This route purpose is to delete daily checklists associated with a child id. It requires admin authorisation. 
* Request body data: not required, the child id and checklist id are passed in the URL
* Response:
  * Successful: a successful request will see a daily checklist deleted and a message displayed “Daily checklist deleted successfully”
  * Error: if not successful a message will be displayed “daily checklist (id) not found

### Update daily checklist - `PUT, PATCH - /children/<int:child_id>/daily_checklists/<int:daily_checklists_id>`
This route deals with editing or updating a daily checklist. Admin and staff have authorisation to perform updates.
* Request Body data: The fields that can be entered for changes are,
  * Sunscreen
  * Sleep
  * Nappies
  * Bottles
  * Breakfast
  * Morning_tea
  * Lunch
  * Afternoon_tea
  * Comments
* Response:
  * Successful: a successful response will see the information from the body of the request, updated and saved to the database. 
  * Error, 400: Returns error message “Daily checklist for child (child_id) not found”

## Reference list
1. 2.4. Populating a Table With Rows 2024, PostgreSQL Documentation.
2. Basic Relationship Patterns — SQLAlchemy 2.0 Documentation 2024, docs.sqlalchemy.org.
3. Cascades — SQLAlchemy 2.0 Documentation 2024, docs.sqlalchemy.org, viewed 25 July 2024, <https://docs.sqlalchemy.org/en/20/orm/cascades.html#passive-deletes>.
4. Chris, K 2022, Database Normalization – Normal Forms 1nf 2nf 3nf Table Examples, freeCodeCamp.org.
5. Declaring Models — Flask-SQLAlchemy Documentation (2.x) n.d., flask-sqlalchemy.palletsprojects.com.
6. Early Childhood Education and Care: Unit Record Level NMDS 2021 2022.
7. Flask - Role Based Access Control 2024, GeeksforGeeks.
8. Flask-Bcrypt — Flask-Bcrypt 1.0.1 documentation n.d., flask-bcrypt.readthedocs.io.
9. How To Use Many-to-Many Database Relationships with Flask-SQLAlchemy | DigitalOcean n.d., www.digitalocean.com.
10. maggiesMSFT 2024, Filter a report using query string parameters in the URL - Power BI, learn.microsoft.com.
11. Philosophy - SQLAlchemy 2024, www.sqlalchemy.org.
12. Pre-filtering tables through URL - wpDataTables - Tables and Charts Plugin n.d., wpDataTables - Tables and Charts WordPress Plugin.
13. Quickstart — marshmallow 3.21.3 documentation n.d., marshmallow.readthedocs.io.
14. Role-based Authorization — Flask-User v1.0 documentation n.d., flask-user.readthedocs.io.
15. The psycopg2 module content — Psycopg 2.9.10.dev1 documentation n.d., www.psycopg.org.
16. Validators — marshmallow 3.21.3 documentation n.d., marshmallow.readthedocs.io.
17. Vannier, J 2022, Everything You Need to Know to Map SQL Tables to REST Endpoints in Python - CoderPad, coderpad.io.
18. What is Flask Python - Python Tutorial 2021, pythonbasics.org. 


