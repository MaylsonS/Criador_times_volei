def verificar_final(lista):
    return len(lista) == 1 and len(lista[0]) == 1

lista =  [[{'nome': 'ma ylson'}, {'nome': 'caio'}]]

if len(lista) == 1:
    print("Vencedor" ,lista[0][1])
print(len(lista))
    


# for partida in lista:
#     for jogador in partida:
#         print(f"{jogador[0]['nome']} & {jogador[1]['nome']}")
#         print("x")