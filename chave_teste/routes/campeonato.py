from flask import Blueprint, render_template, request, redirect, url_for, session
from database.grupos import DUPLA, TRIO, SEIS, CHAVES, SEMI_FINAL
from routes.utils import adicionar_jogador, exibir_nomes , verificar_times, verificar_final, verificar_times_impar
import random

campeonato_route = Blueprint("campeonato_route", __name__)

@campeonato_route.route("/", methods=["GET", "POST"])
def home():
    session.pop("conferir", None)
    session.pop("grupo_origem", None)
    nomes = SEIS if SEIS else TRIO if TRIO else DUPLA
    return render_template("campeonato.html", time= nomes)

@campeonato_route.route("/verificar", methods=["POST"])
def verificar():
    SEMI_FINAL.clear()
    erro = request.args.get("erro", None)
    sucesso = request.args.get("sucesso", None)

    if verificar_times(DUPLA, 2):
        return render_template("campeonato.html", nomes=exibir_nomes(DUPLA, 2), erro="Há um time incompleto!")

    if  verificar_times_impar(DUPLA):
        return render_template("campeonato.html", nomes=exibir_nomes(DUPLA, 3), erro_modal="MODALL!")
    
    if verificar_times(TRIO, 3):
        return render_template("campeonato.html", nomes=exibir_nomes(TRIO, 3), erro="Há um time incompleto!")
    
    if  verificar_times_impar(TRIO):
        return render_template("campeonato.html", nomes=exibir_nomes(TRIO, 3), erro_modal="MODALL!")
    
    if verificar_times(SEIS, 6):
        return render_template("campeonato.html", nomes=exibir_nomes(SEIS, 6), erro="Há um time incompleto!")
    
    if  verificar_times_impar(SEIS):
        return render_template("campeonato.html", nomes=exibir_nomes(SEIS, 3), erro_modal="MODALL!")
    
    
    session["lista_de_time"] = DUPLA if DUPLA else TRIO if TRIO else SEIS
    session["limite"] = 2 if DUPLA else 3 if TRIO else 6

    return redirect(url_for("campeonato_route.formar_chaves"))

@campeonato_route.route("/confirmar_verificacao", methods=["POST"])
def confirmar_verificacao():
    session["lista_de_time"] = DUPLA if DUPLA else TRIO if TRIO else SEIS
    session["limite"] = 2 if DUPLA else 3 if TRIO else 6
    return redirect(url_for("campeonato_route.formar_chaves"))

@campeonato_route.route("/limpar_times", methods=["POST"])
def limpar_times():
    apagar_times = DUPLA if DUPLA else TRIO if TRIO else SEIS
    apagar_times.clear()
    return render_template("campeonato.html", erro="Times Excluidos")
    

@campeonato_route.route("/dupla", methods=["POST"])
def dupla_campeonato():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(DUPLA, jogador, 2)
    
    if verificar_times(DUPLA, 2):
        return render_template("campeonato.html", nomes=exibir_nomes(DUPLA, 2),dupla=DUPLA, trio=TRIO, seis=SEIS)

    return render_template("campeonato.html", nomes=exibir_nomes(DUPLA, 2),dupla=DUPLA, trio=TRIO, seis=SEIS)


@campeonato_route.route("/trio", methods=["POST"])
def trio_campeonato():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(TRIO, jogador, 3)
    
    if verificar_times(TRIO, 3):
        return render_template("campeonato.html", nomes=exibir_nomes(TRIO, 3),dupla=DUPLA, trio=TRIO, seis=SEIS)

    return render_template("campeonato.html", nomes=exibir_nomes(TRIO, 3),dupla=DUPLA, trio=TRIO, seis=SEIS)

@campeonato_route.route("/seis", methods=["POST"])
def seis_campeonato():
    nome = request.form.get("nome")
    jogador = {"nome": nome}
    adicionar_jogador(SEIS, jogador, 6)

    if verificar_times(SEIS, 6):
        return render_template("campeonato.html", nomes=exibir_nomes(SEIS, 6),dupla=DUPLA, trio=TRIO, seis=SEIS)

    return render_template("campeonato.html", nomes=exibir_nomes(SEIS, 6),dupla=DUPLA, trio=TRIO, seis=SEIS)


