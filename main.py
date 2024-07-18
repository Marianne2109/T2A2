import os

from flask import Flask

#Import objects from init.py to connect wih the flask application
from init import db, ma, bcrypt, jwt

#create application factories, we define a function that will contain the app
def create_app():
#create instance of the flask app
    app = Flask(__name__)
    
#write configuration to connect to the database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

#add configuration for jwt secret key
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

#connect objects to the application.
    db.init_app(app) #SQLAlchemy
    ma.init_app(app) #Marshmallow
    bcrypt.init_app(app) #Hash
    jwt.init_app(app) #Json web token

#call the function, should return the instance of the app created   
    return app