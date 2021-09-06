import http.server
from http.server import BaseHTTPRequestHandler
import urllib.parse
import json

from cs_database_utils import CS_Database_Utils
import cs_api_login
import cs_api_register
import wt_jwt

class CommonServicesListener(BaseHTTPRequestHandler):
    
    def do_POST(self):
        print ("\n******** NEW COMMON SERVICES POST REQUEST *********")
        # get the path of the request that was sent in
        path = self.path
        
        # Displaying the headers of the paht being sent in
        print('Headers:"', self.headers, '"')
        
        print ("Domain: ", self.headers['host'])

        # Displaying the type of the content of the request
        print('Content-Type:', self.headers['content-type'])
        
        # Collecting the length of the body read the characters
        # that are contained in the body.
        length = int(self.headers['content-length'])
        body = self.rfile.read(length)
        
        # convert body into a dictionary
        incoming_dictionary = json.loads(body)
        print ("Incoming Dictionary: " + str(incoming_dictionary))
        print ("POST PATH: ", path)
        
        db_utils = self.create_db_object()
        
        # Handling a registration request from POST
        if path == "/api/cs/register":
            response = cs_api_register.cs_register(self, incoming_dictionary, db_utils)
            username = incoming_dictionary["username"]
            if response:
                self.respond_code(200, "User " + username + " entered into database!")
            else:
                self.respond_code(403, "User " + username + " already exists in the database!")

        # Handling a login request from POST
        elif path == "/api/cs/login":
            print ("Login API:")
            if "username" not in incoming_dictionary:
                self.respond_code(403, "Empty username! Code 403")
            if "password" not in incoming_dictionary:
                self.respond_code(403, "Username was not found! Code 403")
            response = cs_api_login.cs_login(self, incoming_dictionary, db_utils)
            if response != None:
                self.respond_convert_json_object (200, response)
            else:
                self.respond_code(403, "Credentials were not found! Code 403")
                
        elif path == "/api/cs/token":
            token = wt_jwt.token_required(incoming_dictionary)
            print ("Return from token required: ", token)
            if "error" not in token:
                self.respond_convert_json_object (200, token)
            else:
                self.respond_convert_json_object (403, token)
                
        #Connection error:
        else:
            # If the path did not match any known request
            # a 404 Not Found error is thrown.
            print ("api/cs failed")
            self.respond_code(404, 'Path did not match any known request! Code 404')
            
    def do_GET(self):
        print ("\n******** NEW COMMON SERVICES GET REQUEST *********")
        print ("GET REQUEST self.path: " + self.path)
        print ("COMMON SERVICES SERVER NAME:", self.server.server_name)
        split_path = self.path.split('?', 1)
        if 'api/cs' in split_path[0]:
            db_utils = self.create_db_object()
            # parse the URL for parameters
            params = urllib.parse.parse_qs(split_path[1])
            
            # for debugging purpose:
            print("Params: " + str(params))
            if "user" in params:
                username = params['user'][0]
                if "get" in params:
                    if params['get'][0] == "name":
                        response = db_utils.get_names_from_username(username)
                    else:
                        response = db_utils.get_user_from_username(username)
                else:
                    response = db_utils.get_user_from_username(username)
                
            # Check quickly if server is running
            elif "status" in params:
                response = "Common Services listener running! (200)"
            else:
                response = None
                
            # Handle the response
            print("Response: " + str(response))
            if response != None:
                self.respond_convert_json_object (200, response)
            else:
                self.respond_code (403, "Could not find any valid params!")
                
        else:
            #Send a 404 Error handling if the route does not exist
            self.respond_code(404, "Route does not exist")

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Headers", "Authorization")
        self.end_headers()
     
    # Converts python dictionary into a json object and sends it with a code
    def respond_convert_json_object (self, code, dictionary):
        # Define the response code and the headers
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")

        # Signify that you are done sending the headers:
        self.end_headers()
        
        # convert python dictionary into a JSON object
        # encode json_object into utf_8
        self.wfile.write(json.dumps(dictionary).encode(encoding='utf_8'))
    
    # Responds with a simple code and response
    def respond_code (self, code, response):
        self.send_response(code)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        bytesStr = response.encode('utf-8')
        self.wfile.write(bytesStr)
        
    # Establish a database object
    def create_db_object(self):
        return CS_Database_Utils()

        
# Execute the web server:
def main():
    # Server port
    port = 4112

    # Create server
    httpServer = http.server.HTTPServer(('', port), CommonServicesListener)
    print("Common Services listener running on port", port)

    # Start server, use CTRL+C to close it.
    try:
        httpServer.serve_forever()
    except KeyboardInterrupt:
        httpServer.server_close()
        print ("Common Services listener Closed!")


if __name__ == "__main__":
    main()