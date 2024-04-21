from sqlalchemy import create_engine, text

# Revised SQL to create the 'users' table
create_users_table = text("""
CREATE TABLE IF NOT EXISTS coveer_db.users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile_type VARCHAR(255) DEFAULT 'creator',
    email_verified BOOLEAN NOT NULL DEFAULT 0,
    email_verification_token VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
""")

# Revised SQL to create the 'social_logins' table
create_social_logins_table = text("""
CREATE TABLE IF NOT EXISTS coveer_db.social_logins (
    social_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    provider VARCHAR(50) NOT NULL,
    social_user_id VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES coveer_db.users(user_id)  -- Corrected FK reference
);
""")

# Revised SQL to create the 'password_resets' table
create_password_resets_table = text("""
CREATE TABLE IF NOT EXISTS coveer_db.password_resets (
    reset_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    reset_token VARCHAR(255) NOT NULL,
    expiration_date DATETIME NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    used BOOLEAN NOT NULL DEFAULT 0
);
""")