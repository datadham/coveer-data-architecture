from sqlalchemy import create_engine, text


# AUTH PROCEDURE FOR ADD GET MODIFY DELETE USER 

create_add_user_procedure = text('''
CREATE PROCEDURE AddUser(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_profile_type VARCHAR(100)
)
BEGIN
    DECLARE v_token VARCHAR(6);
    DECLARE email_exist BOOLEAN DEFAULT FALSE;
    
    -- Generate a 6-digit random token
    SET v_token = LPAD(FLOOR(RAND() * 999999), 6, '0');

    -- Check if the email already exists
    SELECT COUNT(*) INTO email_exist
    FROM users 
    WHERE email = p_email;

    IF email_exist = 0 THEN
        -- Insert new user
        INSERT INTO users (email, password_hash, profile_type, email_verification_token, created_at)
        VALUES (p_email, SHA2(p_password, 256), p_profile_type, v_token, NOW());
        
        -- Return success message
        SELECT 'User registered successfully.' AS Message, v_token as Token;
    ELSE
        -- Return error message
        SELECT 'Email already exists.' AS Message;
    END IF;
END''')

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
    IN p_new_profile_type VARCHAR(100),
    IN p_flag_access TINYINT(1)
)
BEGIN
    UPDATE users 
    SET password_hash = IF(p_new_password IS NOT NULL, SHA2(p_new_password, 256), password_hash),
        profile_type = IF(p_new_profile_type IS NOT NULL, p_new_profile_type, profile_type),
        flag_access = IF(p_flag_access IS NOT NULL, p_flag_access, flag_access),
        updated_at = NOW()
    WHERE email = p_email;
    SELECT 'User updated successfully.' AS Message;
