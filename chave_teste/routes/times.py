from flask import Blueprint, render_template, request
from database.grupos import DUPLA, TRIO, SEIS
from routes.utils import adicionar_jogador, exibir_nomes

times_routes = Blueprint("times_routes", __name__)

@times_routes.route("/", methods=["POST", "GET"])
def times():
    erro = request.args.get("erro", None)
    sucesso = request.args.get("sucesso", None)

    if DUPLA:
        exibir = exibir_nomes(DUPLA, 2)
        if len(DUPLA[-1]) < 2:
            return render_template("formacao.html", nomes=exibir, erro="Há um time incompleto!")
        return render_template("times.html", times=DUPLA, erro=erro, sucesso=sucesso)

    elif TRIO:
        exibir = exibir_nomes(TRIO, 3)
        if len(TRIO[-1]) < 3:
            return render_template("formacao.html", nomes=exibir, erro="Há um time incompleto!")
        return render_template("times.html", times=TRIO, erro=erro, sucesso=sucesso)

    elif SEIS:
        exibir = exibir_nomes(SEIS, 6)
        if len(SEIS[-1]) < 6:
            return render_template("formacao.html", nomes=exibir, erro="Há um time incompleto!")
        return render_template("times.html", times=SEIS, erro=erro, sucesso=sucesso)

    return render_template("formacao.html", nomes=[], erro="Nenhum time foi formado ainda")


@times_routes.route("/dupla", methods=["POST"])
def dupla():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(DUPLA, jogador, 2)
    return render_template("formacao.html", nomes=exibir_nomes(DUPLA, 2))


@times_routes.route("/trio", methods=["POST"])
def trio():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(TRIO, jogador, 3)
    return render_template("formacao.html", nomes=exibir_nomes(TRIO, 3))


@times_routes.route("/seis", methods=["POST"])
def seis():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(SEIS, jogador, 6)
    return render_template("formacao.html", nomes=exibir_nomes(SEIS, 6))
