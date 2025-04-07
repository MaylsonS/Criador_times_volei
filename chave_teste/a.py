lista =  [[[{'nome': 'Renan'}, {'nome': 'Mikael'}], [{'nome': 'clodoldo tang'}, {'nome': 'ma ylson'}]], [[{'nome': 'Emilio'}, {'nome': 'Surita'}], [{'nome': 'Daniel'}, {'nome': 'Zukerman'}]], [[{'nome': 'fCessar'}, {'nome': 'Primeiro'}]]]
print(len(lista))
# print(lista)
for partida in lista:
    # print(f"Len Partida: {len(partida)}\n")
    # print(partida, end=" ")
    for jogador in partida:
        print(f"{jogador[0]['nome']} & {jogador[1]['nome']}")
        print("x")


    # for i,jogador in partida:
    #     print(i['nome'],"&",jogador['nome'])

# {% for fase in semi_finais %}
#   {% for partida in fase %}
#     {% if partida|length > 1 %}
#       {{ partida[0]['nome'] }} & {{ partida[1]['nome'] }}