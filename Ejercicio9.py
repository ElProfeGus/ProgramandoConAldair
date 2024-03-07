"""
Enunciado: Dada una lista de nombres, imprime solo aquellos
nombres que tienen más de 8 letras
"""

nombres = ["Tavito", "Aldairsito", "Kiarita", "Dayanita"]

for nombre in nombres:
    if len(nombre) <= 8:
        print(nombre)

