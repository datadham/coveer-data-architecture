from sqlalchemy import create_engine, text

# SQL Definitions for Table Creation
create_campaigns_table = text('''
CREATE TABLE IF NOT EXISTS campaigns (
    campaign_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    company_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    campaign_status VARCHAR(100),
    campaign_code VARCHAR(100),
    target_audience VARCHAR(255),
    budget DECIMAL(10, 2),
    actual_spending DECIMAL(10, 2),
    campaign_result TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);''')

create_event_campaigns_table = text('''
CREATE TABLE IF NOT EXISTS event_campaigns (
    event_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    campaign_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    title VARCHAR(255),
    description TEXT,
    start_date DATE,
    end_date DATE,
    campaign_status VARCHAR(100),
    campaign_code VARCHAR(100),
    target_audience VARCHAR(255),
    budget DECIMAL(10, 2),
    actual_spending DECIMAL(10, 2),
    campaign_result TEXT,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE
);''')

create_table_participation = text('''
CREATE TABLE IF NOT EXISTS campaign_participation (
    participation_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    participation_link TEXT,
    participation_code TEXT,
    campaign_id INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    status VARCHAR(100),
    role VARCHAR(100),
    join_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    FOREIGN KEY (creator_id) REFERENCES creators(creator_id) ON DELETE CASCADE,
    UNIQUE (campaign_id, creator_id)  -- ensures each pair is unique
);''')




