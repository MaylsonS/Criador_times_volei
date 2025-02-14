import random
DUPLA = []
TRIO = []
SEIS = []


for x in range(10):
    if DUPLA and len(DUPLA[-1]) < 2:
        DUPLA[-1].append(x)
    else:
        DUPLA.append([x])

print(DUPLA)
print(len(DUPLA))
numeros_sort = []

a = random.randint(1,len(DUPLA))

for x in range(1,a ):
    if x in numeros_sort:
        print(f"Numero já sortedo: {x}")
        
        while x in numeros_sort:
            print(f"Novo numero: {random.randint(1, len(DUPLA))}")
    else:
        numeros_sort.append(x)
        print(f"Dupla exlcuida{DUPLA.pop(x)}")




print(f"Random: {a}")
