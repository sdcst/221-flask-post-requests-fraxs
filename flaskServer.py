#!python3
from flask import Flask, request
from flask_cors import CORS
import time, json

app = Flask(__name__)   # creates a flask server with name/handle of app
CORS(app)               # applies cross domain object requests to app

@app.route("/",methods=['POST','GET'])
def main():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded
    return "Hello World (use /help endpoint for a list of options)"

@app.route("/post",methods=['POST'])
def postData():
    #sample url: http://127.0.0.1:5000/post
    #not accessible from a browser because it must be a post request
    #response is a json encoded string that includes the payload
    #payload is retrieved as data and then converted to a dict
    #dict is echoed back
    data = request.form
    data = dict(data)
    if 'greeting' not in data:
        data['greeting'] = "Hello!"
    return json.dumps(data)


@app.route("/help",methods=['GET','POST'])
def help():
    #sample url: http://127.0.0.1:5000/help 
    #output: multline string literal.  Displays endpoint options
    #may use GET or POST methods
    #response is not json encoded
    return """
    Acceptable endpoints: 
    /     : General
    /help : this page
    /html : html result
    /getData: a GET method only endpoint
    /json : a POST method only endpoint that takes a json payload
    """

@app.route("/html",methods=['GET'])
def html():
    #sample url: http://127.0.0.1:5000/html
    #output: simple html statement
    #only available with GET method 
    #response is not json encoded
    return "<h1>Hello World</h1>"

@app.route("/getData")
def getData():
    #sample url: http://127.0.0.1:5000/getData?x=1&y=2&myName=George
    #url can contain GET variables included in the URL
    #output: json encoded data from the response
    #response is json encoded
    x = request.args
    output = dict(x)
    output['title'] = "This is a response from a GET request"
    return json.dumps(output)

@app.route("/json",methods=['POST'])
def jsondata():
    #url: http://127.0.0.1:5000/json
    #only POST data is allowed
    #data sent from ajax form request is retrieved 
    #response is sent back json encoded
    output = {
        "greeting" : "Hello World",
        "success" : 100,
        "timestamp" : time.time()
    }
    x = request.form
    x = dict(x)
    output['payload'] = x
    return json.dumps(output)


app.run()           #starts the app in test mode with default settings
