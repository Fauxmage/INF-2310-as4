from flask import Flask, render_template, request, url_for
import os.path 

app = Flask(__name__, template_folder='templates', static_folder='styles')


@app.route("/")
def home():

    return render_template('index.html')


if __name__ == "__main__":
    app.run() 