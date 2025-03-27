import random
DUPLA = []
TRIO = []
SEIS = []

def formar_chaves(lista, limite):
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


for x in range(12):
    if DUPLA and len(DUPLA[-1]) < 2:
        DUPLA[-1].append(x)
    else:
        DUPLA.append([x])

print(DUPLA)
print(len(DUPLA))
CHAVES = []
partida = []



if len(DUPLA) % 2 != 0:
    confirm = input("Voce tem um time sobrando, quer continuar ?").lower()
    
    formar_chaves(DUPLA,2) if confirm == 's' else print("Chaves n formadas")
else:
    formar_chaves(DUPLA,2)

# for time in lista_embaralhada:
#     if partida and len(partida[-1]) < 2:
#       partida[-1].append(time)

#     else:
#         partida.append([time])

# print(f"Partidas: {partida}")
# print(len(partida))
# for x in range(0,len(partida)):
#     (CHAVES.append(partida[x]))

# print(f"CHAVE: {CHAVES}")

