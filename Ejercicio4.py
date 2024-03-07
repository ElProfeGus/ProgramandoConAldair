"""
Enunciado: Itera sobre una lista de números
e imprime la suma acumulada hasta el índice 
actual
"""

numeros = [1, 2, 3, 4, 5]

auxiliar = 0
suma_acumulada = 0 # Acumulador
for numero in numeros:
    anterior = suma_acumulada
    suma_acumulada += numero
    print(anterior, " + ", numero, " = ", suma_acumulada)


