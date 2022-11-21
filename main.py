from flask import render_template

# import "packages" from flask
from __init__ import app
from account.app_crud import app_crud
from account.app_crud_api import app_crud_api
from personalization.app_personalization import app_personalization
from personalization.app_phonebook import app_phonebook

# redirect and url_for can be used for redirecting users to the login page if they are attempting to access their user profile,
# but they are not yet logged in.

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_personalization)
app.register_blueprint(app_phonebook)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about-dylan/')
def about_dylan():
    return render_template("about-dylan.html")


@app.route('/about-adi/')
def about_adi():
    return render_template("about-adi.html")


@app.route('/about-jean/')
def about_jean():
    return render_template("about-jean.html")


@app.route('/about-sohan/')
def about_sohan():
    return render_template("about-sohan.html")

@app.route('/about-rohan/')
def about_rohan():
    return render_template("about-rohan.html")

@app.route('/about-dev/')
def about_dev():
    return render_template("about-dev.html")


@app.route('/service-search/')
def service_search():
    return render_template("service-search.html")


@app.route('/user-profile/')
def user_profile():
    return render_template("user-profile.html")


# Service Base URLs

@app.route('/4s-ranch-sports-park/')
def sportspark():
    return render_template("/servicebase/4s-ranch-sports-park.html")

@app.route('/balboa-park/')
def balboapark():
    return render_template("/servicebase/balboa-park.html")

@app.route('/brilliant/')
def brilliant():
    return render_template("/servicebase/brilliant.html")

@app.route('/cycle-bar/')
def cyclebar():
    return render_template("/servicebase/cycle-bar.html")

@app.route('/eco-gardeners/')
def ecogardeners():
    return render_template("/servicebase/eco-gardeners.html")

@app.route('/fairbanks-ridge-tutoring/')
def fairbanks():
    return render_template("/servicebase/fairbanks-ridge-tutoring.html")

@app.route('/hamilton/')
def hamilton():
    return render_template("/servicebase/hamilton.html")

@app.route('/joshua-tree-national-park/')
def joshuatreenationalpark():
    return render_template("/servicebase/joshua-tree-national-park.html")

@app.route('/kaiser-permanente-rancho-bernardo/')
def kaiserpermanenteranchobernardo():
    return render_template("/servicebase/kaiser-permanente-rancho-bernardo.html")

@app.route('/khan-academy/')
def khanacademy():
    return render_template("/servicebase/khan-academy.html")
@app.route('/kumon/')
def kumon():
    return render_template("/servicebase/kumon.html")

@app.route('/la-fitness-4s-ranch/')
def lafitness4sranch():
    return render_template("/servicebase/la-fitness-4s-ranch.html")

@app.route('/la-jolla-pool-services/')
def lajollapoolservices():
    return render_template("/servicebase/la-jolla-pool-services.html")

@app.route('/mathnasium/')
def mathnasium():
    return render_template("/servicebase/mathnasium.html")

@app.route('/orange-theory/')
def orangetheory():
    return render_template("/servicebase/orange-theory.html")

@app.route('/pro-touch-pool-service/')
def protouchpoolservice():
    return render_template("/servicebase/pro-touch-pool-service.html")

@app.route('/rady-childrens-hospital-san-diego/')
def radychildrenshospitalsandiego():
    return render_template("/servicebase/rady-childrens-hospital-san-diego.html")

@app.route('/royall-painting/')
def royallpainting():
    return render_template("/servicebase/royall-painting.html")

@app.route('/san-ysidro-health-escondido/')
def sanysidrohealthescondido():
    return render_template("/servicebase/san-ysidro-health-escondido.html")

@app.route('/scripps-hospital-rancho-bernardo/')
def scrippshospitalranchobernardo():
    return render_template("/servicebase/scripps-hospital-rancho-bernardo.html")

@app.route('/soapy-joes-car-wash/')
def soapyjoescarwash():
    return render_template("/servicebase/soapy-joes-car-wash.html")

@app.route('/teqneeq-24-hour-gym/')
def teqneeq24hourgym():
    return render_template("/servicebase/teqneeq-24-hour-gym.html")

@app.route('/the-art-of-dentistry/')
def theartofdentistry():
    return render_template("/servicebase/the-art-of-dentistry.html")

@app.route('/uc-san-diego-health-express-care-rancho-bernardo/')
def ucsandiegohealthexpresscareranchobernardo():
    return render_template("/servicebase/uc-san-diego-health-express-care-rancho-bernardo.html")

if __name__ == "__main__":
    app.run(debug=True, port=777)
