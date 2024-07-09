from db import msgDb
from userdb import userDb
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Set a secret key for session management
api = Api(app)

db = msgDb()
userdb = userDb()

class Chat(Resource):
    def get(self):
        if 'logged_in' not in session:
            return {'error': 'Not logged in'}, 401
        user = session.get('username')
        recipient = request.args.get('recipient', 'global')
        if recipient == 'global':
            return db.returnByGlobal()
        else:
            return db.returnByFilter(user, recipient)

    def post(self):
        if 'logged_in' not in session:
            return {'error': 'Not logged in'}, 401
        new_message = request.json.get('message')
        user = session.get('username')
        recipient = request.json.get('recipient', 'global')
        db.insert(user, recipient, new_message)
        return {'user': user, 'recipient': recipient, 'message': new_message}, 201

api.add_resource(Chat, '/chat')

@app.route('/')
def root():
    if 'logged_in' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Here you should verify the user's credentials
    # For now, we'll just set the session
    session['logged_in'] = True
    session['username'] = username
    return redirect(url_for('index'))

@app.route('/index')
def index():
    if 'logged_in' in session:
        dm_list = get_dm_list_for_user(session.get('username'))
        return render_template('index.html', username=session.get('username'), dm_list=dm_list)
    else:
        return redirect(url_for('root'))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return '', 204

@app.route('/get_messages/<recipient>')
def get_messages_route(recipient=None):
    if 'logged_in' not in session:
        return jsonify({"error": "Not logged in"}), 401
    sender = session.get('username')
    messages = db.returnByFilter(sender, recipient)
    return jsonify(messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'logged_in' not in session:
        return jsonify({"error": "Not logged in"}), 401
    data = request.json
    sender = session.get('username')
    recipient = data.get('recipient')
    message = data.get('message')
    db.insert(sender, recipient, message)
    return jsonify({"status": "success"}), 200

def get_dm_list_for_user(username):
    # Implement this function to return a list of users
    # that the current user has had conversations with
    # For now, we'll return a dummy list
    return ['user1', 'user2', 'user3']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)