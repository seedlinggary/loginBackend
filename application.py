from flask import Flask,jsonify,request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
uri = "mongodb+srv://g:g@login.jdjp7ql.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.login


@app.route('/login', methods=['POST'])
def log_in():
    # db.users.insert_one({'email': 'BigJoe@gmail.com', 'password': 'John', 'first_name': 'Joe'})
    existing_user = db.users.find_one({'email': request.json['email']})
    if existing_user and existing_user['password'] == request.json['password']:
        return jsonify('Logged In')
    
    return jsonify('Log In Failed')

if(__name__) == '__main__':
    # app.run()

    app.run(debug=True)