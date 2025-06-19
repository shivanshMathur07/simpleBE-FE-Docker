from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

def get_mongo_client():
    """
    Connects to MongoDB and returns the database object.

    :param uri: MongoDB connection URI
    :param db_name: Name of the database to connect to
    :return: Database object
    """
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME")
    if not uri or not db_name:
        raise ValueError("MONGO_URI and MONGO_DB_NAME must be set in the environment variables.")
    client = MongoClient(uri)
    db = client[db_name]
    return db