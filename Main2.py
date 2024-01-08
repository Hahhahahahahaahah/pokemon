from prettytable import from_csv

with open("pokemon.csv") as pokedex:
    table = from_csv(pokedex)

print(table)
