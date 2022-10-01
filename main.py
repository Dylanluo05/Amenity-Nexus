# redirect and url_for can be used for redirecting users to the login page if they are attempting to access their user profile,
# but they are not yet logged in.
import MySQLdb.cursors
from flask import render_template, redirect, url_for, session, request


# create a Flask instance
# app = Flask(__name__)

# app.secret_key = 'service-NEXUS-a72387as349sjidla02'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'service-nexus'
# app.config['MYSQL_PASSWORD'] = 'NEXUS-TEMP'
# app.config['MYSQL_DB'] = 'nexusdatabase'

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


@app.route('/signin/', methods=["GET", "POST"])
def signin():
    msg = ""
    if request == "POST" and "email" in request.form and "password" in request.form:
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM useraccounts WHERE email = %s and password = %s", (email, password,))
        user_account = cursor.fetchone()
        if user_account:
            session["signedin"] = True
            session["id"] = user_account["id"]
            session["email"] = user_account["email"]
            return "Sign in was successful!"
        else:
            msg = "Incorrect email and/or password!"
    return render_template("/account/signin.html", msg=msg)


@app.route('/signout/')
def signout():
    session.pop("signedin", None)
    session.pop("id", None)
    session.pop("email", None)
    return redirect(url_for("signin"))


@app.route('/signup/', methods=["GET", "POST"])
def signup():
    msg = ""
    if request.method == "POST" and "email" in request.form and "password" in request.form:
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM useraccounts WHERE email = %s", (fullname,))
        user_account = cursor.fetchone()
        if user_account:
            msg = "User account already exists!"
        else:
            cursor.execute("INSERT INTO useraccounts VALUES (NULL, %s, %s,)", (fullname, password, email,))
            mysql.connection.commit()
            msg = "You have successfully created a new account!x"
    return render_template("/account/signup.html", msg=msg)


@app.route("/userprofile/")
def userprofile():
    if "signedin" in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM useraccounts WHERE id = %s", (session["id"],))
        user_account = cursor.fetchone()
        return render_template("/account/userprofile.html", user_account=user_account)
    return redirect(url_for("signin"))


@app.route('/personalization/')
def personalization():
    return render_template("personalization.html")


@app.route('/crud-test/')
def crudtest():
    return render_template("crud-test.html")


# Service Base URLs
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")


@app.route('/mathnasium/')
def mathnasium():
    return render_template("/servicebase/mathnasium.html")


@app.route('/teqneeq-24-hour-gym/')
def teqneeqgym():
    return render_template("/servicebase/teqneeq-24-hour-gym.html")


@app.route('/The Art of Dentistry/')
def artofdentistry():
    return render_template("/servicebase/The Art of Destistry.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
