lista_numeros = [16,20,21,33,40]

for numero in lista_numeros:
    if numero % 2 == 0:
        print(numero)

print("otra forma de hacerlo")

for i in range(0,len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        print(lista_numeros[i])

print("con el continue")

for numero in lista_numeros:
    if numero % 2 != 0:
        continue
    print(numero)