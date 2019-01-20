from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
 
app = Flask(__name__)
 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
 
@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])
 
@app.route("/playx/<int:row>/<int:col>")
def playx(row, col):
    session["board"][row][col] = "X"
    player = "X"

    session["turn"] = "O"

    status = False
    if session["board"][row][0] != None and session["board"][row][0] == session["board"][row][1] and session["board"][row][0]== session["board"][row][2]:
        status = True
    elif session["board"][0][col] != None and session["board"][0][col]== session["board"][1][col] and session["board"][0][col]== session["board"][2][col]:
        status = True
    elif session["board"][0][0] != None and session["board"][0][0] == session["board"][1][1] and session["board"][0][0] == session["board"][2][2]:
        status = True

    if status == True:
        return render_template("win.html", game=session["board"], turn=session["turn"], win=status, current=player)

    return render_template("game.html", game=session["board"], turn=session["turn"], win=status, current=player)

@app.route("/playo/<int:row>/<int:col>")
def playo(row, col):
    session["board"][row][col] = "O"
    player = "O"

    session["turn"] = "X"

    status = False
    if session["board"][row][0] != None and session["board"][row][0] == session["board"][row][1] and session["board"][row][0]== session["board"][row][2]:
        status = True
    elif session["board"][0][col] != None and session["board"][0][col]== session["board"][1][col] and session["board"][0][col]== session["board"][2][col]:
        status = True
    elif session["board"][0][0] != None and session["board"][0][0] == session["board"][1][1] and session["board"][0][0] == session["board"][2][2]:
        status = True

    if status == True:
        return render_template("win.html", game=session["board"], turn=session["turn"], win=status, current=player)

    return render_template("game.html", game=session["board"], turn=session["turn"],win=status,current=player)

@app.route("/reset")
def reset():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])
