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

@app.route('/about_dylan/')
def about_dylan():
    return render_template("about_dylan.html")


@app.route('/about_ritvik/')
def about_ritvik():
    return render_template("about_ritvik.html")


@app.route('/about_adi/')
def about_adi():
    return render_template("about_adi.html")


@app.route('/about_jean/')
def about_jean():
    return render_template("about_jean.html")


@app.route('/about_sohan/')
def about_sohan():
    return render_template("about_sohan.html")


@app.route('/about_kurtis/')
def about_kurtis():
    return render_template("about_kurtis.html")

@app.route('/about_aryan/')
def about_aryan():
    return render_template("about_aryan.html")


@app.route('/service_search/')
def service_search():
    return render_template("service_search.html")


@app.route('/sign_in/', methods = ["GET", "POST"])
def sign_in():
    if request == "POST":
        if "email" in request.form and "password" in request.form:
            emailRetrieve = request.form["email"]
            passwordRetrieve = request.form["password"]
            #databaseConnection = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            #databaseConnection.execute("SELECT * FROM User Information WHERE email = %s AND password = %s",(emailRetrieve, passwordRetrieve))
    return render_template("/account/sign_in.php")

@app.route('/sign_up/', methods = ["GET", "POST"])
def sign_up():
    return render_template("/account/sign_up.php")

@app.route('/user_profile/')
def user_profile():
    return redirect(url_for("sign_in"))

@app.route('/personalization/')
def personalization():
    return render_template("personalization.html")

#Service Base URLs
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
