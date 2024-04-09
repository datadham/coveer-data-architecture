from faker import Faker
import pandas as pd 
import sqlalchemy
import random
from datetime import datetime
import json 
import os 

fake = Faker()

def getcompany():
    company = {
            "name": fake.company(),
            "industry": fake.bs(),  # Génère un domaine d'activité aléatoire
            "description": fake.catch_phrase(),
            "address": fake.address(),
            "number_of_employees": random.randint(1, 10000),  # Génère un nombre aléatoire d'employés
            "founded_date": fake.date_between(start_date="-30y", end_date="today")
        }
    return company


def getcreator():
    creator = {
            "name": fake.name(),
            "username": fake.user_name(),
            "platform": random.choice(['Instagram', 'YouTube', 'TikTok', 'Twitter']),
            "bio": fake.sentence(nb_words=10),
            "number_of_followers": random.randint(1000, 1000000),
            "number_of_posts": random.randint(10, 1000),
            "engagement_rate": round(random.uniform(0.5, 5.0), 2),  # Pourcentage d'engagement
            "topics": fake.words(nb=3, unique=True)  # Sujets de contenu
        }
    return creator


def getcampaign():
    campaign = {
        "title": fake.catch_phrase(),
        "description": fake.text(max_nb_chars=200),
        "budget": round(random.uniform(1000, 10000), 2),
        "start_date": str(fake.past_date()),
        "end_date": str(fake.future_date()),
        "company":getcompany(),
        "creators":[getcreator() for _ in range(random.randint(1,10))]
    }
    return campaign

def generateData(nb_campaign=0,nb_company=0,nb_creator=0):
    campaigns = [getcampaign() for _ in range(nb_campaign)]
    companys = [getcompany() for _ in range(nb_company)]
    creators = [getcreator() for _ in range(nb_creator)]

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