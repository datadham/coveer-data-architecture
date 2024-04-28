from sqlalchemy import create_engine, text


####  CAMPAIGN PROCEDURE ####
create_add_campaign_procedure = text("""
CREATE PROCEDURE AddCampaign(
    IN p_company_id INTEGER,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_start_date DATE,
    IN p_end_date DATE,
    IN p_campaign_status VARCHAR(100),
    IN p_campaign_code VARCHAR(100),
    IN p_target_audience VARCHAR(255),
    IN p_budget DECIMAL(10, 2),
    IN p_actual_spending DECIMAL(10, 2),
    IN p_campaign_result TEXT
)
BEGIN
    INSERT INTO campaigns (company_id, title, description, start_date, end_date, 
        campaign_status, campaign_code, target_audience, budget, actual_spending, campaign_result)
    VALUES (p_company_id, p_title, p_description, p_start_date, p_end_date, 
        p_campaign_status, p_campaign_code, p_target_audience, p_budget, p_actual_spending, p_campaign_result);
END;
""")

create_get_campaign_procedure = text("""
CREATE PROCEDURE GetCampaign(
    IN p_campaign_id INTEGER
)
BEGIN
    SELECT * FROM campaigns
    WHERE campaign_id = p_campaign_id;
END;
""")

create_modify_campaign_procedure = text("""
CREATE PROCEDURE UpdateCampaign(
    IN p_campaign_id INTEGER,
    IN p_company_id INTEGER,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_start_date DATE,
    IN p_end_date DATE,
    IN p_campaign_status VARCHAR(100),
    IN p_campaign_code VARCHAR(100),
    IN p_target_audience VARCHAR(255),
    IN p_budget DECIMAL(10, 2),
    IN p_actual_spending DECIMAL(10, 2),
    IN p_campaign_result TEXT
)
BEGIN
    UPDATE campaigns SET
        company_id = p_company_id,
        title = p_title,
        description = p_description,
        start_date = p_start_date,
        end_date = p_end_date,
        campaign_status = p_campaign_status,
        campaign_code = p_campaign_code,
        target_audience = p_target_audience,
        budget = p_budget,
        actual_spending = p_actual_spending,
        campaign_result = p_campaign_result
    WHERE campaign_id = p_campaign_id;
END;
""")

create_delete_campaign_procedure = text("""
CREATE PROCEDURE DeleteCampaign(
    IN p_campaign_id INTEGER
)
BEGIN
    DELETE FROM campaigns
    WHERE campaign_id = p_campaign_id;
END;
""")


####  EVENT CAMPAIGN PROCEDURE ####

create_add_event_campaign_procedure = text("""
CREATE PROCEDURE AddEventCampaign(
    IN p_campaign_id INTEGER,
    IN p_company_id INTEGER,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_start_date DATE,
    IN p_end_date DATE,
    IN p_campaign_status VARCHAR(100),
    IN p_campaign_code VARCHAR(100),
    IN p_target_audience VARCHAR(255),
    IN p_budget DECIMAL(10, 2),
    IN p_actual_spending DECIMAL(10, 2),
    IN p_campaign_result TEXT
)
BEGIN
    INSERT INTO event_campaigns (campaign_id, company_id, title, description, start_date, end_date, 
        campaign_status, campaign_code, target_audience, budget, actual_spending, campaign_result)
    VALUES (p_campaign_id, p_company_id, p_title, p_description, p_start_date, p_end_date, 
        p_campaign_status, p_campaign_code, p_target_audience, p_budget, p_actual_spending, p_campaign_result);
END;
""")

create_get_event_campaign_procedure = text("""
CREATE PROCEDURE GetEventCampaign(
    IN p_event_id INTEGER
)
BEGIN
    SELECT * FROM event_campaigns
    WHERE event_id = p_event_id;
END;
""")

create_modify_event_campaign_procedure = text("""
CREATE PROCEDURE UpdateEventCampaign(
    IN p_event_id INTEGER,
    IN p_campaign_id INTEGER,
    IN p_company_id INTEGER,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_start_date DATE,
    IN p_end_date DATE,
    IN p_campaign_status VARCHAR(100),
    IN p_campaign_code VARCHAR(100),
    IN p_target_audience VARCHAR(255),
    IN p_budget DECIMAL(10, 2),
    IN p_actual_spending DECIMAL(10, 2),
    IN p_campaign_result TEXT
)
BEGIN
    UPDATE event_campaigns SET
        campaign_id = p_campaign_id,
        company_id = p_company_id,
        title = p_title,
        description = p_description,
        start_date = p_start_date,
        end_date = p_end_date,
        campaign_status = p_campaign_status,
        campaign_code = p_campaign_code,
        target_audience = p_target_audience,
        budget = p_budget,
        actual_spending = p_actual_spending,
        campaign_result = p_campaign_result
    WHERE event_id = p_event_id;
END;
""")

create_delete_event_campaign_procedure = text("""
CREATE PROCEDURE DeleteEventCampaign(
    IN p_event_id INTEGER
)
BEGIN
    DELETE FROM event_campaigns
    WHERE event_id = p_event_id;
END;
""")

### PARTICIPATION PROCEDURE ### 

create_add_participation_procedure = text("""
CREATE PROCEDURE AddParticipation(
    IN p_campaign_id INTEGER,
    IN p_creator_id INTEGER,
    IN p_participation_link TEXT,
    IN p_participation_code TEXT,
    IN p_status VARCHAR(100),
    IN p_role VARCHAR(100),
    IN p_join_date DATETIME
)
BEGIN
    INSERT INTO campaign_participation (
        campaign_id, creator_id, participation_link, participation_code,
        status, role, join_date
    )
    VALUES (
        p_campaign_id, p_creator_id, p_participation_link, p_participation_code,
        p_status, p_role, p_join_date
    );
END;
""")

create_get_participation_procedure = text("""
CREATE PROCEDURE GetParticipation(
    IN p_participation_id INTEGER
)
BEGIN
    SELECT * FROM campaign_participation
    WHERE participation_id = p_participation_id;
END;
""")

create_modify_participation_procedure = text("""
CREATE PROCEDURE UpdateParticipation(
    IN p_participation_id INTEGER,
    IN p_campaign_id INTEGER,
    IN p_creator_id INTEGER,
    IN p_participation_link TEXT,
    IN p_participation_code TEXT,
    IN p_status VARCHAR(100),
    IN p_role VARCHAR(100),
    IN p_join_date DATETIME
)
BEGIN
    UPDATE campaign_participation SET
        campaign_id = p_campaign_id,
        creator_id = p_creator_id,
        participation_link = p_participation_link,
        participation_code = p_participation_code,
        status = p_status,
        role = p_role,
        join_date = p_join_date
    WHERE participation_id = p_participation_id;
END;
""")

create_delete_participation_procedure = text("""
CREATE PROCEDURE DeleteParticipation(
    IN p_participation_id INTEGER
)
BEGIN
    DELETE FROM campaign_participation
    WHERE participation_id = p_participation_id;
END;
""")