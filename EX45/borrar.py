import random

palos = ["oros", "espadas", "copas", "bastos"]
cartas = []  # Inicializamos la lista de cartas
# i para num; j para palos,
for j in palos:
    i = 1
    while i <= 12:
        numero_y_palo = f"{i} {j}"
        cartas.append(numero_y_palo)
        i += 1
    print(j)
print(cartas)