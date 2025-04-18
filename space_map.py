'''
space_map.py — Space Exploration Map Module

This module provides the core functionality for creating and managing a
space exploration map in the space exploration game. 

It allows users to initialise a map, display it and populate it with key 
entities including the ship, destination, hazards and waypoints.
'''


def create_map(n: int) -> list[list[str]]:
    '''
    Initialises and returns an n x n grid representing the game map.

    Parameters:
        n (int): The size of the grid (number of rows and columns).

    Returns:
        list[list[str]]: A 2D list representing the game map.
    '''
    if not isinstance(n, int) or n <= 0:
        return 'Invalid input'
    list_map = [[' '] * n for i in range(n)]
    return list_map
# from pprint import pprint
# pprint(create_map(4))


def display_map(grid: list[list[str]]):
    '''
    Prints the current state of the grid in a readable map format.

    Parameters:
        grid (list[list[str]]): The 2D list representing the game map.
    '''
    if len(grid) < 1:
        return 'Invalid input'
    for parts in grid:
        print('|' + '|'.join(f' {char} ' for char in parts) + '|')
#   row = ['|' + '|'.join(f' {char} ' for char in parts) + '|' for parts in grid]
#   return '\n'.join(row)
#print(display_map([['@', ' ', 'M', ' '], [' ', 'E', ' ', ' '], [' ', ' ', 'X', ' '], ['.', ' ', ' ', 'R']]))


def populate_map(grid: list[list[str]]):
    '''
    Populates the grid with key entities including the ship, destination,
    hazards, and waypoints.

    Note: Coordinate (x, y) cooresponds to grid[y][x].

    Parameters:
        grid (list[list[str]]): The 2D list representing the game map.
    '''
    if not grid or not isinstance(grid, list):
        return 'Invalid input'
    valid_entities = {'.': 'Asteroid', 'E': 'Enemy', 'M': 'Mineral', 'R': 'Repair Station'}
    height = len(grid)
    width = len(grid[0])

    #1.Ship
    grid[0][0] = '@'
    print('Placing: Ship')
    print('Ship placed: (0, 0)')
    display_map(grid)

    #2.Destination
    print()
    print('Placing: Destination')
    while True:
        coordinate = input('Enter (x y): ').strip().split()
        if len(coordinate) != 2:
            print('Error: expected <x> <y>')
            continue
        x, y = map(int, coordinate)
        if not (0 <= x < width and 0 <= y < height):
            print('Error: out of bounds')
            continue
        if grid[y][x] != ' ':
            print(f"Error: ({x}, {y}) occupied by '{grid[y][x]}'")
            continue
        grid[y][x] = 'X'
        print(f'Destination placed: ({x}, {y})')
        display_map(grid)
        break
    
    #3.Hazards and Waypoints
    print()
    print('Placing: Hazards and Waypoints')
    while True:
        user_input = input('Enter (symbol x y | display | done): ').strip()
        #Conditional Sequence matters
        if user_input.lower() == 'display':
            display_map(grid)
            continue
        elif user_input.lower() == 'done':
            display_map(grid)
            break
        parts = user_input.split()
        if len(parts) != 3:
            print('Error: expected <symbol> <x> <y>')
            continue
        symbol, x, y = parts
        x, y = map(int, parts[1:3])
        if symbol not in valid_entities:
            print(f"Error: '{symbol}' not recognised")
            continue
        if not (0 <= x < width and 0 <= y < height):
            print('Error: out of bounds')
            continue
        if grid[y][x] != ' ':
            print(f"Error: ({x}, {y}) occupied by '{grid[y][x]}'")
            continue
        grid[y][x] = symbol
        print(f'{valid_entities[symbol]} placed: ({x}, {y})')


if __name__ == '__main__':
    # you can put any test code here!
    # this only runs when its the main program ran i.e. python3 space_map.py

    # initialization
    width, height = 5, 5
    game_map = [[' ' for _ in range(width)] for _ in range(height)]

    # set map
    populate_map(game_map)

    # display map
    print("=== map ===")
    display_map(game_map)