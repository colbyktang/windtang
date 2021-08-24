import pymongo
import datetime
import time
import os
import uuid
import hashlib
import requests
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

from cs_database_utils import CS_Database_Utils
from cs_user import User

def main():
    
    #user = User("ctang", "poop", "Colby", "Tang", "ctang@stedwards.edu", "5129704905")
    #db = CS_Database_Utils()
    #db.register_user(user)
    
    data = {
        'username': 'ctang',
        'password': 'poop',
        'first_name': 'Colby',
        'last_name': 'Tang',
        'email': 'ctang@stedwards.edu',
        'phone_number': '5129704905'
    }
    
    url = 'http://localhost:4112/api/cs/login'
    
    r = requests.post(url, json=data)
    status_code = r.status_code
    print (status_code)
    print (r.content)
    
    print ("START WAITING")
    for i in range(5):
        time.sleep(1)
        print ("WAITING ", i)
    
    print ("NEW API REQUEST")
    response = json.loads(r.content)
    token = response["token"]
    
    data = {
        'token': token
    }
    url = 'http://localhost:4112/api/cs/token'
    
    r = requests.post(url, json=data)
    status_code = r.status_code
    print (status_code)
    print (r.content)
    
if __name__ == "__main__":
    main()