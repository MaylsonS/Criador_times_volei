def verificar_final(lista):
    return len(lista) == 1 and len(lista[0]) == 1

lista =  [[[{'nome': 'Renan'}, {'nome': 'Mikael'}]]]
if(verificar_final(lista)):
    vencedor = lista[0][0]
    print(vencedor)
    


# for partida in lista:
#     for jogador in partida:
#         print(f"{jogador[0]['nome']} & {jogador[1]['nome']}")
#         print("x")