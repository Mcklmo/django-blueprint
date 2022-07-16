import flask 
import json
import db 

# create the application object
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# get
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# run
app.run()