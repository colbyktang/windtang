# Class: Customer
# Concern: Demand
# Required parameters:
    # username - String
    # password - String
    # first_name - String
    # last_name - String
    # email - String
    # phone_number - String
    
####################### testing methods ####################################
#new_customer = Customer("jquade", "admin", "Jeff", "Quade", "jquade@stedwards.edu", "5127364724")

#print(new_customer.get_username(), new_customer.get_password(), new_customer.get_first_name(), new_customer.get_last_name(), new_customer.get_email(), new_customer.get_country(), new_customer.get_phone_number())
#############################################################################
from cs_user import User

class Customer (User):

    # getter method for all values of customer
    @property
    def dictionary(self):
        customer_dictionary = {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number
        }
        return customer_dictionary
