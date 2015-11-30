from flask import Flask
import algorithm
app = Flask(__name__)

@app.route("/<playerId>")
def profile():
    return algorithm.profile(playerId)

@app.route("/stat/<playerId>")
def stat():
    return algorithm.stat(playerId)

@app.route("/growth/<playerId>")
def growth():
    return algorithm.growth(playerId)

@app.route("/simmilar/<playerId>")
def simmilar():
    return algorithm.simmilar(playerId)

@app.route("/playerId/<name>")
def playerId():
    return algorithm.getPlayerId(name)


if __name__ == "__main__":
    app.debug = True
    app.run()
