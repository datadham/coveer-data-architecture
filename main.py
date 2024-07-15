import pandas as pd
from datetime import datetime, timedelta
import pymysql
import sqlalchemy
from sqlalchemy.sql import text  # Import required for SQL text expressions

from functions.schema import setup_schema
from functions.procedure import setup_procedure 


pymysql.install_as_MySQLdb()

# Connection details
username = 'root'
password = 'cb5rqwak'
host = 'localhost'
port = '3306'
#database = 'coveer_db'  # Define the database name here for better reusability

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}")

# Managing the database creation and setup
with engine.begin() as connection:
    # Drop the existing database if it exists
    connection.execute(text('DROP DATABASE IF EXISTS coveer_db;'))
    # Create the database
    connection.execute(text('CREATE DATABASE coveer_db;'))
    # Use the newly created database
    connection.execute(text('USE coveer_db;'))
    print('DATABASE is setup successfully')

# Setup all the tables 
setup_schema(engine)

# setup all the procedure 
setup_procedure(engine)



    
    
     