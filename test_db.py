import pymongo
import datetime
import time
import os
import uuid
import hashlib
from pymongo import MongoClient
from bson.objectid import ObjectId

from cs_database_utils import CS_Database_Utils
from cs_user import User

def main():
    user = User("ctang2", "pass", "Colby", "Tang", "ctang@stedwards.edu", "5129704905")
    db = CS_Database_Utils()
    db.register_user(user)
    
if __name__ == "__main__":
    main()