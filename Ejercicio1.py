'''
Suma de números pares e impares: Escribe una función que tome una lista
de números y devuelva la suma de los números pares y la suma de los números
impares por separado
'''
def suma_pares_impares(lista):
    suma_pares = 0
    suma_impares = 0
    for num in lista:
        if num % 2 == 0:
           suma_pares += num
    else: 
        suma_impares += num 
        return suma_pares, suma_impares
    
# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
suma_pares, suma_impares = suma_pares_impares(numeros)
print("suma de pares:", suma_pares)
print("suma impares:", suma_impares)