from sqlalchemy import create_engine, text

create_company_table = text('''
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    address TEXT,
    email VARCHAR(255),
    website VARCHAR(255),
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);''')


create_creators_table = text('''
CREATE TABLE IF NOT EXISTS creators (
    creator_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    bio TEXT,
    social_media_links TEXT,  -- JSON or serialized text format to store multiple links
    specialties TEXT,  -- Could be a list of specialties or focus areas
    audience_size INTEGER,
    email VARCHAR(255),
    website VARCHAR(255),  -- Changed from URL to VARCHAR
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);''')


create_table_follower = text('''
CREATE TABLE IF NOT EXISTS followers (
    follower_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
    participation_id INTEGER,
    cookies TEXT,
    join_date DATETIME DEFAULT CURRENT_TIMESTAMP
    -- FOREIGN KEY (participation_id) REFERENCES participation(participation_id) ON DELETE CASCADE
);''')

