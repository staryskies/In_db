# app.py
from  db import workerDb
from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

db = workerDb()

class Chat(Resource):
    def get(self):
        return jsonify(db.returnAll())

    def post(self):
        new_message = request.json.get('message')
        user = request.json.get('user')
        db.insert(user, new_message)
        return jsonify({'user': user, 'message': new_message}), 201

api.add_resource(Chat, '/chat')

@app.route('/')
def index():
    print("index")
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