END;''')

create_verify_email_procedure = text('''
  CREATE PROCEDURE VerifyEmail(
    IN p_email VARCHAR(255),
    IN p_token VARCHAR(6)
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE token VARCHAR(6);

    -- Retrieve the user_id and token associated with the given email
    SELECT user_id, email_verification_token INTO p_user_id, token
    FROM users
    WHERE email = p_email;

    -- Check if the user_id was retrieved
    IF p_user_id IS NULL THEN
        SELECT 'No user found' AS Message;
    ELSE
        -- Check if the token matches
        IF token = p_token THEN
            UPDATE users
            SET email_verified = 1,
                updated_at = NOW()
            WHERE user_id = p_user_id;
            SELECT 'Token valid email is verified' AS Message, 1 AS Result;
        ELSE
            SELECT 'Token is not valid' AS Message, 0 AS Result;
        END IF;
    END IF;
END;
                          
             ''')


create_login_user_procedure = text("""CREATE PROCEDURE LoginUser(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    -- Declare a variable to store the fetched password hash from the database
    DECLARE v_password_hash VARCHAR(256);
    DECLARE v_user_id INT;
    DECLARE v_flag_access TINYINT(1);

    -- Declare a variable to store the result
    DECLARE v_result BOOLEAN DEFAULT FALSE;

    -- Retrieve the password hash
    SELECT password_hash, flag_access, user_id INTO v_password_hash,v_flag_access,v_user_id
    FROM users
    WHERE email = p_email;

    -- Check if the password is correct
    IF v_password_hash IS NOT NULL AND v_password_hash = SHA2(p_password, 256) AND v_flag_access = 1  THEN
        SET v_result = TRUE;  -- User verified successfully
        
        -- Insert the log entry
        INSERT INTO logs (user_id, event_type, description)
        VALUES (v_user_id, 'login_attempted','success');
    
    ELSE 
         -- Insert the log entry
        INSERT INTO logs (user_id, event_type, description)
        VALUES (v_user_id, 'login_attempted','failed');
    END IF;

    -- Return the result
    SELECT v_result AS Result;
END;""")



create_flag_user_procedure = text('''
                        CREATE PROCEDURE FlagUser(
                            IN p_email VARCHAR(255)
                        )
                        BEGIN
                            -- Update the flag_access field for the specified email
                            UPDATE users
                            SET flag_access = 0,
                                updated_at = NOW()
                            WHERE email = p_email;
                        END;
                        ''')

### PASSWORD RESET ###
create_generate_reset_token_procedure = text('''CREATE PROCEDURE GenerateResetToken(
    IN p_email VARCHAR(255)
)
BEGIN
    DECLARE v_token VARCHAR(10);
    DECLARE v_expiration_date DATETIME;
    DECLARE v_user_id VARCHAR(100);

    -- Retrieve the user_id based on the provided email
    SELECT user_id INTO v_user_id
    FROM users
    WHERE email = p_email;

    -- Check if the user_id is found
    IF v_user_id IS NOT NULL THEN
        -- Generate a random 6-digit token
        SET v_token = LPAD(FLOOR(RAND() * 9999999999), 6, '0');
        -- Set the expiration date to 24 hours from now
        SET v_expiration_date = DATE_ADD(NOW(), INTERVAL 24 HOUR);

        -- Insert the reset token into the password_resets table
        INSERT INTO password_resets (user_id, reset_token, expiration_date, used)
        VALUES (v_user_id, v_token, v_expiration_date, 0);
        
        -- Return the generated token
        SELECT v_token AS ResetToken;
    ELSE
        -- Return 0 if the user is not found
        SELECT 0 AS ResetToken;
    END IF;
END''')


# Update password procedure 
create_update_password_procedure = text('''CREATE PROCEDURE UpdatePassword(
    IN p_email VARCHAR(255),
    IN p_reset_token VARCHAR(6),
    IN p_new_password VARCHAR(255)
)
BEGIN
    DECLARE v_user_id INT;
    DECLARE p_reset_id INT;
    DECLARE v_current_time DATETIME;
    DECLARE v_token_count INT;

    -- Initialize current time
    SET v_current_time = NOW();

    -- Get user_id based on the provided email
    SELECT user_id INTO v_user_id
    FROM users 
    WHERE email = p_email;

    -- Get reset_id based on the provided reset_token and user_id
    SELECT reset_id INTO p_reset_id
    FROM password_resets
    WHERE reset_token = p_reset_token
    AND user_id = v_user_id;

    -- Verify the reset token
    IF v_user_id IS NOT NULL THEN
        -- Check if the reset token is valid and not expired
        SELECT COUNT(*) INTO v_token_count
        FROM password_resets
        WHERE user_id = v_user_id
        AND reset_token = p_reset_token
        AND expiration_date > v_current_time
        AND used = 0;

        -- Return result based on token validity
        IF v_token_count > 0 THEN
            SELECT 'Token is valid' AS Message;

            -- Mark the token as used
            UPDATE password_resets
            SET used = 1
            WHERE reset_id = p_reset_id
            AND user_id = v_user_id;

            -- Update user's password
            UPDATE users
            SET password_hash = SHA2(p_new_password, 256),
                updated_at = NOW()
            WHERE user_id = v_user_id;
        ELSE
            SELECT 'Token is invalid or expired' AS Message;
        END IF;
    ELSE
        SELECT 'Email not found' AS Message;
    END IF;
END                                
''')




### LOGS PROCEDURE ##
create_add_log_procedure = text('''CREATE PROCEDURE AddLog(
    IN p_email VARCHAR(255),
    IN p_event_type VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    DECLARE user_id INT;

    -- Get the user_id based on the provided email
    SELECT user_id INTO user_id
    FROM users 
    WHERE email = p_email;

    -- Check if user_id is found
    IF user_id IS NOT NULL THEN
        -- Insert the log entry
        INSERT INTO logs (user_id, event_type, description)
        VALUES (user_id, p_event_type, p_description);

        SELECT 'Log entry added successfully.' AS Message;
    ELSE
        -- If no user_id is found, return a message
        SELECT 'User not found.' AS Message;
    END IF;
END;''')

create_modify_log_procedure = text('''CREATE PROCEDURE ModifyLog(
    IN p_log_id INT,
    IN p_description TEXT
)
BEGIN
    UPDATE logs
    SET description = p_description
    WHERE log_id = p_log_id;
    SELECT 'Log entry updated successfully.' AS Message;
END;''' )

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

create_get_log_user_procedure = text('''CREATE PROCEDURE GetUserLog(
    IN p_email VARCHAR(255)
)
BEGIN
    DECLARE v_user_id INT;

    -- Get the user_id based on the provided email
    SELECT user_id INTO v_user_id
    FROM users 
    WHERE email = p_email;

    -- Check if user_id is found
    IF v_user_id IS NOT NULL THEN
        SELECT * FROM logs
        WHERE user_id = v_user_id;
    ELSE 
        -- If no user_id is found, return a message
        SELECT 'User not found.' AS Message;
    END IF;
END;''')