"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

NOTAWESOME = ['bad', 'mean', 'ugly']
AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body>
        Hi! This is the home page.
        <a href="http://localhost:5000/hello">Link Text</a>
      </body>  
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
            Select a compliment:
            <select name="compliment">
                <option value="awesome">Awesome</option>
                <option value="terrific">Terrific</option>
                <option value="fantastic">Fantastic</option>
            </select>
            <input type="submit" value="Submit">
        </form>
        <a href="http://localhost:5000/diss">Click for insult</a>
      </body>
    </html>
    """

@app.route("/diss")
def say_diss():

    return"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/insult">
          What's your name? <input type="text" name="person2">
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """



@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    #insult = choice(NOTAWESOME)

    #y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/insult")
def insult():
    """Get user by name."""

    player2 = request.args.get("person2")
    #compliment = request.args.get("compliment")

    insult = choice(NOTAWESOME)

    #y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player2, insult)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=False, host="0.0.0.0")
