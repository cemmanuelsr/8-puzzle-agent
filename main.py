from Puzzle8 import Puzzle
from SearchAlgorithms import BuscaGananciosa, AEstrela, pretty_print_table
from Graph import State

from copy import deepcopy
from time import time

def flatten_table(table):
    flatten = list()
    for i in range(len(table)):
        for j in range(len(table[0])):
            flatten.append(table[i][j])

    return flatten

def get_algorithm(algorithm='BG'):
    if(algorithm == 'BG'):
        return 'Busca Gananciosa', BuscaGananciosa()
    if(algorithm == 'A*'):
        return 'A*', AEstrela()

def main():

    INITIAL_STATE = [
        [2, 3, 1],
        [8, 0, 4],
        [7, 6, 5]
    ]
    state = Puzzle(INITIAL_STATE, (0, 0), '', 'manhattan2')

    if(state.is_possible()):

        algo_name, algorithm = get_algorithm()
        print(f'Estado inicial - {algo_name}')
        pretty_print_table(INITIAL_STATE)
        
        start = time()
        result = algorithm.search(state)
        end = time()
        if result != None:
            print('Achou!')
            print(result.show_path())
        else:
            print('Nao achou solucao')

        print(f'Tempo de espera: {end - start} segundos')
    
    else:
       print('Tabuleiro sem solucao')

if __name__ == '__main__':
    main()
