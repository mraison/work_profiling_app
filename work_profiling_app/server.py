from flask import Flask, request, Response, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=[1,2,3,4])


@app.route('/users', methods=['POST'])
def create_user():
    # Here we should receive a name and hand back the new user
    pass


@app.route('/skills', methods=['POST'])
def create_skill():
    # expect a skill description.
    # Here we should receive a name and hand back the new user
    pass


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
    # enter in the feed back from that collaborator for the given week for the given skill for the given user.
    # expect some numeric. (and maybe a message)
    pass




if __name__ == '__main__':
    app.run()
