from flask import Flask, render_template, redirect, url_for, session, request
# redirect and url_for can be used for redirecting users to the login page if they are attempting to access their user profile,
# but they are not yet logged in.
#from flask_mysqldb import MySQL
#import MySQLdb

# create a Flask instance
app = Flask(__name__)

app.secret_key = 'service-NEXUS-a72387as349sjidla02'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'service-nexus'
app.config['MYSQL_PASSWORD'] = 'NEXUS-TEMP'
app.config['MYSQL_DB'] = 'nexus'

#mysql = MySQL(app)


@app.route('/')
def home():
    return render_template("/foundation/home.html")

@app.route('/aboutdylan/')
def aboutdylan():
    return render_template("aboutdylan.html")


@app.route('/aboutritvik/')
def aboutritvik():
    return render_template("aboutritvik.html")


@app.route('/aboutadi/')
def aboutadi():
    return render_template("aboutadi.html")


@app.route('/aboutjean/')
def aboutjean():
    return render_template("aboutjean.html")


@app.route('/aboutsohan/')
def aboutsohan():
    return render_template("aboutsohan.html")


@app.route('/aboutkurtis/')
def aboutkurtis():
    return render_template("aboutkurtis.html")

@app.route('/aboutaryan/')
def aboutaryan():
    return render_template("aboutaryan.html")


@app.route('/servicesearch/')
def servicesearch():
    return render_template("servicesearch.html")


@app.route('/signin/', methods = ["GET", "POST"])
def signin():
    if request == "POST":
        if "email" in request.form and "password" in request.form:
            emailRetrieve = request.form["email"]
            passwordRetrieve = request.form["password"]
            #databaseConnection = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            #databaseConnection.execute("SELECT * FROM User Information WHERE email = %s AND password = %s",(emailRetrieve, passwordRetrieve))
    return render_template("/account/signin.html")

@app.route('/signup/', methods = ["GET", "POST"])
def signup():
    return render_template("/account/signup.html")

@app.route('/user_profile/')
def user_profile():
    return redirect(url_for("signin"))

@app.route('/personalization/')
def personalization():
    return render_template("personalization.html")

#Service Base URLs
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
