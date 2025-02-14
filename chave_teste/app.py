from flask import Flask, render_template, redirect, url_for, session

from routes.amistoso import  amistoso_route
from routes.partidas import partidas_route
from routes.times import times_routes
from routes.campeonato import campeonato_route

app = Flask(__name__)
app.register_blueprint(amistoso_route, url_prefix="/amistoso")
app.register_blueprint(partidas_route, url_prefix="/partidas")
app.register_blueprint(times_routes, url_prefix="/times")
app.register_blueprint(campeonato_route, url_prefix="/campeonato")


app.secret_key = "Sapato_amassado"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/vencedor")
def vencedor():
    return render_template("winner.html", vencedor= vencedor)

@app.route("/logout")
def sair():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
