from string import ascii_uppercase

from game_sets import *

# Create square matrix
alphabet = [letter for letter in ascii_uppercase if letter <= "J"]
table = [['.' for _ in range(10)] for _ in range(10)]
table.insert(0, alphabet)


new_ships = [create_ship(2), create_ship(3), create_ship(4), create_ship(5)]
ships = validate_ships(new_ships)

user_hits = 0
user_trys = set()

for ship in ships:
    user_hits += len(ship)

while True:

    display_table(table)

    user_guess = [char for char in input("Coordinates: ").upper()]

    try:
        if user_guess[1] == "0":
            user_guess[0] = 10
            user_guess[1] = ord(user_guess[2]) - 65
            user_guess.pop()
        else:
            user_guess[0] = int(user_guess[0])
            user_guess[1] = ord(user_guess[1]) - 65

        user_coordinates = {tuple(user_guess)}

        if user_trys.intersection(user_coordinates):
            print("Already tryed that coordinate, try other!")
            continue
        else:
            user_trys.add(tuple(user_guess))

        if len(user_guess) != 2:
            print("Write coordinates with no blank spaces ' ', and only two characters.")
            continue

        if user_guess[1] > 10 or user_guess[0] > 10 or isinstance(user_guess[1], str):
            print("Can't use those coordinates, try again...")
            continue

        for ship in ships:

            # If user hitted a ship update table
            if ship.intersection(user_coordinates):
                table = update_table(table, "X", *user_guess)
                user_hits -= 1
                break
        else:
            table = update_table(table, "0", *user_guess)

        if len(user_trys) == 50:
            print("Sorry you lost, try again!")

        if user_hits == 0:
            display_table(table)
            print("Congratulations, YOU WON!!")
            break

    except ValueError:
        print(f"Height of {user_guess[0]} don't exist")
