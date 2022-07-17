import flask 
import json
import db 

# create the application object
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# get
@app.route('/', methods=['GET'])
def home():
    return flask.render_template('index.html')

# run
app.run()