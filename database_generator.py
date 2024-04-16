from faker import Faker
import pandas as pd 
import sqlalchemy
import random
from datetime import datetime
import json 
import os 
import uuid



fake = Faker()


def get_company():
    return {
        "id": str(uuid.uuid4()),
        "name": fake.company(),
        "industry": fake.bs(),
        "description": fake.catch_phrase(),
        "address": fake.address(),
        "number_of_employees": random.randint(1, 10000),
        "founded_date": fake.date_between(start_date="-30y", end_date="today"),
    }


def get_creator():
    return {
        "id": str(uuid.uuid4()),
        "name": fake.name(),
        "username": fake.user_name(),
        "platform": random.choice(['Instagram', 'YouTube', 'TikTok', 'Twitter']),
        "bio": fake.sentence(nb_words=10),
        "number_of_followers": random.randint(1000, 1000000),
        "number_of_posts": random.randint(10, 1000),
        "engagement_rate": round(random.uniform(0.5, 5.0), 2),
        "topics": fake.words(nb=3, unique=True)
    }


def get_campaign(creators,companies):
    # Randomly select a subset of creators for each campaign
    selected_creators = random.sample(creators, k=random.randint(5, 10))
    selected_company = random.sample(companies,k=1)
    return {
        "id": str(uuid.uuid4()),
        "company":selected_company,
        "title": fake.catch_phrase(),
        "description": fake.text(max_nb_chars=200),
        "budget": round(random.uniform(1000, 10000), 2),
        "start_date": str(fake.past_date()),
        "end_date": str(fake.future_date()),
        "creators": selected_creators   
    }

  
# Generate all data
#all_creators = [get_creator() for _ in range(200)]
#all_companies = [get_company() for _ in range(5)]
#all_campaigns = [get_campaign(all_creators,all_companies) for _ in range(78)]

#print(all_campaigns[0].keys())

def generateData(nb_campaign=0,nb_company=0,nb_creator=0):
    companys = [get_company() for _ in range(nb_company)]
    creators = [get_creator() for _ in range(nb_creator)]
    campaigns = [get_campaign(creators,companys) for _ in range(nb_campaign)]

    return {'creators':creators,'companys':companys,'campaigns':campaigns}

nb_company=5
nb_creator=50
nb_campaign=100

data = generateData(nb_campaign,nb_company,nb_creator)


# Create a directory 'data' if it does not exist
os.makedirs('data', exist_ok=True)

for col in data.keys():
    # Store the JSON data in a file named after the key inside the 'data' directory
    with open(f'data/{col}.json', 'w') as f:
        # Correct placement of default=str inside json.dumps()
        f.write(json.dumps(data[col], default=str))