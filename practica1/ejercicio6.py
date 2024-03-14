lista_numeros = [-2,16,20,21,33,40]

lista_par= []
lista_impar = []

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print("lista de numeros pares: ",lista_par)
print("lista de numeros impares: ",lista_impar)

