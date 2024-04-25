# Import variables module 
from variables.core import *
from variables.auth import *
from variables.user import *


def setup_schema(engine):
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