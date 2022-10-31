import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from account.query import user_by_id, sqlquery_2_list, task_by_id
from personalization.model import Personalization
from __init__ import login_manager, db
import pytz

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_personalization = Blueprint('personalization', __name__,
                         url_prefix='/personalization',
                         template_folder='templates/personalization/',
                         static_folder='static',
                         static_url_path='static')

def personalization_all_alc():
    table = Personalization.query.filter(Personalization.userID == current_user.userID)
    json_ready = [peep.read() for peep in table]
    for peep in table:
        print(peep.read())
    return json_ready

# def timeline_all_sql():
#     table = db.session.execute(f'select * from timeline where userID = {current_user.userID} or access = 1')
#     print(table)
# json_ready = sqlquery_2_list(table)
# return json_ready


@app_personalization.route('/')
@login_required
def personalization():
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
    list_personalization = personalization_all_alc()
    if list_personalization is not None:
        list_personalization.reverse()
    uo = user_by_id(current_user.userID)
    if uo is not None:
        user = uo.read()
    return render_template('user-profile.html', user=user, user_by_id=user_by_id, personalization=list_personalization, msg = "Hello")

# Notes create/add
@app_personalization.route('/create/', methods=["POST"])
@login_required
def create():
    """gets data from form and add to Notes table"""
    if request.form:
        # construct a Notes object
        content_object = Personalization(
            request.form.get("name"), request.form.get("date"), request.form.get("time"), current_user.userID
        )
        # create a record in the Notes table with the Notes object
        content_object.create()
    return redirect(url_for('personalization.personalization'))

@app_personalization.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        reminderid = request.form.get("id")
        po = task_by_id(reminderid)
        if po is not None:
            po.delete()
    return redirect(url_for('personalization.personalization'))

