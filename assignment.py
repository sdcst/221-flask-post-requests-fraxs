from flask import Flask, request, render_template
from flask_cors import CORS
import random
import time, json
app = Flask(__name__) 
CORS(app)  
@app.route("/",methods=['POST','GET'])
def main():
    quotes = []
    file = open("quotes.txt",'r')
    file = file.read()
    newlist = file.split("\n")
    for i in newlist:
        if i not in quotes:
            quotes.append(i)
    count = 0
    for i in range(len(quotes)-1):
        count += 1
    randomnumber = random.randint(0,count)
    return quotes[randomnumber]
@app.route("/admin",methods=['POST','GET'])
def admin():
    quotes = []
    file = open("quotes.txt",'r')
    file = file.read()
    newlist = file.split("\n")
    for i in newlist:
        if i not in quotes:
            quotes.append(i)
    new = ''
    for i in quotes:
        new = new + f"{i}<br>"
    return new
@app.route("/add",methods=['POST','GET'])
def newquote():
    form_data = request.form
    form_data = dict(form_data)
    with open('quotes.txt','a') as f:
        f.write(f"\n{form_data['val1']}")
    return 'received'


app.run()  