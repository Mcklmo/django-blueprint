import flask 
import json
import db 
from flask import request

# create the application object
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# set db connection variable
connection = None

# get requests with file responses
@app.route('/', methods=['GET'])
def home():
    return flask.render_template('index.html')

@app.route('/calculate', methods=['GET'])
def table():
    return flask.render_template('calculate.html')

# get requests with json responses
@app.route('/tables/all', methods=['GET'])
def get_tables():
    return json.dumps(db.get_tables(connection))

# post 
@app.route('/connect', methods=['POST'])
def connect():
    # connect to db with user input from post
    # data from post request
    try:
        data=request.json
        print(data)
        connection=db.connect(data["host"],data["user"],data["password"],data["database"])
        return flask.jsonify({"success":True})
    except Exception as e:
        print(e)
        return flask.jsonify({"success":False,"error":"Error "+str(e)})

# run
app.run()