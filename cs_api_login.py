import json
import hashlib
import os

from cs_database_utils import CS_Database_Utils

def cs_login(self, dictionary, db_utils):
    # Grab the username and password from the dictionary and check them
    username = dictionary["username"]
    password = dictionary["password"]

    # Creating database utils object to interact with the database
    doCredentialsMatch = db_utils.does_credentials_exist(username, password)
    print("doCredentialsMatch: ", doCredentialsMatch)

    #if username and password pair is found:
    if doCredentialsMatch:
        names_dictionary = db_utils.get_names_from_username(username)
        return names_dictionary

    #if an error occurs
    else:
        return None