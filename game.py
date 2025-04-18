'''
game.py — Space Exploration Game Module

The game module runs the space exploration game.

It coordinates gameplay by integrating the map functionality from space_map.py
and the Ship class from ship.py. This module initialises the space exploration
map and ship, and runs the game where players issue commands to explore the 
map, interact with entities, and aim to reach the destination.
'''

# import your 2 files here!
from ship import Ship
from space_map import create_map, display_map, populate_map

# define map size
def get_map_size() -> int:
    while True:
        # check input value here
        try:
            map_size = int(input('Enter size of map (n >= 2): '))
            if map_size < 2:
                print('Error: n too low')
                continue
            return map_size
        except ValueError:
            print('Error: map_size must always be an integer')    

# create a space map
def set_navigation_system() -> list[list[str]]:
    size = get_map_size()
    grid = create_map(size)
    print(f'{size} x {size} map initialised.\n')
    populate_map(grid)
    return grid

# create a Ship
def set_ship_system() -> Ship:
    # check ship_name
    while True:
        ship_name = input('Enter ship name: ')
        if not ship_name:
            print('Error: empty ship name')
            continue
        break
    # check the value of ship_fuel input
    while True:
        try:
            ship_fuel = int(input('Enter fuel (1-99): '))
            if ship_fuel < 1:
                print('Error: fuel too low')
                continue
            elif ship_fuel > 99:
                print('Error: fuel too high')
                continue   
        except ValueError:
            print('Error: fuel must always be an integer')
        break
    # ship object
    ship = Ship(ship_name, ship_fuel)
    return ship

# check game-ending conditions
def check_game_ending_conditions(ship: Ship, grid: list[list[str]]) -> bool:
    x, y = ship.get_coordinates()
    # win
    if ship.land_at_destination():
        print('Odyssey has reached: Sector 9-Delta')
        grid[y][x] = 'W'
        display_map(grid)
        print('\n>>> MISSION COMPLETED')
        return True
    # lose except command'q'
    if ship.is_out_of_fuel():
        print(f'{ship.name} is out of fuel.')
        grid[y][x] = 'L'
        display_map(grid)
        print('\n>>> MISSION FAILED')
        return True
    if ship.is_out_of_health():
        print(f'{ship.name} has fallen.')
        grid[y][x] = 'L'
        display_map(grid)
        print('\n>>> MISSION FAILED')
        return True
    return False

# interaction
def process_command(command: str, ship: Ship, grid: list[list[str]], directions: dict) -> bool:
    # check command
    available_commands = ['map', 'status', 'n', 'e', 's', 'w', 'q']
    if command == 'map':
        display_map(grid)
        return True
    elif command == 'status':
        print(ship)
        return True
    elif command == 'q':
        print(f'{ship.name} has self-destructed.')
        x, y = ship.get_coordinates()
        grid[y][x] = 'L'
        display_map(grid)
        print('\n>>> MISSION FAILED')
        return False
    # get coordinates
    current_x, current_y = ship.get_coordinates()
    # movement
    directions = {'n': (0, -1), 's': (0, 1), 'e': (1, 0), 'w': (-1, 0)}
    delta_x, delta_y = directions[command]
    # check new coordinates
    new_x, new_y = current_x + delta_x, current_y + delta_y
    if not (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid)):
        print('Error: out of bounds')
        return True
    # check symbol at new coordinate
    symbol = grid[new_y][new_x]
    # interaction between ship and symbol
    moved = ship.interact(symbol, new_x, new_y) 
    if not moved:
        return True
    # update map
    grid[current_y][current_x] = ' ' 
    ship.set_coordinates(new_x, new_y)
    grid[new_y][new_x] = '@'
    if check_game_ending_conditions(ship, grid):
        return False
    return True


def main():
    '''
    Runs the entire program from start to end. 
    
    All program logic must be executed within the main() function. We have
    provided some starting implementation and comments to help you out.
    '''
    # start 
    print('>>> STARTING ROUTE: Kepler-452b -> Sector 9-Delta')

    # 1. Configuring navigation systems
    # - Ask for size of map
    # - Then use this size to create a map reusing functions from the space_map 
    #   module!
    # ... 
    print('\n>> CONFIGURING NAVIGATIONAL SYSTEMS')
    grid = set_navigation_system()
    print('>> NAVIGATIONAL SYSTEMS READY')
    # 2. Configuring ship systems
    # - Ask for name and fuel of ship
    # - Then using the name and fuel, create a Ship instance reusing the Ship
    #   class from the ship module!
    # ...
    print('\n>> CONFIGURING SHIP SYSTEMS')
    ship = set_ship_system()
    print(ship)
    print('>> SHIP SYSTEMS READY')
    print("\n>>> EXECUTING LIFTOFF: EXITING Kepler-452b's ORBIT")

    # 3. Game Loop
    # - At this stage, you should have both a map and ship initialised
    # - Take in commands from user to navigate map and progress the game
    # - You'll need to make frequent use of both your map and ship!
    #    - Your ship stores (x, y): This is [y][x] on the map!
    #    - When you find where the ship wants to move, call its interact()
    #      method!
    # - After each interaction, you'll need to check win/loss conditions
    #    - Check if ship reached destination (remember ship stores this!)
    #    - Check if ship has no health
    #    - Check if ship has no fuel left
    # ...
    print('\n>>> AWAITING COMMANDS\n')
    available_commands = ['map', 'status', 'n', 'e', 's', 'w', 'q']
    directions = {'n': (0, -1), 's': (0, 1), 'e': (1, 0), 'w': (-1, 0)}
    # game active
    game_active = True
    while game_active:
        # firstly, check game-ending conditions
        if check_game_ending_conditions(ship, grid):
            break
        # secondly, check user command
        try:
            command = input('Enter (n,e,s,w | map | status): ').lower().strip()
            if not command:
                continue
            elif command not in available_commands:
                print('Error: unrecognised command')
                continue
            elif not process_command(command, ship, grid, directions):
                break
        except EOFError:
            break


# don't modify this!
if __name__ == '__main__':
    main()