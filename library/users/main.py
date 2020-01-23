from pymongo import MongoClient
from dotenv import load_dotenv
import os
import hashlib, binascii

APP_ROOT = os.path.join(os.path.dirname(__file__), '')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

mongo_url = os.getenv('MONGODB_URI')
client = MongoClient(mongo_url)
db = client['villagecontent']

def regusers(username, password, role = None):
    password = str.encode(password)
    dk = hashlib.pbkdf2_hmac('sha512', password, b'salt', 10000)
    hash_password = binascii.hexlify(dk)
    hash_password = hash_password.decode()
    if not role:
        userdata= {
            "username" : username,
            "password" : hash_password,
            "role" : "general"
        }
        userscollection = db['users']
        chk = userscollection.find_one({"username": username})

        if not chk:

            userscollection.insert_one(userdata)
            print('Username : %s \nHashed Password : %s' % (username, hash_password))
            return True
        else: 
            print('Username Exists')
            return False
    else:
        userdata= {
            "username" : username,
            "password" : hash_password,
            "role" : role
        }

        userscollection = db['users']
        chk = userscollection.find_one({"username": username})

        if not chk:

            userscollection.insert_one(userdata)
            print('Username : %s \nHashed Password : %s' % (username, hash_password))
            return True
        else: 
            print('Username Exists')
            return False

def login(username, password):

    password = str.encode(password)
    dk = hashlib.pbkdf2_hmac('sha512', password, b'salt', 10000)
    hash_password = binascii.hexlify(dk)
    hash_password = hash_password.decode()
    userdata= {
        "username" : username,
        "Password" : hash_password
    }

    userscollection = db['users']
    chk = userscollection.find_one({"username": username})

    if not chk: 
        print('username : %s does not exist' % username)
        return False
    else:
        getpassword = chk['password']
        if (getpassword == hash_password):
            print('User log in successful')
            return True
        else:
            print ('User Failed to login')
            return False
    userscollection.insert_one(userdata)
    print('Username : %s \nHashed Password : %s' % (username, hash_password))