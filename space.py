import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint

APP_ROOT = os.path.join(os.path.dirname(__file__), '')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['villagecontent']

spacecollection = db['space']

def basic_space():
    space = spacecollection.find_one({"title": "Basic Membership"})
    return space