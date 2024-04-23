from sqlalchemy import create_engine, text


# AUTH PROCEDURE FOR ADD GET MODIFY DELETE USER 

create_add_user_procedure =text("""
CREATE PROCEDURE AddUser(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_profile_type VARCHAR(100)
)
BEGIN
    DECLARE v_token VARCHAR(6);
    SET v_token = LPAD(FLOOR(RAND() * 999999), 6, '0');
    INSERT INTO users (email, password_hash, profile_type, email_verification_token)
    VALUES (p_email, SHA2(p_pass word, 256), p_profile_type, v_token);
    SELECT 'User registered successfully.' AS Message;
END;
""")

create_get_user_procedure = text('''
    CREATE PROCEDURE GetUser(IN p_email VARCHAR(255))
    BEGIN
        SELECT * FROM users WHERE email = p_email;
    END ;''')

create_delete_user_procedure = text('''
    CREATE PROCEDURE DeleteUser(IN p_email VARCHAR(255))
    BEGIN
        DELETE FROM users WHERE email = p_email;
        SELECT 'User deleted successfully.' AS Message;
    END;
    ''')

create_modify_user_procedure =text('''CREATE PROCEDURE ModifyUser(
    IN p_email VARCHAR(255),
    IN p_new_password VARCHAR(255),
    IN p_new_profile_type VARCHAR(100)
)
BEGIN
    UPDATE users 
    SET password_hash = IF(p_new_password IS NOT NULL, SHA2(p_new_password, 256), password_hash),
        profile_type = IF(p_new_profile_type IS NOT NULL, p_new_profile_type, profile_type)
    WHERE email = p_email;
    SELECT 'User updated successfully.' AS Message;
END;''')


#--------------------------------------------------------------------------------------------------#
### PASSWORD RESET
#--------------------------------------------------------------------------------------------------#

create_generate_reset_token_procedure = text('''CREATE PROCEDURE GenerateResetToken(
        IN p_user_id INT
    )
    BEGIN
        DECLARE v_token VARCHAR(10);
        DECLARE v_expiration_date DATETIME;

        SET v_token = LPAD(FLOORRAND() * 9999999999), 6, '0');
        SET v_expiration_date = DATE_ADD(NOW(), INTERVAL 24 HOUR);

        INSERT INTO password_resets (user_id, reset_token, expiration_date, used)
        VALUES (p_user_id, v_token, v_expiration_date, 0);

        SELECT v_token AS ResetToken;
    END;''')


# check if the token is valid or not 
create_verify_reset_token_procedure = text('''CREATE PROCEDURE VerifyResetToken(
    IN p_user_id INT,
    IN p_reset_token VARCHAR(6),
    IN p_current_time DATETIME
)
BEGIN
    SELECT * FROM password_resets
    WHERE user_id = p_user_id
      AND reset_token = p_reset_token
      AND expiration_date > p_current_time
      AND used = 0;
END;''')


# mark the token as used 
create_mark_token_used_procedure = text('''CREATE PROCEDURE MarkTokenAsUsed(
    IN p_reset_id INT
)
BEGIN
    UPDATE password_resets
    SET used = 1
    WHERE reset_id = p_reset_id;

    SELECT 'Token marked as used.' AS Message;
END;''')




#--------------------------------------------------------------------------------------------------#
### LOGS PROCEDURE 
#--------------------------------------------------------------------------------------------------#


create_add_log_procedure = text('''CREATE PROCEDURE AddLog(
    IN p_user_id INT,
    IN p_event_type VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    INSERT INTO logs (user_id, event_type, description)
    VALUES (p_user_id, p_event_type, p_description);
    SELECT 'Log entry added successfully.' AS Message;
END;)''')



create_modify_log_procedure = text('''CREATE PROCEDURE ModifyLog(
    IN p_log_id INT,
    IN p_description TEXT
)
BEGIN
    UPDATE logs
    SET description = p_description
    WHERE log_id = p_log_id;
    SELECT 'Log entry updated successfully.' AS Message;
END''' ;)


create_delete_log_procedure = text('''CREATE PROCEDURE DeleteLog(
    IN p_log_id INT
)
BEGIN
    DELETE FROM logs
    WHERE log_id = p_log_id;
    SELECT 'Log entry deleted successfully.' AS Message;
END;''')


create_get_log_procedure = text('''CREATE PROCEDURE GetLog(
    IN p_log_id INT
)
BEGIN
    SELECT * FROM logs
    WHERE log_id = p_log_id;
END;''')