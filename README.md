# API Web Server Application

## Link
- GitHub repo:
- Trello board:

## R1. Explain the problem that this app will solve and explain how this app solves or addresses the problem. 
For this project, I am creating a basic API web application for the Management of a Childcare Center. 
It is designed to support administrators and educators by providing a simple way of accessing the information of a child, supporting easy day to day records such as feeding times, nappy changing, naps and more. 
Without a web application these daily tasks have to be recorded in pen and paper and kept in clipboards or binders. This application supports the workflow for all staff members by automating and organising these records.
It also provides access to important information about a child such as health records and carers details allowing for a deeper insight into the child in a holistic way. This in term would allow for educators to feel more connected to the children improving their capacity to be more present in the room and ultimately improve the overall quality of the care provided. 
This app will create a keep record for each child's details, their carers details, health record and daily checklist. Staff members have different levels of access depending on their role within the centre. 
Child Care Centers of varying sizes use third party softwares to support the management of the centre and to collect data that can be used for mandatory reporting to the State or Territory and Federal Government. The use of these platforms has a significant cost that at times small centres struggle to cover. Having a simple web application can assist with the overall efficiency of the centres’ management while assisting with data collection and data that can be extrapolated and used to secure funding (“Early Childhood Education and Care: Unit record level NMDS 2021)

## R2. Describe the way tasks are allocated and tracked in your project. 
For project management and task tracking I used Trello LINK
I divided the tasks into 5 categories:
* Backlog
* To do
* Doing
* Testing
* Done

For each category I created cards and checklists within. The process was fluid and when I identified the need some elements in the checklists were transformed into its own card. I regularly updated these cards and checklists by adding items or ticking and unticking as I progressed through each task. I also made comments when needed to keep track of the progress or blocks along the way. At times I worked over items across different cards which I expected to happen given that I was working by myself. 
I used a Kanban template from Trello that I edited to suit my project needs. Some of examples of the cards created:

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
After the models and relationships are defined we can create CRUD operations which are fundamental operations for interacting with a database. CRUD stands for creating, reading, updating and deleting. The methods used are GET, POST, PUT, PATCH and DELETE, these are handled through requests.
