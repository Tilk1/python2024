print("ingrese una lista de numeros")

#lista_numeros = input().split()
lista_numeros = [11,20,33,-22,40]

for numero in lista_numeros:
    if numero < 0:
        print("numero negativo encontrado")
        break
    print(numero)

#otra forma de hacerlo

for i in range(0,len(lista_numeros)):
    if lista_numeros[i] < 0:
        print("numero negativo encontrado")
        break
    print(lista_numeros[i])

