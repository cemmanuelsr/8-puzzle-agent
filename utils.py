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
