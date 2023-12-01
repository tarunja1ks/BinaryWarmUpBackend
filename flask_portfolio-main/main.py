import threading
import sys
# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from aienglishprediction import aienglishprediction
from flask_cors import CORS
# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization

from flask import Flask, render_template, request, jsonify
from urllib.parse import quote as url_quote
import subprocess
import os
from generate import generate as gn # importing the generator api
app = Flask(__name__)
CORS(app)


# Initialize the SQLAlchemy object to work with the Flask app instance
# db.init_app(app)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")


@app.route("/decrypt", methods=["POST"])
def decrypt():
    text = request.json.get("text") # getting text
    output="test"
    testenglish=aienglishprediction()
    prediction=testenglish.predict(text)
    print(text,prediction,file=sys.stderr)
    return jsonify(str(prediction)) # returning the output


if __name__ == "__main__":
    
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8080")
