from flask import Blueprint, render_template, request, redirect, url_for, session
from database.grupos import DUPLA, TRIO, SEIS, CHAVES
from routes.utils import adicionar_jogador, exibir_nomes , verificar_times
import random

campeonato_route = Blueprint("campeonato_route", __name__)

@campeonato_route.route("/", methods=["GET", "POST"])
def home():
    return render_template("campeonato.html")

@campeonato_route.route("/verificar", methods=["POST"])
def verificar():
    if verificar_times(DUPLA, 2):
        return render_template("campeonato.html", nomes=exibir_nomes(DUPLA, 2), erro="Há um time incompleto!")
    if verificar_times(TRIO, 3):
        return render_template("campeonato.html", nomes=exibir_nomes(TRIO, 3), erro="Há um time incompleto!")
    if verificar_times(SEIS, 6):
        return render_template("campeonato.html", nomes=exibir_nomes(SEIS, 6), erro="Há um time incompleto!")
    
    return redirect("formar_chaves.html")

@campeonato_route.route("/dupla", methods=["POST"])
def dupla_campeonato():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(DUPLA, jogador, 2)
    
    if verificar_times(DUPLA, 2):
        return render_template("formacao.html", nomes=exibir_nomes(DUPLA, 2), erro="Há um time incompleto!")

    return render_template("formacao.html", nomes=exibir_nomes(DUPLA, 2))


@campeonato_route.route("/trio", methods=["POST"])
def trio_campeonato():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(TRIO, jogador, 3)
    
    if verificar_times(TRIO, 2):
        return render_template("formacao.html", nomes=exibir_nomes(TRIO, 2), erro="Há um time incompleto!")

    return render_template("formacao.html", nomes=exibir_nomes(TRIO, 3))

@campeonato_route.route("/seis", methods=["POST"])
def seis_campeonato():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(SEIS, jogador, 6)

    if verificar_times(SEIS, 6):
        return render_template("formacao.html", nomes=exibir_nomes(SEIS, 6), erro="Há um time incompleto!")

    return render_template("formacao.html", nomes=exibir_nomes(SEIS, 6))


@campeonato_route.route("/chaves", methods= ["POST"])
def formar_chaves(lista, limite):
    if request.method == "GET":
        return render_template("campeonato.html")
    else:
        partida = []
        lista_embaralhada = lista.copy()
        random.shuffle(lista_embaralhada)
        print(f"COPIA: {lista_embaralhada}")

        for time in lista_embaralhada:
            if partida and len(partida[-1]) < limite:
                partida[-1].append(time)

            else:
                partida.append([time])

        for x in range(0,len(partida)):
            (CHAVES.append(partida[x]))

        print(f"CHAVE: {CHAVES}")
        return render_template("chaves_camp.html", chave= CHAVES)