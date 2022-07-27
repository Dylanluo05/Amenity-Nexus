
from flask import Flask, render_template
#from flask_mysqldb import MySQL

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "nothing"

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


@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/personalization/')
def personalization():
    return render_template("personalization.html")

@app.route('/test/')
def test():
    return render_template("/servicebase/test.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
