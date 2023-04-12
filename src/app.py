from flask import Flask, render_template, request, url_for
#from OpenSSL import SSL
import os.path 
import bcrypt

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

    #username = request.form['username']
    #password = request.form['password']
    
    
    return render_template('authenticated.html')

@app.route("/", methods=['POST'])
def register_post():
    
    # Get the user credentials
    username = request.form['username']
    password = request.form['password']

    p_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(p_bytes, salt)
    print(hash)
    
    # Open user credentials file
    with open(USER_CREDENTIALS, 'a+') as f:

        # Write the user credentials to the file as new user
        f.write(f"{username},{hash}\n")
        #return "User registration successfull!"
        return render_template('loggedin.html')
    

@app.route("/login", methods=['POST', 'GET'])
def log_in():
    
    if request.method == 'POST':
        # User credentials
        username = request.form['username']
        password = request.form['password']
        p_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(p_bytes, salt)
        print(hash)

        # Check if the user exists in our file
        with open(USER_CREDENTIALS, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if username in line:

                    # Check whether the password exists for the specific user
                    exists_username, exists_password = line.strip().split(',')
                    if exists_password == bcrypt.checkpw(password, hash):
                        #return f"Welcome, {username}!"
                        return render_template('loggedin.html')

                    # If not exist, return invalid credentials message
                    else:
                        return "Invalid credentials"

            else:
                return "Username does not exist."


    # If GET request, return the login template
    else:
        return render_template('login.html')
        


if __name__ == "__main__":
    app.run() 
