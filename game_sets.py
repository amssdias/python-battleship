import random


def display_table(table: list):
    '''
    Display a square matrix containing dots.
    '''

    # Go through height of table
    for counter, height in enumerate(table):
        if counter == 0:
            print("".rjust(3), end="")
        else:
            print(str(counter).rjust(2), end=" ")

        # Go thru row of table
        for row in height:
            print(row.rjust(2), end="")
        print()


def create_ship(size: int):
    """
    Function to build a ship, parameters are the size of the ship (lenght).
    """

    height, row = [random.randint(1, 10), random.randint(0, 10)]
    direction = random.randint(1, 2)
    ship = set()

    # Horizontal
    if direction == 1:
        if row <= 10 - size:
            for i in range(size):
                ship.add((height, row + i))
            return ship
        else:
            for i in range(size):
                ship.add((height, row - i))
            return ship

    # Vertical
    else:
        if height <= 10 - size:
            for i in range(size):
                ship.add((height + i, row))
            return ship
        else:
            for i in range(size):
                ship.add((height - i, row))
            return ship


def validate_ships(ships: list):
    """
    Function to make sure there are no ships on the same coordinates. If there are it will create new ship with create_ship function.
    It will return a new list with all the ships.
    """

    ships_validated = []

    # Loop through ships created
    for ship in ships:

        if len(ships_validated) == 0:
            ships_validated.append(ship)
        else:

            # Loop through ships checked
            for new_ship in ships_validated:

                # If there are ships in same coordinates, don't add to checked ships
                if ship.intersection(new_ship):

                    # Create new ship and add to the list of ships
                    new = create_ship(len(ship))
                    ships.append(new)
                    break

            # If no intersections, add to checked ships
            else:
                ships_validated.append(ship)

    return ships_validated


def update_table(table: list, character: str, height: int, row: int):
    """
    Update square matrix of battleship.
    """

    table[height][row] = character
    return table
