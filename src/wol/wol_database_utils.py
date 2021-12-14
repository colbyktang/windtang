import pymongo
import datetime
import time
import os
import uuid
import hashlib
from pymongo import MongoClient
from bson.objectid import ObjectId

class WOL_Database_Utils:
    def __init__(self, uri="mongodb://localhost:27017/admin"): 
        # Making a connection to a database with MongoClient from pymongo
        self.uri = uri
        self.client = MongoClient(uri)   
        self.time_format = "%Y-%m-%d %H:%M:%S"
        self.db = self.client.logs
        self.set_collection_wol()

    # Retrieving a collection called wol in the database
    def get_collection_wol(self):
        return self.db.wol

    # Use a collection called wol in the database
    def set_collection_wol(self):
        self.collection = self.db.wol
    
    # retrieve the current time in YYYY-MM-DD HH:MM:SS
    def get_timestamp(self):
        return datetime.datetime.now().strftime(self.time_format)
    
    # retrieve the current time in milliseconds for determining the newest/oldest
    def get_milliseconds(self):
        return int(round(time.time() * 1000))
    
    # called when object is deleted
    def __delete__(self):
        self.client.close()
    
#########
# LOGS #
#########
    
    # Upload log dictionary to mongodb
    def create_log(self, log_type, status):
        dictionary = {"type": log_type, "status": status, "timestamp": self.get_timestamp()}
        retValue = self.collection.insert_one(dictionary)          
        return retValue
    
    def create_wol_log (self, status):
        return self.create_log ("Wake-on-LAN signal", status)