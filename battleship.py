from string import ascii_uppercase

from funcs import *


alphabet = [letter for letter in ascii_uppercase if letter <= "J"]
table = [['.' for _ in range(10)] for _ in range(10)]
table.insert(0, alphabet)

display_table(table)
print('------------')

ships = [create_ship(2), create_ship(3), create_ship(4), create_ship(5)]

for counter, ship in enumerate(ships):
    print(f"Ship_{counter}: {ship}")

print('------------')
all_ships = validate_ships(ships)

for counter, ship in enumerate(all_ships):
    print(f"Ship_{counter}: {ship}")

print('------------')
