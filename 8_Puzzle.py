from SearchAlgorithms import BuscaGananciosa, AEstrela, pretty_print_table
from Graph import State

from copy import deepcopy
from time import time

GOAL_TABLE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

POSSIBILITIES = [
            (1 , 0),
    (0, -1),       (0 , 1),
            (-1, 0)
]

TILE_GOALCOORDS_MAP = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    8: (1, 0), 0: (1, 1), 4: (1, 2),
    7: (2, 0), 6: (2, 1), 5: (2, 2)
}

class Puzzle(State):

    def __init__(self, table, exclude_move, op, hs=['manhattan', 'permInversion']):
        self.table = table
        self.exclude_move = exclude_move
        self.hs = hs
        self.operator = op

    def tile_coords(self, tile_value = 0):
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if(self.table[i][j] == tile_value):
                    return i, j
    
    def sucessors(self):
        sucessors = []

        zero_row, zero_col = self.tile_coords()

        for diff_row, diff_col in POSSIBILITIES:

            if((diff_row, diff_col) != self.exclude_move):

                copy_table = deepcopy(self.table)

                if(0 <= zero_row + diff_row <= 2 and 0 <= zero_col + diff_col <= 2):
                    op = f'{copy_table[zero_row][zero_col]} <--> {copy_table[zero_row + diff_row][zero_col + diff_col]}'
                    copy_table[zero_row][zero_col], copy_table[zero_row + diff_row][zero_col + diff_col] = copy_table[zero_row + diff_row][zero_col + diff_col], copy_table[zero_row][zero_col]

                    sucessors.append(Puzzle(copy_table, (-diff_row, -diff_col), op, self.hs))

        return sucessors
    
    def is_goal(self):
        return self.table == GOAL_TABLE
    
    def description(self):
        return "https://en.wikipedia.org/wiki/15_puzzle so que 8-Puzzle"
    
    def cost(self):
        return 1

    def flatten_table(self):
        flatten = list()
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                flatten.append(self.table[i][j])

        return flatten

    def h(self):
        h = 0

        if('manhattan' in self.hs):
            for tile in range(1, 9):
                tile_row, tile_col = self.tile_coords(tile)
                goal_row, goal_col = TILE_GOALCOORDS_MAP[tile]
                h += (abs(goal_row - tile_row) + abs(goal_col - tile_col))

        if('permInversion' in self.hs):
            flatten = self.flatten_table()
            for i in range(len(flatten)):
                for j in range(i+1, len(flatten)):
                    if(flatten[j] < flatten[i]):
                        h += 1

        if('match' in self.hs):
            for tile in range(1, 9):
                tile_row, tile_col = self.tile_coords(tile)
                goal_row, goal_col = TILE_GOALCOORDS_MAP[tile]
                if(goal_row != tile_row or goal_col != tile_col):
                    h += 1

        return h

    def print(self):
        return str(self.operator)
    
    def env(self):
        return f'{self.operator} ---> {self.table}'


def main():

    INITIAL_STATE = [
        [1, 3, 4],
        [8, 0, 5],
        [7, 2, 6]
    ]

    print('Estado inicial - Busca Gananciosa')
    pretty_print_table(INITIAL_STATE)

    state = Puzzle(INITIAL_STATE, (0, 0), '', hs=['manhattan'])
    algorithm = BuscaGananciosa()
    start = time()
    result = algorithm.search(state)
    end = time()
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    print(f'Tempo de espera: {end - start} segundos')

if __name__ == '__main__':
    main()
