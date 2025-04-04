lista = [[["time 1", "time 2"], ["time 3", "time 4"]]]

# Percorre os grupos dentro da lista
for grupo in lista:
    for time in grupo[0]:
        print(time)
    for time in grupo[1]:
        print(time)