@campeonato_route.route("/chaves")
def formar_chaves():
    lista_de_time = session.get("lista_de_time")
    limite = session.get("limite",2)
    erro = request.args.get("erro", None)
    sucesso = request.args.get("sucesso", None)

    if erro or sucesso:
        return render_template("chaves_camp.html", chave= CHAVES, erro=erro, sucesso=sucesso,semi_finais= SEMI_FINAL)
    
    if not lista_de_time:
        return render_template("campeonato.html", chave=[], erro="Nenhum time foi formado.",semi_finais= SEMI_FINAL)
    
    partida = []
    lista_embaralhada = lista_de_time.copy()
    
    random.shuffle(lista_embaralhada)
    print(f"COPIA: {lista_embaralhada}")

    for time in lista_embaralhada:
        if partida and len(partida[-1]) < limite:
            partida[-1].append(time)

        else:
            partida.append([time])
            
    CHAVES.clear()
    CHAVES.extend(partida) 

    print(f"CHAVE: {CHAVES}")
    return render_template("chaves_camp.html", chave = CHAVES, semi_finais= SEMI_FINAL)

@campeonato_route.route("/comecar_partida", methods=["POST"])
def comecar_partida():
    if "LIMITE" not in session or session["LIMITE"] == 0:
        return render_template("campeonato_partida.html", erro="É preciso Colocar um limite de pontos !!!", times=session.get("times_partida", []),limite=session.get("LIMITE", 0),pontos1=session["pontosA"], pontos2=session["pontosB"])
    
    print(f"LIMITE de PONTOS: {session['LIMITE']}")
    session["partida_iniciada"] = True
    return redirect(url_for("campeonato_route.partida", sucesso= "Partida iniciada"))

@campeonato_route.route("/reiniciar_partida", methods=["POST"])
def reiniciar_partida():
    if "LIMITE" not in session or session["LIMITE"] == 0:
        return render_template("campeonato_partida.html", erro="É preciso Colocar um limite de pontos !!!", times=session.get("times_partida", []), limite=session.get("LIMITE", 0),pontos1=session["pontosA"], pontos2=session["pontosB"])
    
    print(f"LIMITE de PONTOS: {session['LIMITE']}")
    session["pontosA"], session["pontosB"] = 0, 0
    session["partida_iniciada"] = False
    return redirect(url_for("campeonato_route.partida", erro= "Partida Reiniciada"))



@campeonato_route.route("/criar_partida", methods=["POST","GET"])
def criar_partida():
    if request.method == "GET":
        return render_template("home.html")
    
    session["pontosB"], session["pontosA"] = 0, 0
    session.pop("times_partida",  None)
    session.pop("LIMITE", None) 
    session["partida_iniciada"] = False
   
    session["partida"] = []
    session["times_para_remocao"] = []
    lista_times = request.form.getlist("selecione_os_times")

    if len(lista_times) != 1:
        print(f"CHAVE: {CHAVES}")
        print(f"SEMI_FINAL: {SEMI_FINAL}")
        if len(CHAVES) == 0 and len(SEMI_FINAL) == 1 and len(SEMI_FINAL[0]) == 1:
            return render_template("campeonato.html", chave=CHAVES, semi_finais=SEMI_FINAL)

        return redirect(url_for("campeonato_route.formar_chaves", erro="Voce precisa escolher uma partida!!"))
    
    else:
        #Indice dos times
        lista_times = [int(time) for time in lista_times]
        
        if CHAVES and any(CHAVES):
            
            grupo = CHAVES

        elif SEMI_FINAL and any(SEMI_FINAL):
            if verificar_final(SEMI_FINAL):
                vencedor = SEMI_FINAL[0][0]
                return render_template("winner_campeonato.html", vencedor=vencedor)
            grupo = SEMI_FINAL
        else:
            return redirect(url_for("campeonato_route.formar_chaves", erro="Grupos vazios"))

    
        session["times_partida"] = [grupo[int(indici)] for indici in lista_times]
        print(f"times_partida: {session['times_partida']}")
        
        limite = session.get("limite", 2)
        partida_temporaria =[]
        for partida in session["times_partida"]:
            for time in partida:
                jogadores = [j["nome"] for j in time]
                partida_temporaria.append(jogadores)

        session["partida"] = ( [partida_temporaria[i:i+2] for i in range (0, len(partida_temporaria), 2 )] )

        session["times_para_remocao"] = grupo[int(lista_times[0])]
        print(f"Times para remover {session['times_para_remocao']}")


        session["grupo_origem"] = "CHAVES" if grupo == CHAVES else "SEMI_FINAL"

        print(grupo)
        print(f"conferir os time removido: {session['times_para_remocao']}")
        print("Partida",session["partida"])
        return render_template("campeonato_partida.html", times = session["times_partida"],limite=session.get("LIMITE", 0))
    
