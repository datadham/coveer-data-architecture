from sqlalchemy import create_engine, text

######## -------------- COMPANY PROCEDURE------------------------------------------------------------------------------------#################

create_add_company_procedure = text("""
CREATE PROCEDURE AddCompany(
    IN p_user_id INTEGER,
    IN p_name VARCHAR(255),
    IN p_industry VARCHAR(255),
    IN p_address TEXT,
    IN p_contact_email VARCHAR(255),
    IN p_website VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    INSERT INTO companies (user_id, name, industry, address, contact_email, website, description)
    VALUES (p_user_id, p_name, p_industry, p_address, p_contact_email, p_website, p_description);
    SELECT 'Company added successfully.' AS Message;
END;
""")

create_get_company_procedure = text("""
CREATE PROCEDURE GetCompany(
    IN p_company_id INTEGER
)
BEGIN
    SELECT * FROM companies WHERE company_id = p_company_id;
END;
""")

create_modify_company_procedure = text("""
    CREATE PROCEDURE UpdateCompany(
        IN p_company_id INTEGER,
        IN p_name VARCHAR(255),
        IN p_industry VARCHAR(255),
        IN p_address TEXT,
        IN p_contact_email VARCHAR(255),
        IN p_website VARCHAR(255),
        IN p_description TEXT
    )
    BEGIN
        UPDATE companies
        SET name = p_name,
            industry = p_industry,
            address = p_address,
            contact_email = p_contact_email,
            website = p_website,
            description = p_description
        WHERE company_id = p_company_id;
        SELECT 'Company updated successfully.' AS Message;
    END;
    """)

create_delete_company_procedure = text("""
CREATE PROCEDURE DeleteCompany(
    IN p_company_id INTEGER
)
BEGIN
    DELETE FROM companies WHERE company_id = p_company_id;
    SELECT 'Company deleted successfully.' AS Message;
END;
""")

################### -----------------------COMPANY PROCEDURE------------------------------ #####################################################

create_add_creator_procedure = text("""
CREATE PROCEDURE AddCreator(
    IN p_user_id INTEGER,
    IN p_name VARCHAR(255),
    IN p_bio TEXT,
    IN p_social_media_links TEXT,
    IN p_specialties TEXT,
    IN p_audience_size INTEGER,
    IN p_contact_email VARCHAR(255),
    IN p_website VARCHAR(255)
)
BEGIN
    INSERT INTO creators (user_id, name, bio, social_media_links, specialties, audience_size, contact_email, website)
    VALUES (p_user_id, p_name, p_bio, p_social_media_links, p_specialties, p_audience_size, p_contact_email, p_website);
    SELECT 'Creator added successfully.' AS Message;
END;
""")


create_get_creator_procedure = text("""
CREATE PROCEDURE GetCreator(
    IN p_creator_id INTEGER
)
BEGIN
    SELECT * FROM creators WHERE creator_id = p_creator_id;
END;
""")


create_modify_creator_procedure = text("""
CREATE PROCEDURE UpdateCreator(
    IN p_creator_id INTEGER,
    IN p_name VARCHAR(255),
    IN p_bio TEXT,
    IN p_social_media_links TEXT,
    IN p_specialties TEXT,
    IN p_audience_size INTEGER,
    IN p_contact_email VARCHAR(255),
    IN p_website VARCHAR(255)
)
BEGIN
    UPDATE creators
    SET name = p_name,
        bio = p_bio,
        social_media_links = p_social_media_links,
        specialties = p_specialties,
        audience_size = p_audience_size,
        contact_email = p_contact_email,
        website = p_website
    WHERE creator_id = p_creator_id;
    SELECT 'Creator updated successfully.' AS Message;
END;
""")


create_delete_creator_procedure = text("""
CREATE PROCEDURE DeleteCreator(
    IN p_creator_id INTEGER
)
BEGIN
    DELETE FROM creators WHERE creator_id = p_creator_id;
    SELECT 'Creator deleted successfully.' AS Message;
END;
""")


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



create_delete_follower_procedure = text("""
CREATE PROCEDURE DeleteFollower(
    IN p_follower_id INTEGER
)
BEGIN
    DELETE FROM followers WHERE follower_id = p_follower_id;
    SELECT 'Follower deleted successfully.' AS Message;
END;
""")

