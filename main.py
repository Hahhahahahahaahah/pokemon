from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon number", "Pokemon name", "Pokemon Type"]
table.add_rows(
    [
        [1,"Bulbasaur", "Grass/Poison"],
        [2,"Ivysaur", "Grass/Poison"],
        [3, "Venusaur","Grass/Poison"],
        [4, "Charmander", "Fire"],
        [5, "Charmelon", "Fire"]
    ]
)

print(table)