@campeonato_route.route("/partida", methods=["POST", "GET"])
def partida():
    erro = request.args.get("erro", None)
    sucesso = request.args.get("sucesso", None)

    times= SEIS if SEIS else TRIO if TRIO else DUPLA

    return render_template("campeonato_partida.html", times=session.get("times_partida", []) ,erro=erro,sucesso=sucesso, limite=session.get("LIMITE", 0),pontos1=session["pontosA"], pontos2=session["pontosB"])

@campeonato_route.route("/pontos", methods=["POST"])
def pontos():
    session["time_vencedor"] = []
    if "pontosA" not in session:
        session["pontosA"] = 0
    if "pontosB" not in session:
        session["pontosB"] = 0

    acao = request.form.get("action")

    # 1. Definir o limite de pontos
    if acao == "limtie_pontos":
        try:
            limite = int(request.form.get("ponto_limite", 0))
        except ValueError:
            limite = 0

        if limite <= 0:
            return render_template("campeonato_partida.html", erro="Valor inválido para limite de pontos!", times=session.get("times_partida", []), limite=0)

        session["LIMITE"] = limite
        return render_template("campeonato_partida.html", pontos1=session["pontosA"], pontos2=session["pontosB"], limite=limite, times=session.get("times_partida", []))

    # 2. Verificações obrigatórias
    if "LIMITE" not in session or session["LIMITE"] == 0:
        return render_template("campeonato_partida.html", erro="É preciso Colocar um limite de pontos !!!", times=session.get("times_partida", []), limite=0)

    if not session.get("partida_iniciada"):
        return render_template("campeonato_partida.html", erro="É preciso COMEÇAR a partida primeiro!", times=session.get("times_partida", []), limite=session["LIMITE"], pontos1=session["pontosA"], pontos2=session["pontosB"])

    # 3. Atualizar pontos
    if acao == "atualizar_pontos":
        valorA = int(request.form.get("btn_valorA", 0))
        session["pontosA"] = max(0, session["pontosA"] + valorA)

        valorB = int(request.form.get("btn_valorB", 0))
        session["pontosB"] = max(0, session["pontosB"] + valorB)

        # Verifica se algum time venceu
        if session["pontosA"] == session["LIMITE"]:
            for grupo in session["times_partida"]:
                session["time_vencedor"].extend(grupo[0])
            adicionar_jogador(SEMI_FINAL, session["time_vencedor"], 2)
            return render_template("winner_campeonato.html", vencedor=session["time_vencedor"], pontos=session["pontosA"], times=session["times_partida"], campeonato_encerrado=True, semi_finais=SEMI_FINAL, chave=CHAVES)

        elif session["pontosB"] == session["LIMITE"]:
            for grupo in session["times_partida"]:
                session["time_vencedor"].extend(grupo[1])
            adicionar_jogador(SEMI_FINAL, session["time_vencedor"], 2)
            return render_template("winner_campeonato.html", vencedor=session["time_vencedor"], pontos=session["pontosB"], times=session["times_partida"], campeonato_encerrado=True, semi_finais=SEMI_FINAL, chave=CHAVES)

        return render_template("campeonato_partida.html", pontos1=session["pontosA"], pontos2=session["pontosB"], limite=session["LIMITE"], times=session["times_partida"])

    # 4. Ação desconhecida
    return render_template("campeonato_partida.html", erro="Ação desconhecida!", pontos1=session["pontosA"], pontos2=session["pontosB"], limite=session.get("LIMITE", 0), times=session.get("times_partida", []))
    
@campeonato_route.route("/proxima_partida", methods = ["POST"])
def proxima_partida():
    if "grupo_origem" in session and "times_para_remocao" in session:
        if session["grupo_origem"] == "CHAVES":
            if session["times_para_remocao"] in CHAVES:
                CHAVES.remove(session["times_para_remocao"])
        elif session["grupo_origem"] == "SEMI_FINAL":
            if session["times_para_remocao"] in SEMI_FINAL:
                SEMI_FINAL.remove(session["times_para_remocao"])

    session.pop("conferir", None)
    session.pop("grupo_origem", None)

    
    if len(CHAVES) == 0 and len(SEMI_FINAL) == 1:
        return render_template("winner_tudo.html", chave=CHAVES, semi_finais=SEMI_FINAL)

    return render_template("chaves_camp.html", chave=CHAVES, semi_finais=SEMI_FINAL)
