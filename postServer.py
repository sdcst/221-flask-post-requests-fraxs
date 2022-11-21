#!python

from flask import Flask,request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/post",methods=["POST"])
def postResponse():
    # a simple echo server that response with the payload received.
    payload = request.form
    data = dict(payload)
    print(data)
    return json.dumps(data)


app.run()