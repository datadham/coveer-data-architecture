from sqlalchemy import create_engine, text

######## -------------- COMPANY PROCEDURE------------------------------------------------------------------------------------#################

create_add_company_procedure = text("""CREATE PROCEDURE AddCompany(
    IN p_email VARCHAR(255),
    IN p_name VARCHAR(255),
    IN p_industry VARCHAR(255),
    IN p_address TEXT,
    IN p_website VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE company_exists INT;

    -- Retrieve the user_id associated with the given email
    SELECT user_id INTO p_user_id 
    FROM users 
    WHERE email = p_email;

    -- Check if a company with the same name already exists
    SELECT COUNT(*) INTO company_exists
    FROM companies
    WHERE name = p_name;

    IF company_exists = 0 THEN
        -- Insert the new company if it does not exist
        INSERT INTO companies (user_id, name, industry, address, email, website, description)
        VALUES (p_user_id, p_name, p_industry, p_address, p_email, p_website, p_description);
        SELECT 'Company added successfully.' AS Message;
    ELSE
        -- Return a message if the company already exists
        SELECT 'Company already exists.' AS Message;
    END IF;
END;
""")


create_get_company_procedure = text("""
CREATE PROCEDURE GetCompany(
    IN p_email VARCHAR(255)
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE company_count INT;
    
    -- Retrieve the user_id associated with the given email
    SELECT user_id INTO p_user_id 
    FROM users 
    WHERE email = p_email;
    
    -- Check if there are any companies associated with the user_id
    SELECT COUNT(*) INTO company_count 
    FROM companies 
    WHERE user_id = p_user_id;

    IF company_count = 0 THEN
        -- Return a message if no companies exist for the user
        SELECT 'No company data exists for this user.' AS Message;
    ELSE
        -- Return all company details associated with the user_id if companies exist
        SELECT * FROM companies WHERE user_id = p_user_id;
    END IF;
END;""")



create_modify_company_procedure = text("""
    CREATE PROCEDURE UpdateCompany(
    IN p_email VARCHAR(255),
    IN p_name VARCHAR(255),
    IN p_industry VARCHAR(255),
    IN p_address TEXT,
    IN p_website VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE company_count INT;
    

    -- Retrieve the user_id associated with the given email
    SELECT user_id INTO p_user_id 
    FROM users 
    WHERE email = p_email;
    
    -- Check if there are any companies associated with the user_id
    SELECT COUNT(*) INTO company_count 
    FROM companies 
    WHERE user_id = p_user_id;
    
    IF company_count = 0 THEN
        -- Return a message if no companies exist for the user
        SELECT 'No company data exists for this user.' AS Message;
    ELSE 
        -- Update company details only if a new value has been provided
        UPDATE companies
        SET name = IF(p_name IS NOT NULL, p_name, name),
            industry = IF(p_industry IS NOT NULL, p_industry, industry),
            address = IF(p_address IS NOT NULL, p_address, address),
            website = IF(p_website IS NOT NULL, p_website, website),
            description = IF(p_description IS NOT NULL, p_description, description)
        WHERE user_id = p_user_id;
        SELECT 'Company updated successfully.' AS Message;
    END IF;
END;""")


################### -----------------------COMPANY PROCEDURE------------------------------ #####################################################

create_add_creator_procedure = text("""CREATE PROCEDURE AddCreator(
    IN p_email VARCHAR(255),
    IN p_name VARCHAR(255),
    IN p_bio TEXT,
    IN p_social_media_links TEXT,
    IN p_specialties TEXT,
    IN p_audience_size INTEGER,
    IN p_website VARCHAR(255)
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE creator_exists INT DEFAULT 0;

    -- Retrieve the user_id associated with the given email
    SELECT user_id INTO p_user_id 
    FROM users 
    WHERE email = p_email;

    -- Check if a creator already exists for this user_id
    SELECT COUNT(*) INTO creator_exists 
    FROM creators 
    WHERE user_id = p_user_id;

    IF creator_exists > 0 THEN 
        -- If the creator exists, return a message indicating so
        SELECT 'A creator already exists for this user. Consider updating the existing profile.' AS Message;
    ELSE
        -- Insert new creator
        INSERT INTO creators (user_id, name, bio, social_media_links, specialties, audience_size, email, website)
        VALUES (p_user_id, 
                p_name,  
                p_bio, 
                p_social_media_links, 
                p_specialties, 
                p_audience_size, 
                p_email, 
                p_website);

        -- Confirm successful addition
        SELECT 'Creator added successfully. You may now proceed to add more detailed information.' AS Message;
    END IF;
END;""")


