from Graph import State
from copy import deepcopy

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

def right_position(table):
    n = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if(table[i][j] != 0 and table[i][j] == GOAL_TABLE[i][j]):
                n += 1

    return n

def flatten_table(table):
    flatten = list()
    for i in range(len(table)):
        for j in range(len(table[0])):
            flatten.append(table[i][j])

    return flatten

class Puzzle(State):

    def __init__(self, table, exclude_move, op, heuristic='manhattan'):
        self.table = table
        self.exclude_move = exclude_move
        self.heuristic = heuristic
        self.operator = op

    def is_possible(self):
        flatten = flatten_table(self.table)
        flatten.remove(0)
        possible = 0
        for i in range(len(flatten)):
            for j in range(i+1, len(flatten)):
                if(flatten[j] < flatten[i]):
                    possible += 1

        if(not possible%2):
            print('Nao possui solucao')
        return possible%2

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
                if(0 <= zero_row + diff_row <= 2 and 0 <= zero_col + diff_col <= 2):
                    copy_table = deepcopy(self.table)
                    op = f'{copy_table[zero_row][zero_col]} <--> {copy_table[zero_row + diff_row][zero_col + diff_col]}'
                    copy_table[zero_row][zero_col], copy_table[zero_row + diff_row][zero_col + diff_col] = copy_table[zero_row + diff_row][zero_col + diff_col], copy_table[zero_row][zero_col]

                    sucessors.append(Puzzle(copy_table, (-diff_row, -diff_col), op, self.heuristic))

        return sucessors
    
    def is_goal(self):
        return self.table == GOAL_TABLE
    
    def description(self):
        return "https://en.wikipedia.org/wiki/15_puzzle so que 8-Puzzle"
    
    def cost(self):
        return 1

    def h(self):
        h = 0

        if(self.heuristic == 'manhattan'):
            for tile in range(1, 9):
                tile_row, tile_col = self.tile_coords(tile)
                goal_row, goal_col = TILE_GOALCOORDS_MAP[tile]
                h += (abs(goal_row - tile_row) + abs(goal_col - tile_col))

        if(self.heuristic == 'manhattan2'):
            previous_matching_positions = right_position(self.table)
            for tile in range(1, 9):
                tile_row, tile_col = self.tile_coords(tile)
                goal_row, goal_col = TILE_GOALCOORDS_MAP[tile]

                if(tile_row != goal_row or tile_col != goal_col):
                    for diff_row, diff_col in POSSIBILITIES[:2]:
                        if(0 <= tile_row + diff_row <= 2 and 0 <= tile_col + diff_col <= 2):
                            copy_table = deepcopy(self.table)
                            copy_table[tile_row][tile_col], copy_table[tile_row + diff_row][tile_col + diff_col] = copy_table[tile_row + diff_row][tile_col + diff_col], copy_table[tile_row][tile_col]
                            post_matching_position = right_position(copy_table)

                            if(post_matching_position - previous_matching_positions == 2):
                                h += 2
                                break

                h += (abs(goal_row - tile_row) + abs(goal_col - tile_col))

        if(self.heuristic == 'match'):
            h = 8 - right_position(self.table)

        if(self.heuristic == 'euclidian'):
            for tile in range(1, 9):
                tile_row, tile_col = self.tile_coords(tile)
                goal_row, goal_col = TILE_GOALCOORDS_MAP[tile]
                h += ((goal_row - tile_row)**2 + (goal_col - tile_col)**2)**0.5

        return h

    def print(self):
        return str(self.operator)
    
    def env(self):
        return f'{self.operator} ---> {self.table}'

