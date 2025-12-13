# In Python, a __init__.py file marks a directory as a package
# and controls how that package is initialized and exposed.
# Without __init__.py (in older Python versions), this import would fail.

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importing the elements defined in the model
# Need to import models to ensure they are added do DB
from database_model.base import Base
from database_model.Customer import Customer
from database_model.TravelPlan import TravelPlan

db_path = "database/"
# Check if the directory does not exist
if not os.path.exists(db_path):
   # then create the directory
   os.makedirs(db_path)

# database access URL (this is a local SQLite access URL)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# create the database connection engine
engine = create_engine(db_url, echo=False)

# Instantiate a session creator bound to the database
Session = sessionmaker(bind=engine)

# create the database if it does not exist
if not database_exists(engine.url):
    create_database(engine.url)

# create the database tables if they do not exist
Base.metadata.create_all(engine)