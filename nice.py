from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

INSULTNESS = [
    'YOU STINK!',"YOUR FATHER SMELLED OF ELDERBERRIES!","YOUR MOTHER WAS A HAMSTER!"]

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        <p><a href=http://localhost:5000/hello>Click for a greeting!</a></p>
        <p><a href=http://localhost:5000/diss>Click for an insult, ya dummy!</a></p>
      </body> 
    </html>
    """


@app.route('/hello')
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
          <label for= "compliment">Compliment:</label>
            <select name="self-compliment" id="compliment">
              <option value="pretty">Pretty</option>
              <option value="pretty and smart">Pretty & Smart</option>
              <option value="just smart">Just Smart</option>
            </select>
          <br>

          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    nice_word = request.args.get("self-compliment")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s, you are %s and I think you're %s!
      </body>
    </html>
    """ % (player,nice_word, compliment)

@app.route('/diss')
def diss_person():
  """Give person a diss"""

  insult = choice(INSULTNESS)
  return """
  <!doctype html>
  <html>
    <head>
      <title>INSULT</title>
    </head>
    <body>
      %s
    </body>
  </html>
  """ % (insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
