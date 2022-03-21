from Puzzle8 import Puzzle
from SearchAlgorithms import BuscaGananciosa, AEstrela, pretty_print_table

from time import time

def get_algorithm(algorithm='BG'):
    if(algorithm == 'BG'):
        return 'Busca Gananciosa', BuscaGananciosa()
    if(algorithm == 'A*'):
        return 'A*', AEstrela()

def main():

    INITIAL_STATE = [
        [2, 8, 3],
        [1, 4, 0],
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

if __name__ == '__main__':
    main()
