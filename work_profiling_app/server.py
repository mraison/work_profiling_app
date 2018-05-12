from flask import Flask, request
from flask import jsonify
from modules.controllers.baseController import baseController
from modules.controllers.users.usersController import usersController
from modules.controllers.skills.skillsController import skillsController
import json

from modules.views.baseView import baseView

app = Flask(__name__)

appSession = None

@app.before_request
def startSession():
    global appSession
    appSession = {
        'url': request.base_url,
        'method': request.method,
        'returnFormat': request.args.get('format'),
        'postData': request.form,
        'urlArgs': request.args
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    c = baseController(appSession)
    return c.index()


@app.route('/users', methods=['GET', 'POST'])
def users():
    # Here we should receive a name and hand back the new user
    c = usersController(appSession)
    if appSession['method'] == 'POST':
        return c.createUser()
    else:
        return c.index()


@app.route('/skill', methods=['GET', 'POST'])
def skills():
    appSession['returnFormat'] = 'json'
    # Here we should receive a name and hand back the new user
    c = skillsController(appSession)
    if appSession['method'] == 'POST':
        return c.createSkills()
    else:
        return c.index()


@app.route('/skillSet', methods=['POST'])
def skillSets():
    # return jsonify(appSession)
    appSession['returnFormat'] = 'json'
    # Here we should receive a name and hand back the new user
    c = skillsController(appSession)
    # if appSession['method'] == 'POST':
    return c.createSkillSets()
    # else:
    #     return c.index()

@app.route('/users/<userId>', methods=['GET', 'POST'])
def user(userId):
    # Here we should receive a name and hand back the new user
    c = usersController(appSession)
    return c.user(userId)


@app.route('/skills/<skillId>', methods=['GET', 'POST'])
def skill(skillId):
    # Here we should receive a name and hand back the new user
    c = skillsController(appSession)
    return c.skill(skillId)

@app.route('/users/<user_id>/skills', methods=['POST'])
def add_new_skill_for_user(user_id):
    # user_id: the user who is gaining the skill.
    # Should receive a new skill id
    pass


@app.route('/users/<user_id>/collaborators', methods=['POST'])
def add_new_collaborator(user_id, skill_id):
    # user_id: the user who is gaining the skill.
    # expect a collab_id for the id of the collaborator.
    pass


@app.route('/users/<user_id>/weeks', methods=['POST'])
def start_new_week(user_id, skill_id, collab_id):
    # user_id: the user who is starting the new week.
    # don't expect anything to be given. incrememnt on the week id. This should be an integer counter.
    pass


@app.route('/users/<user_id>/skills/<skill_id>/collaborators/<collab_id>/weeks/<week_id>/give_feedback', methods=['GET', 'POST'])
def give_feedback(user_id, skill_id, collab_id, week_id):
    # @todo Make a controller folder for this!!!
    # enter in the feed back from that collaborator for the given week for the given skill for the given user.
    # expect some numeric. (and maybe a message)
    pass




if __name__ == '__main__':
    app.run()