create_get_creator_procedure = text("""
CREATE PROCEDURE GetCreator(
    IN p_email VARCHAR(255)
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE creator_count INT;
    
    -- Retrieve the user_id associated with the given email
    SELECT user_id INTO p_user_id 
    FROM users 
    WHERE email = p_email;
    
    -- Check if the user_id was actually set (found)
    IF p_user_id IS NULL THEN
        SELECT 'No user found with the provided email.' AS Message;
    ELSE
        -- Count how many creator are associated with this user
        SELECT COUNT(*) INTO creator_count 
        FROM creators 
        WHERE user_id = p_user_id;
        
        -- Check if any creator exist for the user
        IF creator_count = 0 THEN
            SELECT 'No creator data exists for this user.' AS Message;
        ELSE
            -- Return all creator details associated with the user_id if creator exist
            SELECT * FROM creators WHERE user_id = p_user_id;
        END IF;
    END IF;
END;
""")







create_modify_creator_procedure = text("""
CREATE PROCEDURE UpdateCreator(
    IN p_email VARCHAR(255),
    IN p_name VARCHAR(255) ,
    IN p_bio TEXT,
    IN p_social_media_links TEXT,
    IN p_specialties TEXT,
    IN p_audience_size INTEGER,
    IN p_website VARCHAR(255)
)
BEGIN
    DECLARE p_user_id INT;
    DECLARE creator_count INT;
    
    -- Retrieve the user_id associated with the given email
    SELECT user_id INTO p_user_id 
    FROM users 
    WHERE email = p_email;
    
    -- Check if there are any companies associated with the user_id
    SELECT COUNT(*) INTO creator_count 
    FROM creators
    WHERE user_id = p_user_id;
    
    IF creator_count = 0 THEN
        -- Return a message if no companies exist for the user
        SELECT 'No creator data exists for this user.' AS Message;
    ELSE 
        -- Update creator details only if a new value has been provided
        UPDATE creators
         SET name = IF(p_name IS NOT NULL, p_name, name),
             bio = IF(p_bio IS NOT NULL, p_bio, bio),
             social_media_links = IF(p_social_media_links IS NOT NULL, p_social_media_links, social_media_links),
             specialties = IF(p_specialties IS NOT NULL, p_specialties, specialties),
             audience_size = IF(p_audience_size IS NOT NULL, p_audience_size, audience_size),
             website = IF(p_website IS NOT NULL, p_website, website)
        WHERE user_id = p_user_id;
        
        SELECT 'Creator updated successfully.' AS Message;
    END IF;
END;""")





################### -----------------------Followers------------------------------ #####################################################


create_add_follower_procedure = text("""
CREATE PROCEDURE AddFollower(
    IN p_participation_id INTEGER,
    IN p_cookies TEXT
)
BEGIN
    INSERT INTO followers (participation_id, cookies)
    VALUES (p_participation_id, p_cookies);
    SELECT 'Follower added successfully.' AS Message;
END;
""")



create_get_follower_procedure = text("""
CREATE PROCEDURE GetFollower(
    IN p_follower_id INTEGER
)
BEGIN
    SELECT * FROM followers WHERE follower_id = p_follower_id;
END;
""")



create_modify_follower_procedure = text("""
CREATE PROCEDURE UpdateFollower(
    IN p_follower_id INTEGER,
    IN p_participation_id INTEGER,
    IN p_cookies TEXT
)
BEGIN
    UPDATE followers
    SET participation_id = p_participation_id,
        cookies = p_cookies
    WHERE follower_id = p_follower_id;
    SELECT 'Follower updated successfully.' AS Message;
END;
""")

