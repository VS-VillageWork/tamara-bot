import os
from pymongo import MongoClient
from dotenv import load_dotenv


APP_ROOT = os.path.join(os.path.dirname(__file__), '')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


mongo_url = os.getenv('MONGODB_URI')
client = MongoClient(mongo_url)
db = client['villagecontent']

spacecollection = db['space']

def coworking():
    space = spacecollection.find({})
    return space
