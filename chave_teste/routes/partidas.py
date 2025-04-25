from flask import Blueprint, render_template, request, redirect, url_for, session
from database.grupos import DUPLA, TRIO, SEIS

# from routes.times import times_routes

partidas_route= Blueprint("partidas_route", __name__)


@partidas_route.route("/criar_partida", methods=["POST","GET"])
def criar_partida():
    if request.method == "GET":
        return "CRIAR PARTIDA GET"
    session["pontosB"], session["pontosA"],session["limite"] = 0, 0, 0
    session.pop("times_partida",  None)
    lista_times = request.form.getlist("selecione_os_times")

    if len(lista_times) != 2:
        return redirect(url_for("times_routes.times", erro="Voce precisa escolher dois times!!"))
    else:
        lista_times = [ int(indice) for indice in lista_times]
        
        print(f"indicis lista: {lista_times}")

        grupo =  DUPLA if DUPLA else TRIO if TRIO else SEIS
        
        if not grupo:
            return redirect(url_for("times", erro="Grupos vazio"))

        session["times_partida"] = [grupo[indici] for indici in lista_times]
        print(f'times_partida: {session["times_partida"]}')

        print(session["times_partida"])
        return render_template("partida.html", sucesso="passou", times = session["times_partida"])


@partidas_route.route("/partida")
def partida():
    erro = request.args.get("erro", None)
    sucesso = request.args.get("sucesso", None)

    times= SEIS if SEIS else TRIO if TRIO else DUPLA

    return render_template("partida.html", times=times ,erro=erro,sucesso=sucesso)


############## Ajustar Para funcinar no amistoso ####################################

@partidas_route.route("/comecar_partida", methods=["POST"])
def comecar_partida():
    if "LIMITE" not in session or session["LIMITE"] == 0:
        return render_template("partidas_partida.html", erro="É preciso Colocar um limite de pontos !!!", times=session.get("times_partida", []),limite=session.get("LIMITE", 0),pontos1=session["pontosA"], pontos2=session["pontosB"])
    
    print(f"LIMITE de PONTOS: {session['LIMITE']}")
    session["partida_iniciada"] = True
    return redirect(url_for("partidas_route.partida"))

@partidas_route.route("/reiniciar_partida", methods=["POST"])
def reiniciar_partida():
    if "LIMITE" not in session or session["LIMITE"] == 0:
        return render_template("partidas_partida.html", erro="É preciso Colocar um limite de pontos !!!", times=session.get("times_partida", []), limite=session.get("LIMITE", 0),pontos1=session["pontosA"], pontos2=session["pontosB"])
    
    print(f"LIMITE de PONTOS: {session['LIMITE']}")
    session["pontosA"], session["pontosB"] = 0, 0
    session["partida_iniciada"] = False
    return redirect(url_for("partidas_route.partida"))

##########################################################################################

@partidas_route.route("/pontos", methods=["POST"])
def pontos():
    if "pontosA" not in session:
        session["pontosA"] = 0
    if "pontosB" not in session:
        session["pontosB"] = 0
    if "LIMITE" not in session:
        session["LIMITE"] = 100

    acao = request.form.get("action")

    if acao == "limtie_pontos":
        limite = int(request.form.get("ponto_limite", 0))
        print(f"LIMITE: {limite}")
        session["LIMITE"] = limite
        return render_template("partida.html", pontos1=session["pontosA"], pontos2=session["pontosB"], limite=session["LIMITE"], times = session["times_partida"])

    elif acao == "atualizar_pontos":
        # Atualiza os pontos para o time A
        valorA = int(request.form.get("btn_valorA", 0))
        print(f"PontoA: {valorA}")
        session["pontosA"] += valorA
        session["pontosA"] = max(0, session["pontosA"])  # Impede valores negativos

        # Atualiza os pontos para o time B
        valorB = int(request.form.get("btn_valorB", 0))
        print(f"PontoB: {valorB}")
        session["pontosB"] += valorB
        session["pontosB"] = max(0, session["pontosB"])  # Impede valores negativos

        # Verifica se algum time alcançou o limite
        if session["pontosA"] == session["LIMITE"]:
            print(f'A ganhador {session["times_partida"][0]}')
            return render_template("winner.html", vencedor=session["times_partida"][0], pontos=session["pontosA"],times = session["times_partida"], time_vencedor = session["times_partida"][0][0])
        
        elif session["pontosB"] == session["LIMITE"]:
            print(f'B ganhador {session["times_partida"][1]}')
            return render_template("winner.html", vencedor = session["times_partida"][1], pontos=session["pontosB"],times = session["times_partida"], time_vencedor = session["times_partida"][0][1])

        return render_template("partida.html", pontos1=session["pontosA"], pontos2=session["pontosB"], limite=session["LIMITE"],times = session["times_partida"])

    else:
        return render_template("partida.html",  erro="Ação desconhecida", pontos1=session["pontosA"], pontos2=session["pontosB"], limite=session["LIMITE"], times = session["times_partida"])



# iniciar partidas

# Gerenciar pontos 

