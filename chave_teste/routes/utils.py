def adicionar_jogador(grupo, jogador ,limite):
    if grupo and len(grupo[-1]) < limite:
        grupo[-1].append(f"& {jogador}")
    else:
        grupo.append([jogador])
        
    print(grupo)
    
def exibir_nomes(grupo, limite):
    return (f"{nome[0]['nome']} & {nome[1][11:-1]}" if len(nome) == limite else f"{nome[0]['nome']}" for nome in grupo)

def verificar_times(times, limite):
    if not times:
        return False
    return len(times[-1]) < limite
