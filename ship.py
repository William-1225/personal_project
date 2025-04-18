'''
ship.py — Ship Module

This module defines the Ship class used in the space exploration game.

The Ship class encapsulates all functionality related to the player's ship,
including the ship's current state (position, fuel, health, and minerals)
and methods to manage movement, resource consumption, interactions with map
entities and displaying status reports.
'''

class Ship:
    def __init__(self, name: str, fuel: int):
        '''
        Initialises a Ship instance with the given name and starting fuel.

        The ship will also begin with some extra attributes set to the 
        following default values:
            x (int): 0
            y (int): 0
            health (int): 3 (full health)
            minerals (int): 0
            destination_reached (bool): False
        '''
        self.name = name
        self.fuel = fuel
        self.x = 0
        self.y = 0
        self.health = 3 # full health
        self.minerals = 0
        self.destination_reached = False


    def consume_fuel(self):
        '''Decreases the ship's fuel by 1 unit, where it can't fall below 0.'''
        self.fuel = max(self.fuel - 1, 0)


    def is_out_of_fuel(self) -> bool:
        '''
        Returns True if the ship has no fuel remaining (reaches 0), False
        otherwise.
        '''
        return self.fuel == 0


    def damage_ship(self):
        '''Decreases the ship's health by 1, where it can't fall below 0.'''
        self.health = max(self.health - 1, 0)


    def repair_ship(self):
        '''Increases the ship's health by 1, up to a maximum of 3.'''
        self.health = min(self.health + 1, 3)


    def is_out_of_health(self) -> bool:
        '''
        Returns True if the ship has no health remaining (reaches 0), False
        otherwise.
        '''
        return self.health == 0


    def add_mineral(self):
        '''Increases the ship's minerals by 1. '''
        self.minerals += 1


    def use_mineral(self):
        '''Decreases the ship's minerals by 1, where it can't fall below 0.'''
        self.minerals = max(self.minerals - 1, 0)


    def land_at_destination(self):
        '''
        Marks that the ship has reached its destination by setting 
        destination_reached to True.
        '''
        self.destination_reached = True


    def get_coordinates(self):
        return (self.x, self.y)
    
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


    def interact(self, symbol: str, symbol_x: int, symbol_y: int) -> bool:
        '''
        Handles the ship's interaction with a map entity based on its symbol 
        and coordinates.

        The interaction varies depending on the type of entity. Each 
        interaction may affect the ship's state (e.g., coordinates, health, 
        minerals, etc).

        Parameters:
            symbol (str): The symbol representing the entity 
                    (' ', 'X', '.', 'E', 'M', 'R')
            symbol_x (int): The x-coordinate of the entity
            symbol_y (int): The y-coordinate of the entity
  
        Returns:
            bool: True if the ship moves to the entity's coordinates, 
                  False otherwise.
        '''
        # A ship cannot interact without fuel
        if self.fuel == 0:
            return False
        
        #1.symbol: ' '
        if symbol == ' ':
            self.consume_fuel()
            self.x, self.y = symbol_x, symbol_y
            return True
        
        #2.symbol: 'X'
        elif symbol == 'X':
            self.consume_fuel()
            self.destination_reached = True
            self.x, self.y = symbol_x, symbol_y
            print(f'{self.name} has reached: Sector 9-Delta')
            return True

        #3.symbol: '.'
        elif symbol == '.':
            print('Cannot move past an asteroid!')
            return False
        
        #4.symbol: 'E'
        elif symbol == 'E':
            self.consume_fuel()
            self.damage_ship()
            self.x, self.y = symbol_x, symbol_y
            if self.health == 0:
                print(f'{self.name} has fallen.')
            else:
                print(f'We won the fight! Health: {self.health}/3')
            return True

        #5.symbol: 'M'
        elif symbol == 'M':
            self.consume_fuel()
            self.add_mineral()
            self.x, self.y = symbol_x, symbol_y
            print(f'+1 mineral! Minerals: {self.minerals}')
            return True

        #6.symbol: 'R'
        elif symbol == 'R':
            if self.health == 3:
                print('Ship is already at full health!')
                return False
            elif self.health != 3 and self.minerals == 0:
                print('You need a mineral to activate this repair station.')
                return False
            else:
                self.x, self.y = symbol_x, symbol_y
                self.consume_fuel()
                self.use_mineral()
                self.repair_ship()
                print(f'Ship repaired! Health: {self.health}/3')
                return True
        
        #by defalut, return false
        return False


    def __str__(self) -> str:
        '''Returns a status report summarising the ship's current state.'''
        report = []
        report.append(f'Status Report - {self.name}')
        report.append('-' * 25)
        report.append(f"{'Coordinates':15}: ({self.x}, {self.y})")
        report.append(f"{'Fuel Level':15}: {self.fuel:02d} units")
        report.append(f"{'Health':15}: {self.health}")
        report.append(f"{'Minerals':15}: {self.minerals:02d}")
        report.append('-' * 25)
        return '\n'.join(report)

if __name__ == '__main__':
    # you can put any test code here!
    # this only runs when its the main program ran i.e. python3 ship.py

        # initialization
        ship = Ship('will', 10)
        print("initialization")
        print(ship)

        # try to move to ' '
        print("\n--- ' ' ---")
        ship.interact(' ', 1, 0)
        print(ship)

        # try to move to '.'
        print("\n--- '.' ---")
        ship.interact('.', 2, 0)
        print(ship)

        # try to move to 'E'
        print("\n--- 'E' ---")
        ship.interact('E', 1, 1)
        print(ship)

        # move to 'E' until out of health
        ship.interact('E', 1, 2)
        ship.interact('E', 1, 3)
        print(ship)

        # try to move to 'M'
        print("\n--- 'M' ---")
        ship.health = 2
        ship.interact('M', 2, 3)
        print(ship)

        # try to move to 'R'（minerals available）
        print("\n--- 'R' ---")
        ship.interact('R', 2, 4)
        print(ship)

        # try to move to 'X'
        print("\n--- 'X' ---")
        ship.interact('X', 3, 4)
        print(ship)

        # out of fuel
        print("\n--- out_of_fuel ---")
        ship.fuel = 0
        result = ship.interact(' ', 4, 4)
        print("successful movement ?", result)
        print(ship)