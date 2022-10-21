from flask import render_template

# import "packages" from flask
from __init__ import app
from account.app_crud import app_crud
from account.app_crud_api import app_crud_api
from personalization.app_personalization import app_personalization

# redirect and url_for can be used for redirecting users to the login page if they are attempting to access their user profile,
# but they are not yet logged in.

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_personalization)


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


@app.route('/service-search/')
def service_search():
    return render_template("service-search.html")


@app.route('/user-profile/')
def user_profile():
    return render_template("user-profile.html")


# Service Base URLs
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")


@app.route('/teqneeq-24-hour-gym/')
def teqneeq24hourgym():
    return render_template("/servicebase/teqneeq-24-hour-gym.html")


@app.route('/khan-academy/')
def khanacademy():
    return render_template("/servicebase/khan-academy.html")


@app.route('/mathnasium/')
def mathnasium():
    return render_template("/servicebase/mathnasium.html")


@app.route('/orange-theory/')
def orangetheory():
    return render_template("/servicebase/orange-theory.html")


@app.route('/cycle-bar/')
def cyclebar():
    return render_template("/servicebase/cycle-bar.html")


@app.route('/the-art-of-dentistry/')
def theartofdentistry():
    return render_template("/servicebase/the-art-of-dentistry.html")


@app.route('/fairbanks-ridge-tutoring/')
def fairbanksridgetutoring():
    return render_template("/servicebase/fairbanks-ridge-tutoring.html")


@app.route('/4sboysandgirlsclub/')
def boysandgirlsclub():
    return render_template("4sboysandgirlsclub.html")


@app.route('/balboapark/')
def balboapark():
    return render_template("balboapark.html")


@app.route('/joshuatreenationalpark/')
def joshuatreenationalpark():
    return render_template("joshuatreenationalpark.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)
