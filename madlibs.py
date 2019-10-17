"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    answer = request.args.get("yesno")

    possible_games = ["game.html", "game2.html"]

    if answer == "yes":
        return render_template(choice(possible_games))

    # elif answer == "hellyes":
    #     return render_template("game2.html")

    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    color = request.args.get("color")

    return render_template("madlib.html", person=person,
                           noun=noun,
                           adjective=adjective,
                           color=color)


@app.route('/madlib2')
def show_second_madlib():
    name = request.args.get("name")
    gender = request.args.get("gender")
    color1 = request.args.get("color1")
    color2 = request.args.get("color2")
    color3 = request.args.get("color3")
    size_adj = request.args.getlist("size-adj")  # checkboxes
    room = request.args.get("room")
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    time = request.args.get("time")

    male = ['he', 'him', 'his']
    female = ['she', 'her', 'her']
    other = ['they', 'them', 'their']

    if gender == 'boy':
        nominative, oblique, possessive = male
    elif gender == 'girl':
        nominative, oblique, possessive = female
    else:
        nominative, oblique, possessive = other

    return render_template("madlib2.html",
                           name=name,
                           color1=color1,
                           color2=color2,
                           color3=color3,
                           size_adj=size_adj,
                           room=room,
                           number1=number1,
                           number2=number2,
                           time=time,
                           nominative=nominative,
                           oblique=oblique,
                           possessive=possessive
                           )


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
