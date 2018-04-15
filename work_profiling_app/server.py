from flask import Flask, request, Response, jsonify, render_template
from functools import wraps
import json
import sys


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_user():
    # Here we should receive a name and hand back the new user
    pass


@app.route('/users/<user_id>/skills', methods=['POST'])
def define_new_skill(user_id):
    # user_id: the user who is gaining the skill.
    # Should receive a new skill name (e.g. critical thinking, communication, etc.)
    pass


@app.route('/users/<user_id>/skills/<skill_id>/collaborators', methods=['POST'])
def add_new_collaborator(user_id, skill_id):
    # user_id: the user who is gaining the skill.
    # skill_id: skill to add the collaborator to. I'm not sure if this makes sense but
    #           the idea is that some collaborators may speak more strongly to one set than another.
    #           and this allows users to group the skills they'd like to develop with the people they
    #           want to develop them with.
    pass


@app.route('/users/<user_id>/skills/<skill_id>/collaborators/<collab_id>/weeks', methods=['POST'])
def start_new_week(user_id, skill_id, collab_id):
    # user_id: the user who is starting the new week.
    # skill_id: the skill(s) the user is tracking this week.
    # collab_id: the collaborator(s) for this week.
    # Don't expect to receive any data, just iterate up one from the previous week
    pass


@app.route('/users/<user_id>/skills/<skill_id>/collaborators/<collab_id>/weeks/<week_id>/give_feedback', methods=['POST'])
def give_feedback(user_id, skill_id, collab_id, week_id):
    # enter in the feed back from that collaborator for the given week for the given skill for the given user.
    # expect some numeric. (and maybe a message)
    pass


# here's where we want to get progress.
# The way you should read it is thus:
# ---- How did <user_id> improve their <cat_id> skills during week <week_id> according to <collab_id>
@app.route('/users/<user_id>/skills/<skill_id>/collaborators/<collab_id>/weeks/<week_id>/get_feedback', methods=['GET'])
def get_progress(user_id, skill_id, collab_id, week_id):
    pass





if __name__ == '__main__':
    app.run()
