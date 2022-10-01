from flask import Flask, render_template, redirect, url_for, session, request
# redirect and url_for can be used for redirecting users to the login page if they are attempting to access their user profile,
# but they are not yet logged in.
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_login import current_user

# import "packages" from flask
from __init__ import app
from account.app_crud import app_crud

from account.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


@app.route('/')
def home():
    return render_template("/foundation/home.html")

@app.route('/about-dylan/')
def about_dylan():
    return render_template("about-dylan.html")


@app.route('/about-ritvik/')
def about_ritvik():
    return render_template("about-ritvik.html")


@app.route('/about-adi/')
def about_adi():
    return render_template("about-adi.html")


@app.route('/about-jean/')
def about_jean():
    return render_template("about-jean.html")


@app.route('/about-sohan/')
def about_sohan():
    return render_template("about-sohan.html")



@app.route('/service-search/')
def service_search():
    return render_template("service-search.html")

@app.route('/personalization/')
def personalization():
    return render_template("personalization.html")

#Service Base URLs
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")

@app.route('/teqneeq-24-hour-gym/')
def teqneeq24hourgym():
    return render_template("/servicebase/teqneeq-24-hour-gym.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
