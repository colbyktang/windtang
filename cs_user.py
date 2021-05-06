# re module provides support 
# for regular expressions 
import re
import os
import hashlib

class User:
    def __init__ (self, username, password, first_name, last_name, email, phone_number):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number


    # getter method for username
    @property
    def username(self):
        return self._username
    
    # setter method for username
    @username.setter
    def username(self, username):
        if (len(username) < 5):
            raise ValueError("Username has less than 5 characters!")
        if (len(username) > 30):
            raise ValueError("Username has more than 30 characters!")
        self._username = username

    # getter method for passord
    @property
    def password(self):
        return self._password
    
    # setter method for password
    @password.setter
    def password(self, password):
        special_character_password = '[@_!#$%^&*()<>?/\|}{~:]'
        
        if (len(password) < 6):
            raise ValueError("Password has less than 6 characters!") 
        else:
            self._password = password
   
    # getter method for first name
    @property
    def first_name(self):
        return self._first_name
    
    # setter method for first name
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    # getter method for last name
    @property
    def last_name(self):
        return self._last_name
    
    # setter method for last name
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    # getter method for email
    @property
    def email(self):
        return self._email
    
    # setter method for email
    @email.setter
    def email(self, email):
        email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(email_regex, email)):
            self._email = email
        else:
            raise ValueError("Email is invalid")

    # getter method for phone number
    @property
    def phone_number(self):
        return self._phone_number
    
    # setter method for phone number
    @phone_number.setter
    def phone_number(self, phone_number):
        if (len(phone_number) < 10):
            raise ValueError("Phone number must have 10 digits!")
        else:
            self._phone_number = phone_number
        
    # getter method for all values of user
    @property
    def dictionary(self):
        user_dictionary = {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number
        }
        return user_dictionary    



# Handmade/crafted variables!
#user1 = User("jquade", "admin", "Jeff", "Quade", "jquade@stedwards.edu", "USA", "5127364724")
#user1.last_name = "jeff!"

#mark = User("jquade", "admin", "Jeff", "Quade", "jquade@stedwards.edu", "USA", "5127364724")
#mark.phone_number = "1a"
    