""" #Itera
Enunciado: Crea un bucle sobre una lista e imprime 
solo los números [pares]
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)