from flask import Flask, render_template, request, url_for, session, redirect
import os.path 
from db import create_db
import bcrypt
import conf

app = Flask(__name__, template_folder='templates', static_folder='styles')
app.secret_key = os.urandom(16)


@app.route("/")
def home():
    
    # Returns homepage/index page
    return render_template('index.html')

@app.route("/authenticated", methods=['POST', 'GET'])
def authenticated():
    """
    Authentication check for users. 
    If the user is logged in, then the authentication check approves.
    If the user is not logged in, the authentication check is not approved.
    """
    

    if not session.get('logged_in'):

        # If user is not logged in, redirect to login
        return redirect('/login')
    
    else:
        # If user is logged in, render the authenticated secret template

        return render_template('authenticated.html')
    
@app.route("/authenticatedweeb", methods=['POST', 'GET'])
def authenticated_weeb():
    """
    This is a special authentication check
    existing only for Jørn.
    """
    

    if not session.get('logged_in'):

        # If user is not logged in, redirect to login
        return redirect('/login')
    
    else:
        # If user is logged in, render the authenticated secret template

        return render_template('authenticatedweeb.html')
    
    
    

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

    check_username = conf.authenticate_user(username=username)

    # Check if username exists in database
    if check_username == True:
        return "Username already exists."
    
    else:

        # Insert user into database
        conf.reg_user(username=username, password=hash_pass)

    # Render template
    return redirect('/login')

    

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
                session['logged_in'] = username
                return redirect('/')
            else: 
                return "Wrong password."
        else:
            return "User does not exist."


    # If GET request, return the login template
    else:
        return render_template('login.html')
    
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('logged_in', None)

    # Redirect to front page
    return render_template('/loggedout.html')
        


if __name__ == "__main__":
    app.run() 
