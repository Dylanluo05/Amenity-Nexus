from flask import Flask, render_template, redirect, url_for, request

# redirect and url_for can be used for redirecting users to the login page if they are attempting to access their user profile,
# but they are not yet logged in.
# from flask_mysqldb import MySQL
# import MySQLdb

# create a Flask instance
app = Flask(__name__)

app.secret_key = 'service-NEXUS-a72387as349sjidla02'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'service-nexus'
app.config['MYSQL_PASSWORD'] = 'NEXUS-TEMP'
app.config['MYSQL_DB'] = 'nexus'


# mysql = MySQL(app)


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


@app.route('/about-kurtis/')
def about_kurtis():
    return render_template("about-kurtis.html")


@app.route('/about-aryan/')
def about_aryan():
    return render_template("about-aryan.html")


@app.route('/service-search/')
def service_search():
    return render_template("service-search.html")


@app.route('/sign-in/', methods=["GET", "POST"])
def sign_in():
    if request == "POST":
        if "email" in request.form and "password" in request.form:
            emailRetrieve = request.form["email"]
            passwordRetrieve = request.form["password"]
            # databaseConnection = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # databaseConnection.execute("SELECT * FROM User Information WHERE email = %s AND password = %s",(emailRetrieve, passwordRetrieve))
    return render_template("/account/sign-in.php")


@app.route('/sign-up/', methods=["GET", "POST"])
def sign_up():
    return render_template("/account/sign-up.php")


@app.route('/user-profile/')
def user_profile():
    return redirect(url_for("sign_in"))


@app.route('/personalization/')
def personalization():
    return render_template("personalization.html")


# Service Base URLs
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")


@app.route('/mathnasium/')
def mathnasium():
    return render_template("/servicebase/mathnasium.html")


@app.route('/khan-academy/')
def khanacademy():
    return render_template("/servicebase/khan-academy.html")


@app.route('/teqneeq-24-hour-gym/')
def khanacademy():
    return render_template("/servicebase/teqneeq-24-hour-gym.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
