import jwt
import datetime


from jwt.exceptions import ExpiredSignatureError
from cryptography.hazmat.primitives import serialization

def test():
    private_key = open("wt-jwt", 'r').read()
    public_key = open("wt-jwt.pub", 'r').read()

    key = serialization.load_ssh_private_key(private_key.encode(), password=b'***REMOVED***')
    pub_key = serialization.load_ssh_public_key(public_key.encode())

    payload_data = {
        "sub": "4242",
        "name": "Temp name",
        "nickname": "TempNickname"
    }

    token = jwt.encode (
        payload = payload_data,
        key = key,
        algorithm='RS256'
    )

    try:
        payload = jwt.decode(
            token, 
            key=pub_key, 
            algorithms=['RS256', ]
        )
        print (payload)

    except ExpiredSignatureError as error:
        print ("Unable to decode the token, error: ", error)

def get_private_key ():
    private_key = open("src/cs/.ssh/wt-jwt", 'r').read()
    passphrase = open("src/cs/.ssh/wt-pwd", 'r').read()
    return serialization.load_ssh_private_key(private_key.encode(), password=str.encode(passphrase))

def get_public_key ():
    public_key = open("src/cs/.ssh/wt-jwt.pub", 'r').read()
    pub_key = serialization.load_ssh_public_key(public_key.encode())

def create_token(names_dictionary):
    # Read in private key
    key = get_private_key()
    
    try:
        payload_data = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=15),
            'iat': datetime.datetime.utcnow(),
            'sub': names_dictionary["_id"],
            'username': names_dictionary["username"],
            'first_name': names_dictionary["first_name"],
            'last_name': names_dictionary["last_name"]
        }
        
        # Create RSA encoded token
        return jwt.encode (
            payload_data,
            key,
            algorithm='RS256'
        )
    
    except Exception as e:
        return e
    
def token_required (headers):
    pub_key = get_public_key()
    
    token_passed = headers['token']
    try:
        if headers['token'] != '' and headers['token'] != None:
            try:
                return_data = jwt.decode (
                    token_passed, 
                    pub_key, 
                    algorithms=['RS256']
                )
                print ("token_required: True")
                return return_data
            
            except ExpiredSignatureError:
                return_data = {
                    "error": "1",
                    "message": "Token has expired"
                }
                print ("token_required: ExpiredSignatureError")
                return return_data
            
            except:
                return_data = {
                    "error": "1",
                    "message": "Invalid Token"
                }
                print ("token_required: Invalid Token")
                return return_data
            
        else:
            return_data = {
                "error": "2",
                "message": "Token Required"
            }
            print ("token_required: Token Required")
            return return_data
        
    except Exception as e:
        return_data = {
            "error": "3",
            "message": "An error occured"
        }
        print ("token_required: An error occured")
        return return_data