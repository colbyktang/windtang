# Team 12
# Written by Will
# Changed by Colby Tang

## __demanddb Collections__

### Customer
#   username - String: Used during login
#   password - String: Used during login
#   first_name - String: Displayed in the dashboard
#   last_name - String: Displayed in the dashboard
#   email - String: To contact the fleet manager
#   country - String: Country of residence
#   phone_number - String: To contact the customer

## __supplydb Collections__

### FM (Fleet Manager)
#   username - String: Used during login
#   password - String: Used during login
#   first_name - String: Displayed in the dashboard
#   last_name - String: Displayed in the dashboard
#   email - String: To contact the fleet manager
#   country - String: Country of residence
#   phone_number - String: To contact the fleet manager

import pymongo
import datetime
import time
import os
import uuid
import hashlib
from pymongo import MongoClient
from bson.objectid import ObjectId

from customer import Customer

class CS_Database_Utils:
    def __init__(self, uri="mongodb://ctang_admin:password@localhost:27017/admin"): 
        # Making a connection to a database with MongoClient from pymongo
        self.uri = uri
        self.client = MongoClient(uri)   
        self.time_format = "%Y-%m-%d %H:%M:%S"
        self.db = self.client.users
        self.set_collection_users()

    # Retrieving a collection called fm in the database
    def get_fm_collection(self):
        return self.db.fm

    # Retrieving a collection called users in the database
    def set_collection_users(self):
        self.collection = self.db.users
    
    # Retrieving a collection called fm in the database
    def set_collection_fm(self):
        self.collection = self.db.fm
    
    # retrieve the current time in YYYY-MM-DD HH:MM:SS
    def get_timestamp(self):
        return datetime.datetime.now().strftime(self.time_format)
    
    # retrieve the current time in milliseconds for determining the newest/oldest
    def get_milliseconds(self):
        return int(round(time.time() * 1000))
    
    # called when object is deleted
    def __delete__(self):
        self.client.close()
        
    # hash a value
    def hash(self, value):
        if "supply" in self.server_type:
            return value
        # Salts make the search space larger in the case of brute forcing and adds difficulty for rainbow tables; 
        # Using a salt only requires you to do a little more work and store an extra random byte sequence.
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        
        # 'sha256' is the hash digest algorithm for HMAC
        # value.encode('utf-8') converts the value into bytes
        # salt provides the salt
        # 100000 is 100,000 iterations of SHA-256
        key = hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
        return key
    
    def check_password(self, hashed_password, user_password):
        if "supply" in self.server_type:
            return True
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    
#########
# USERS #
#########
    
    # Upload user dictionary to mongodb
    def register_user(self, user):
        # Check if username is already in the database, if so return None, otherwise return the insert result
        doesUsernameAlreadyExist = self.is_username_in_db(user.username)
        if doesUsernameAlreadyExist:
            retValue = None
        else:
            # grab the dictionary from the user, does not include a password
            dictionary = user.dictionary
            
            # update the dictionary with a hashed password along with a timestamp
            dictionary.update( {"password": self.hash(user.password)})
            dictionary.update( {"timestamp": self.get_timestamp()})
            
            # insert the user dictionary into the db
            retValue = self.collection.insert_one(dictionary)

        return retValue
    
    # Is username in database? If so return true, else false
    def is_username_in_db(self, username):
        find_one_result = self.collection.find_one({'username': username}, {'username': 1})

        if find_one_result != None:
            return True
        else:
            return False

    # Does the username and password pair match in the database?
    def does_credentials_exist(self, username, password):
        find_one_result = self.collection.find_one({'username': username}, {'password': 1})
        if find_one_result != None:
            return self.check_password (find_one_result["password"], password)
        else:
            return False
    
    # Returns all information of user
    def get_user_from_username(self, username):
        entry = self.collection.find_one({'username': username}, {'password': 0})
        if entry != None:
            entry['_id'] = str(entry['_id'])
        return entry

    # Returns the first and last name of the username
    def get_names_from_username(self, username):
        entry = self.collection.find_one({'username': username}, {'_id': 0, 'first_name': 1, 'last_name':1})
        return entry