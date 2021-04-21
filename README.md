# Battleship Game

The idea is to build a square matrix containing zeroes and we will place a battleship randomly on the grid.

The user has a few chances to drop a bomb on the location of the ship by guessing. After a few incorrect guesses, the game will be over.


## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up


## Run

- Download the project, open your terminal window on the folder with "battleship.py" and type:

```
python battleship.py
```

Enjoy!


## Files

### Battleship.py

This is the main file, the file you want to run on your terminal window. We create the game and keep updating till you either win or lose.

### Game_sets.py

This is a file where I put the logic of the game, there's only few functions:

```python
# To display the table
def display_table(table: list):

# Create ships on random locations
def create_ship(size: int):

# Make sure ships aren't on same positions
def validate_ships(ships: list):

# Update table
def update_table(table: list, character: str, height: int, row: int):
```