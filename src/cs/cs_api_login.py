import json
import hashlib
import os
import wt_jwt

from cs_database_utils import CS_Database_Utils

def cs_login(self, dictionary, db_utils):
    print("cs_login")
    # Grab the username and password from the dictionary and check them
    username = dictionary["username"]
    password = dictionary["password"]

    # Creating database utils object to interact with the database
    doCredentialsMatch = db_utils.does_credentials_exist(username, password)
    print("doCredentialsMatch: ", doCredentialsMatch)

    #if username and password pair is found:
    if doCredentialsMatch:
        names_dictionary = db_utils.get_names_from_username(username)
        names_dictionary["username"] = username
        
        # Create token
        token = wt_jwt.create_token (names_dictionary)
        print ("Created token: ", token)
        names_dictionary["token"] = token
        
        return names_dictionary

    #if an error occurs
    else:
        return None