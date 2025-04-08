def adicionar_jogador(grupo, jogador ,limite):
    if grupo and len(grupo[-1]) < limite:
        grupo[-1].append(jogador)
    else:
        grupo.append([jogador])
        
    print(grupo)
    
def exibir_nomes(grupo, limite):
    return (f'{nome[0]["nome"]} & {nome[1]["nome"]}' if len(nome) == limite else f'{nome[0]["nome"]}' for nome in grupo)

def verificar_times(times, limite):
    if not times:
        return False
    return len(times[-1]) < limite

def verificar_final(lista):
    return len(lista) == 1 and len(lista[0]) == 1
