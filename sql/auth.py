from sqlalchemy import create_engine, text

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
    VALUES (p_email, SHA2(p_password, 256), p_profile_type, v_token);
    SELECT 'User registered successfully.' AS Message;
END;
""")
