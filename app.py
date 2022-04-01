#pylint: disable=invalid-name
#pylint: disable=missing-final-newline
#pylint: disable=line-too-long
#pylint: disable=unpacking-non-sequence
#pylint: disable=superfluous-parens
#pylint: disable=trailing-whitespace
#pylint: disable=wrong-import-order
#pylint: disable=unused-import
#pylint: disable=invalid-envvar-default

import os
import flask
import requests
import random

from flask import flash, redirect, url_for
from flask import request
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists,delete,func

from dotenv import find_dotenv, load_dotenv



load_dotenv(find_dotenv())


app = flask.Flask(__name__)
secret_key=os.getenv("SECRET_KEY")
app.secret_key = secret_key     




@app.route("/",methods=["GET", "POST"])
def index():
    """
    landing page, per instructions the user 
    will see an account creation option here; 
    or skip straight to the log in page 
    """
        
    return flask.render_template("index.html")


@app.route("/test")
def test():
    """
    the user will log in on this page
    """
    return flask.render_template("test.html")

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
    debug=True)