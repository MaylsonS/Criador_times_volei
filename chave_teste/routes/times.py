from flask import Blueprint, render_template,  request
from database.grupos import DUPLA, TRIO, SEIS

times_routes = Blueprint("times_routes", __name__)

@times_routes.route("/", methods=["POST","GET"])
def times():
    erro = request.args.get("erro", None)
    sucesso = request.args.get("sucesso", None)

    if len(DUPLA) > 1:
        print(f"DUPLA aaa {DUPLA}")
        return render_template("times.html", times=DUPLA ,erro=erro,sucesso=sucesso)
    elif len(TRIO) > 1:
        print(f"TRIO: {TRIO}")
        return render_template("times.html", times=TRIO, erro=erro,sucesso=sucesso)
    else:
        print(f"SEIS {SEIS}")
        return render_template("times.html", times= SEIS, erro=erro,sucesso=sucesso)


@times_routes.route("/dupla", methods=["POST","GET"])
def dupla():
    if request.method == "GET":
        return ("AAAAAAAAAAAAA")

    nome = request.form.get("nome")

    jogador = {"nome": nome}

    if DUPLA and len(DUPLA[-1]) < 2:
        DUPLA[-1].append(jogador)
    else:
        DUPLA.append([jogador])  

    # print(f"dupla: {DUPLA}")

    exibir_nome= (f"{nome[0]['nome']} & {nome[1]['nome']}" if len(nome) == 2 else f"{nome[0]['nome']}" for nome  in DUPLA)

    return render_template("formacao.html", nomes=exibir_nome)


@times_routes.route("/seis", methods=["POST"])
def seis():
    nome = request.form.get("nome")
    jogador = {"nome": nome}

    if SEIS and len(SEIS[-1]) < 6:
        SEIS[-1].append(jogador)
    else:
        SEIS.append([jogador])  

    # print(f"SEIS: {SEIS}")
    
    nomes_a_exibir= (f"{nome[0]['nome']} | {nome[1]['nome']} | {nome[2]['nome']} | {nome[3]['nome']} | {nome[4]['nome']} & {nome[5]['nome']}" if len(nome) == 6 else f"{nome[0]['nome']}" for nome in SEIS)

    return render_template("formacao.html", nomes=nomes_a_exibir)


@times_routes.route("/trio", methods=["POST"])
def trio():
    nome = request.form.get("nome")
    jogador = {"nome": nome}

    if TRIO and len(TRIO[-1]) < 3:
        TRIO[-1].append(jogador)
    else:
        TRIO.append([jogador]) 
    
    exibir_nome= (f"{nome[0]['nome']} & {nome[1]['nome']} & {nome[2]['nome']}" if len(nome) == 3 else f"{nome[0]}" for nome  in TRIO)

    return render_template("formacao.html", nome=exibir_nome)



    
# Gerenciar os times
