# Import sql module
from sql.auth import *
from sql.user import *
from sql.core import *

def setup_procedure(engine):  
    with engine.begin() as connection:
         ### SETUP DES TABLES AUTH #########   
        # .sql/auth USER PROCEDURE
        connection.execute(create_add_user_procedure)
        connection.execute(create_modify_user_procedure)
        connection.execute(create_get_user_procedure)
        connection.execute(create_delete_user_procedure)
        connection.execute(create_login_user_procedure)
        connection.execute(create_verify_email_procedure)
        print('user procedure added successffully')
        
        # reset passsword procedure 
        connection.execute(create_generate_reset_token_procedure)
        connection.execute(create_update_password_procedure)
        connection.execute(create_flag_user_procedure )
        print('reset password procedure added successffully')
        
        
        # Log table procedure 
        connection.execute(create_add_log_procedure )
        connection.execute(create_modify_log_procedure)
        connection.execute(create_delete_log_procedure)
        connection.execute(create_get_log_procedure)
        connection.execute(create_get_log_user_procedure)
        print('log procedure added successffully')
        
        

        ### SETUP DES PROCEDURE USER #########        
        
        # Companies-related procedures
        connection.execute(create_add_company_procedure)
        connection.execute(create_get_company_procedure)
        connection.execute(create_modify_company_procedure)
        print('Company procedures added successfully.')

        # Creators-related procedures
        connection.execute(create_add_creator_procedure)
        connection.execute(create_get_creator_procedure)
        connection.execute(create_modify_creator_procedure)
        print('Creator procedures added successfully.')

        # Followers-related procedures
        connection.execute(create_add_follower_procedure)
        connection.execute(create_get_follower_procedure)
        connection.execute(create_modify_follower_procedure)
        print('Follower procedures added successfully.')
        
        
        ## SETUP DES PROCEDURE CORE ###
        
        # Campaigns
        connection.execute(create_add_campaign_procedure)
        connection.execute(create_modify_campaign_procedure)
        connection.execute(create_delete_campaign_procedure)
        connection.execute(create_get_campaign_procedure)
        print('Campaign procedures added successfully.')
        
        # Event Campaigns-related procedures
        connection.execute(create_add_event_campaign_procedure)
        connection.execute(create_get_event_campaign_procedure)
        connection.execute(create_modify_event_campaign_procedure)
        connection.execute(create_delete_event_campaign_procedure)
        print('Event Campaign procedures added successfully.')

        # Campaign Participation-related procedures
        connection.execute(create_add_participation_procedure)
        connection.execute(create_get_participation_procedure)
        connection.execute(create_modify_participation_procedure)
        connection.execute(create_delete_participation_procedure)
        print('Campaign Participation procedures added successfully.')
                
        