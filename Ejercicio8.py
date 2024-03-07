"""
Enunciado: Dada una cadena de texto, cuenta cuantas veces
aparece la letra 'a'
"""
texto = "Aldair  y Gustavo van a ser buenos programadores de IA"

contador_a = 0 # Acumulador

for caracter in texto:
    if caracter == 'a' or caracter == 'A':
        contador_a += 1

print("La letra 'a' aparece", contador_a, "veces.")
    

