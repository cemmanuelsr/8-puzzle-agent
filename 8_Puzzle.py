from SearchAlgorithms import BuscaGananciosa
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

class Puzzle(State):

    def __init__(self, table, exclude_move, op):
        self.table = table
        self.exclude_move = exclude_move
        self.operator = op

    def blank_space_coords(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if(self.table[i][j] == 0):
                    return i, j
    
    def sucessors(self):
        sucessors = []

        zero_row, zero_col = self.blank_space_coords()

        for diff_row, diff_col in POSSIBILITIES:

            if((diff_row, diff_col) != self.exclude_move):

                copy_table = deepcopy(self.table)

                if(0 <= zero_row + diff_row <= 2 and 0 <= zero_col + diff_col <= 2):
                    op = f'{copy_table[zero_row][zero_col]} <--> {copy_table[zero_row + diff_row][zero_col + diff_col]}'
                    copy_table[zero_row][zero_col], copy_table[zero_row + diff_row][zero_col + diff_col] = copy_table[zero_row + diff_row][zero_col + diff_col], copy_table[zero_row][zero_col]

                    sucessors.append(Puzzle(copy_table, (-diff_row, -diff_col), op))

        return sucessors
    
    def is_goal(self):
        return self.table == GOAL_TABLE
    
    def description(self):
        return "https://en.wikipedia.org/wiki/15_puzzle so que 8-Puzzle"
    
    def cost(self):
        return 1

    def n_right_positions(self):
        n = 0
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if(self.table[i][j] == GOAL_TABLE[i][j]):
                    n += 1

        return n

    def h(self):
        return -self.n_right_positions()

    def print(self):
        return str(self.operator)
    
    def env(self):
        return f'{self.operator} ---> {self.table}'


def main():
    print('Busca Gananciosa')

    INITIAL_STATE = [
        [1, 0, 3],
        [8, 2, 4],
        [7, 6, 5]
    ]

    state = Puzzle(INITIAL_STATE, (0, 0), '')
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
