import pandas as pd
from datetime import datetime, timedelta
import pymysql
import sqlalchemy
from sqlalchemy.sql import text  # Import required for SQL text expressions


# Import variables module 
from variables.core import *
from variables.auth import *
from variables.user import *


# Import sql module
from sql.auth import *


pymysql.install_as_MySQLdb()

# Connection details
username = 'root'
password = 'cb5rqwak'
host = 'localhost'
port = '3306'
database = 'coveer_db'  # Define the database name here for better reusability

pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Managing the database creation and setup
with engine.begin() as connection:
    # Drop the existing database if it exists
    connection.execute(text('DROP DATABASE IF EXISTS coveer_db;'))
    # Create the database
    connection.execute(text('CREATE DATABASE coveer_db;'))
    # Use the newly created database
    connection.execute(text('USE coveer_db;'))
    print('DATABASE is setup successfully')
    
   
# auth tables creation
with engine.begin() as connection:
    # .variables/auth tables 
    connection.execute(create_users_table)
    connection.execute(create_social_logins_table)
    connection.execute(create_password_resets_table)
    connection.execute(create_logs_table)
    print('AUTH tables are setup successfully')



# users tables creation
with engine.begin() as connection:
    # .variables/core tables 
    connection.execute(create_company_table)
    connection.execute(create_creators_table)
    connection.execute(create_table_follower)
    print('USER tables are setup successfully')   
    


# core tables creation
with engine.begin() as connection:
    # .variables/core tables 
    connection.execute(create_campaigns_table)
    connection.execute(create_event_campaigns_table)
    connection.execute(create_table_participation)
    print('CORE tables are setup successfully')


# create procedure auth creation
with engine.begin() as connection:
    # .sql/auth USER PROCEDURE
    connection.execute(create_add_user_procedure)
    connection.execute(create_modify_user_procedure)
    connection.execute(create_get_user_procedure)
    connection.execute(create_delete_user_procedure)
    print('user procedure added successffully')
    
    # reset passsword procedure 
    connection.execute(create_generate_reset_token_procedure)
    connection.execute(create_verify_reset_token_procedure)
    connection.execute(create_mark_token_used_procedure)
    print('reset password procedure added successffully')
    
    
    # Log table procedure 
    connection.execute(create_add_log_procedure )
    connection.execute(create_modify_log_procedure)
    connection.execute(create_delete_log_procedure)
    connection.execute(create_get_log_procedure)
    print('reset password procedure added successffully')
    
    
    
    
     