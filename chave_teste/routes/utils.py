def adicionar_jogador(grupo, jogador ,limite):
    if grupo and len(grupo[-1]) < limite:
        grupo[-1].append(jogador)
    else:
        grupo.append([jogador])
        
    print(grupo)
    
def exibir_nomes(grupo, limite):
    return (" & ".join(j["nome"] for j in nome) for nome in grupo)

def verificar_times(times, limite):
    if not times:
        return False
    return len(times[-1]) < limite

def verificar_final(lista):
    return len(lista) == 1 and len(lista[0]) == 1
