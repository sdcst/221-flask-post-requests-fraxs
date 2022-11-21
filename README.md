## SDSS Computing Studies Python Assignment
### Flask!

Objectives:
* To create a basic flask server that receives form data
* To have a flask server respond to a post request
* Create a client python file that can make a post request to a server

### POST Requests
There are two standard methods by which a server can serve a request/response: GET and POST.

GET requests are the ones that are made in the URL, and are generally made using a browser. When you go to Google and search for cats, you can use this URL: https://www.google.com/search?q=cats  
This is an example of a GET method, where the information to be sent is included in the URL.

POST Requests are hidden. This is very important when you don't want sensitive data (such as passwords or cryptographic keys) to be displayed or visible in the URL.  We instead embed data inside the request itself which is received by the server.  The data that is sent is often called a *Payload*.  It usually consists of key-value pairs, much like we would see in a dictionary.  In fact, we can send a dictionary as the payload in a post request.  Note that only single level dictionaries can be sent....Dictionaries nested inside dictionaries do not work.

Today, we will be looking at some important commands in both a flask SERVER program, and a python CLIENT program.

### Server Considerations
We need to include a couple new items. Look at the file postServer.py as your example.

```from flask import request```
This is required to retrieve the form data from your post request
```payload = request.form```
This is where we actually retrieve the payload from the request.  It does need to be converted to a dictionary for us to use.

## Client Considerations
We need to import the requests module in order to mak a server request by GET or POST from a python program.
One of the methods in the requests module is the .post() method.  While it has many important arguments/parameters, the most important one is the URL of the server.  Another optional argument is "data" which will include any form data that you need to send.  This is generally of a type tuple or list or dictionary.
In our example file client.py we are making a post request using a dictionary.

## Assignment
Add new quotes by POST
Last class, we created an API endpoint that connected to a Flask server, providing quotes/facts/jokes when GET requests were made.  Today, we will extend the functionality by adding an endpoint that only serves POST requests; we can add on to that existing assignment, or if you want you can create a separate assignment that connects to the same dbase file.
We will be sending it a dictionary that must contain (at a minimum) the following information:
* the quote
* a SHA256 hashed key (for security). You will build this into your program without the need for the user to enter it.  What is SHA256?  You can read about it here: https://xorbin.com/tools/sha256-hash-calculator and you can also generate a SHA256 hash from a random phrase.

Your client script will ask the user for a quote/joke.
The client will send a payoad that contains the key, the quote/joke along with any other information you may need (you might specify the name of the table or database
The server script will search for similar entries in the database, and if there is no math, it will add it to the database.  You may want to consider the use of wildcards to help you out: https://www.sqlitetutorial.net/sqlite-like/. You can view the 'sqlLike.py' file for an example.

Other functionality:
Write another client script and api endpoint that do the following:
Client Script requests a list of all quotes/jokes from the server.  When it retrieves a result, it displays them all to the user in alphabetical order for ease of viewing
Server script should have an endpoint that allows for retrieval of ALL quotes, sorted into alphabetical order.
