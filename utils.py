from random import randint, choice

from SearchAlgorithms import BuscaGananciosa, AEstrela

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

def initial_state(string_state):
    tiles = [int(tile) for tile in string_state.split(',')]
    table = [tiles[i:i+3] for i in range(0, len(tiles), 3)]

    return table

def get_algorithm(algorithm='bg'):
    if(algorithm == 'bg'):
        return 'Busca Gananciosa', BuscaGananciosa()
    if(algorithm == 'star'):
        return 'A*', AEstrela()

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

def get_coords(table, tile):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if(table[i][j] == tile):
                return i, j

def shuffle_table(table):
    zero_row, zero_col = get_coords(table, 0)
    number_of_ops = randint(5, 20)
    past_possibility = (0,0)
    path = ''

    for _ in range(number_of_ops):
        diff_row, diff_col = choice(POSSIBILITIES)
        while((-diff_row, -diff_col) == past_possibility or not(0 <= zero_row + diff_row <= 2 and 0 <= zero_col + diff_col <= 2)):
            diff_row, diff_col = choice(POSSIBILITIES)

        op = f'{table[zero_row][zero_col]} <--> {table[zero_row + diff_row][zero_col + diff_col]}'
        table[zero_row][zero_col], table[zero_row + diff_row][zero_col + diff_col] = table[zero_row + diff_row][zero_col + diff_col], table[zero_row][zero_col]

        path = path + ' ; ' + op
        zero_row, zero_col = zero_row + diff_row, zero_col + diff_col

    return path
