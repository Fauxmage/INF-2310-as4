from flask import Flask, render_template, request, url_for
import os.path 
from db import create_db
import bcrypt
import conf

app = Flask(__name__, template_folder='templates', static_folder='styles')

USER_CREDENTIALS = "user_creds.txt"

@app.route("/")
def home():
    
    # Returns homepage/index page
    return render_template('index.html')

@app.route("/authenticated", methods=['GET'])
def register_get():
    """
    Authentication check for users. 
    If the user is logged in, then the authentication check approves.
    If the user is not logged in, the authentication check is not approved.
    """

    username = request.form['username']
    password = request.form['password']
    
    
    return render_template('authenticated.html')

@app.route("/", methods=['POST'])
def register_post():
    """ Register a new user """
    
    # Get username and password from register form
    username = request.form['username']
    password = request.form['password']

    # Hash password 
    p_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(p_bytes, salt)
    print(hash)

    # Insert user into database
    conf.reg_user(username=username, password=hash_pass)

    # Render template
    return render_template('loggedin.html')

    

@app.route("/login", methods=['POST', 'GET'])
def log_in():
    """ Log in, redirects user if successful to /loggedin, otherwise give correct error message """
    
    # If POST, attempt to login with provided user credentials
    if request.method == 'POST':

        # User credentials
        username = request.form['username']
        password = request.form['password']
        passies = password.encode('utf-8')
        print(hash)

        # Check whether the password exists for the specific user

        fetch_usr = conf.return_user(username)
        print("In app password before check:", fetch_usr)
        
        if fetch_usr != False:
            
            pwd_check = bcrypt.checkpw(passies, fetch_usr)
            if pwd_check == True:
                return render_template('loggedin.html')
            else: 
                return "Wrong password."
        else:
            return "User does not exist."


    # If GET request, return the login template
    else:
        return render_template('login.html')
    
        


if __name__ == "__main__":
    app.run() 
