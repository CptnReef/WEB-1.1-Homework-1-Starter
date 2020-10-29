
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    """Display an OPINION about Penguins."""
    return f'Penguins are cute!'

@app.route('/sloths')
def sloths():
    """Display a FACT about Sloths."""
    return f'Sloths are cuter than penguins and cuddlier!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How do you know I like {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madLibs(adjective,noun):
    """ Brief message, a bad joke using madlibs. Please forgive me, I'm pretty dry."""
    return f'Haha it is funny because spaghetti had {adjective} on the {noun}.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1,number2):
    """Display a message to the user that changes based on their multiplication"""

    if number1.isdigit() == True and number2.isdigit() == True:
        number = int(number1) * int(number2)
        return f'{number1} times {number2} equals {number}'
    else:
        return f'Invalid inputs: {number1} and {number2}. Please try again by entering 2 numbers!'

if __name__ == '__main__':
    app.run(debug=True)