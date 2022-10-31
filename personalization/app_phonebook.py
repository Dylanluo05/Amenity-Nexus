import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from account.query import user_by_id, sqlquery_2_list, task_by_id
from personalization.model import Personalization
from personalization.model2 import Phonebook
from __init__ import login_manager, db
import pytz

app_phonebook = Blueprint('phonebook', __name__,
                          url_prefix='/phonebook',
                          template_folder='templates/phonebook/',
                          static_folder='static',
                          static_url_path='static')

def phonebook_all_alc():
    table = Phonebook.query.filter(Phonebook.userID == current_user.userID)
    json_ready = [peep.read() for peep in table]
    for peep in table:
        print(peep.read())
    return json_ready

# def timeline_all_sql():
#     table = db.session.execute(f'select * from timeline where userID = {current_user.userID} or access = 1')
#     print(table)
# json_ready = sqlquery_2_list(table)
# return json_ready


@app_phonebook.route('/')
@login_required
def phonebook():
    # # defaults are empty, in case user data not found
    # # print(timeline_all_sql())
    # user = ""
    # list_timeline = []
    #
    # # grab user database object based on current login
    # uo = user_by_id(current_user.userID)
    #
    # # if user object is found
    # if uo is not None:
    #     user = uo.read()  # extract user record (Dictionary)
    #     # print(uo)
    #     # print(user)
    #     # print(uo.timeline)
    #     for content in uo.timeline:  # loop through each user note
    #         # print(content)
    #         content = content.read()  # extract note record (Dictionary)
    #         content['content'] = markdown.markdown(content['content'])  # convert markdown to html
    #         list_timeline.append(content)  # prepare note list for render_template
    #     if list_timeline is not None:
    #         list_timeline.reverse()
    # # render user and note data in reverse chronological order(display latest notes rec on top)
    # # print(list_timeline)
    list_phonebook = phonebook_all_alc()
    if list_phonebook is not None:
        list_phonebook.reverse()
    uo = user_by_id(current_user.userID)
    if uo is not None:
        user = uo.read()
    return render_template('user-profile.html', user=user, user_by_id=user_by_id, phonebook=list_phonebook)

# Notes create/add
@app_phonebook.route('/create2/', methods=["POST"])
@login_required
def create2():
    """gets data from form and add to Notes table"""
    if request.form:
        # construct a Notes object
        content_object = Phonebook(
            request.form.get("servicephonenumber1"), request.form.get("servicephonenumber2"), request.form.get("servicephonenumber3"),
            request.form.get("servicephonenumber4"), request.form.get("servicephonenumber5"), request.form.get("servicephonenumber6"),
            request.form.get("servicephonenumber7"), request.form.get("servicephonenumber8"), request.form.get("servicephonenumber9"),
            request.form.get("servicephonenumber10"), request.form.get("servicephonenumber11"), request.form.get("servicephonenumber12"),
            request.form.get("servicephonenumber13"), request.form.get("servicephonenumber14"), request.form.get("servicephonenumber15"),
            request.form.get("servicephonenumber16"), request.form.get("servicephonenumber17"), request.form.get("servicephonenumber18"),
            request.form.get("servicephonenumber19"), request.form.get("servicephonenumber20"), request.form.get("servicephonenumber21"),
            current_user.userID
        )
        # create a record in the Notes table with the Notes object
        content_object.create()
    return redirect(url_for('phonebook.phonebook'))

#@app_phonebook.route('/delete2/', methods=["POST"])
#def delete2():
#    """gets userid from form delete corresponding record from Users table"""
#    if request.form:
#        reminderid = request.form.get("id")
#        po = task_by_id(reminderid)
#        if po is not None:
#            po.delete()
#    return redirect(url_for('phonebook.phonebook'))