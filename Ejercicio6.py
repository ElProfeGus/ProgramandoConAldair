"""
Enunciado: Itera sobre una lista de paises e imprime solo aquellos que 
comienzan con la letra "P"
"""

paises = ["Polonia", "Afganistan", "Peru", "Venezuela", "Huaycan"]

for pais in paises:
    if pais.startswith("P"):
        print(pais)