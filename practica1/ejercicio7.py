def convertir_a_str(lista_numeros: list[int]) -> str:
    resultado = "-".join(str(numero) for numero in lista_numeros if numero % 3 != 0)
    return resultado


entrada_usuario = input("ingrese numeros separados por coma: ")
numeros = list(map(int, entrada_usuario.split(",")))

resultado = convertir_a_str(numeros)
print("La cadena resultante es:", resultado)
