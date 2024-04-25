# Import sql module
from sql.auth import *
from sql.user import *


def setup_procedure(engine):
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
        print('log procedure added successffully')
        
        
        
        # Companies-related procedures
        connection.execute(create_add_company_procedure)
        connection.execute(create_get_company_procedure)
        connection.execute(create_modify_company_procedure)
        connection.execute(create_delete_company_procedure)
        print('Company procedures added successfully.')

        # Creators-related procedures
        connection.execute(create_add_creator_procedure)
        connection.execute(create_get_creator_procedure)
        connection.execute(create_modify_creator_procedure)
        connection.execute(create_delete_creator_procedure)
        print('Creator procedures added successfully.')

        # Followers-related procedures
        connection.execute(create_add_follower_procedure)
        connection.execute(create_get_follower_procedure)
        connection.execute(create_modify_follower_procedure)
        connection.execute(create_delete_follower_procedure)
        print('Follower procedures added successfully.')
        