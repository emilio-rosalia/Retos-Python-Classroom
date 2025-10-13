mis_pokemon = set()

condicion = True
while condicion:
    pokemon = input("Ingrese el nombre de un pokemon: ")
    if pokemon.lower() == 'fin':
        condicion = False
    else:
        mis_pokemon.add(pokemon)

print("Tus pokemon capturados son: ")
for pokemon in mis_pokemon:
    print(pokemon, end=' ')