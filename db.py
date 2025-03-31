from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_database():
    client = MongoClient(config["ATLAS_URI"])
    db = client[config["DB_NAME"]]
    try:
        yield db  # Dependency injection for cleaner DB access
    finally:
        client.close()