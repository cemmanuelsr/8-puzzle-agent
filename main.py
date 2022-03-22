from Puzzle8 import Puzzle
from SearchAlgorithms import BuscaGananciosa, AEstrela, pretty_print_table

from time import time
import argparse

parser = argparse.ArgumentParser(prog='main')
parser.add_argument('-a', '--algorithm', type=str, default='bg')
parser.add_argument('-H', '--heuristic', type=str, default='manhattan2')
args = parser.parse_args()

def get_algorithm(algorithm='bg'):
    if(algorithm == 'bg'):
        return 'Busca Gananciosa', BuscaGananciosa()
    if(algorithm == 'star'):
        return 'A*', AEstrela()

def main():

    INITIAL_STATE = [
        [2, 8, 3],
        [1, 4, 0],
        [7, 6, 5]
    ]
    state = Puzzle(INITIAL_STATE, (0, 0), '', args.heuristic)

    if(state.is_possible()):

        algo_name, algorithm = get_algorithm(args.algorithm)
        print(f'Estado inicial - Realizando {algo_name} c/ heuristica {state.heuristic}')
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
