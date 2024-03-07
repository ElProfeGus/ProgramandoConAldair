"""
Enunciado: Dada una lista de números, encuentra el número
más grande
"""

numeros = [1, 1000, 9000, 8]
numero_dos = [25, 50]

maximo = numeros[0] # Que poner el primer número
maximo_2 = numero_dos[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero
        
for numero_doss in numero_dos:
    if numero_doss > maximo_2:
        maximo_2 = numero_doss
    

print("El número más grande es: ", maximo)
print("El número más grande es: " , numero_doss)

# Alex 
# Que haye el maximo numero de 100 arreglos = alex para eso existen los metodos


