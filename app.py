from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
 
app = Flask(__name__)
 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

game = [[None, None, None], [None, None, None], [None, None, None]]

 
@app.route("/")
def index():
    if "board" not in session:
        game = [[None, None, None], [None, None, None], [None, None, None]]
        session["board"] = game
        session["turn"] = "X"
 
    return render_template("game.html", game=session["board"], turn=session["turn"])
 
@app.route("/playx/<int:row>/<int:col>")
def playx(row, col):
    game[row][col] = "X"
    player = "X"

    session["turn"] = "O"
    status = False
    if game[row][0] != None and game[row][0] == game[row][1] and game[row][0]== game[row][2]:
        status = True
    elif game[0][col] != None and game[0][col]== game[1][col] and game[0][col]== game[2][col]:
        status = True
    elif game[0][0] != None and game[0][0] == game[1][1] and game[0][0] == game[2][2]:
        status = True

    if status == True:
        return render_template("win.html", game=game, turn=session["turn"], win=status, current=player)

    return render_template("game.html", game=game, turn=session["turn"], win=status, current=player)

@app.route("/playo/<int:row>/<int:col>")
def playo(row, col):
    game[row][col] = "O"
    player = "O"

    session["turn"] = "X"

    status = False
    if game[row][0] != None and game[row][0] == game[row][1] and game[row][0]== game[row][2]:
        status = True
    elif game[0][col] != None and game[0][col]== game[1][col] and game[0][col]== game[2][col]:
        status = True
    elif game[0][0] != None and game[0][0] == game[1][1] and game[0][0] == game[2][2]:
        status = True

    if status == True:
        return render_template("win.html", game=game, turn=session["turn"], win=status, current=player)

    return render_template("game.html", game=game, turn=session["turn"],win=status,current=player)

@app.route("/reset")
def reset():
    return redirect(url_for("index"))
