import json
from customer import Customer

# from cs_database_utils import CS_Database_Utils
# from demand_customer import Customer

def cs_register(self, dictionary, db_utils):
    # Pull all the keys from the dictionary
    username = dictionary["username"]
    password = dictionary["password"]
    
    if ("first_name" in dictionary):
        first_name = dictionary["first_name"]
    else:
        first_name = ""
        
    if ("last_name" in dictionary):
        last_name = dictionary["last_name"]
    else:
        last_name = ""
        
    email = dictionary["email"]
    
    if ("phone_number" in dictionary):
        phone_number = dictionary["phone_number"]
    else:
        phone_number = ""
    
    # Create customer object
    new_customer = Customer(username, password, first_name, last_name, email, phone_number)

    # insert dictionary into db
    result = db_utils.register_user(new_customer)

    # if the insertion was successful return 200
    if result != None:
        return True
    # if user already exists return 403
    else:
        return False
