# Dictionaries, Oh Lovely Dictionaries
#Spain Version
comunidades = ["Andalucia","Murcia", "Extremadura",
                    "Madrid", "Castilla-la-Mancha", "Comunidad Valenciana",
                    "Islas Baleares", "Islas Canarias", "Cataluña", "Aragon",
                    "Pais Vasco", "Asturias","Cantabria", "Castilla y Leon"]
abreviaciones_list =["AND", "ARA", "AST", "CANT", "CYL", "CLM","CAT", "CVA", "EXT", "GAL", "IB", "IC", "RIO", "MAD", "MUR", "NAV", "PV"]
print("-" * 10)

for i in comunidades:
    print(i)

print("-" * 10)

print("Has olvidado algunas comunidades...")
comunidades.append("Galicia")
comunidades.append("Navarra")
comunidades.append("La Rioja")

print("Uy, no están en orden, lo corrijo! ")
comunidades.sort()
print("-" * 10)
n = 1
for i in comunidades:
    print(f"{n} - {i}")
    n += 1
print("-" * 10)

# com_index = {}
# i = 1
# for comunidad in comunidades:
#     com_index[comunidad] = i
#     i += 1

com_index = {comunidad: i for i, comunidad in enumerate(comunidades,1)}
print(com_index)

com_abreviatura = dict(zip(comunidades, abreviaciones_list))

print(com_abreviatura)
print("-" * 10)

for i, j in list(com_abreviatura.items()):
    print(f"{i} - {j}")