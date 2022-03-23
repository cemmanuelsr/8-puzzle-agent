from Puzzle8 import Puzzle
from SearchAlgorithms import BuscaGananciosa, AEstrela, pretty_print_table
from utils import get_algorithm, initial_state

from time import time

def test_1():

    INITIAL_STATE = initial_state("8, 1, 3, 0, 7, 2, 6, 5, 4")
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial - Facil')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos\n')
    assert result.show_path() == ' ; 0 <--> 8 ; 0 <--> 1 ; 0 <--> 7 ; 0 <--> 2 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 2 ; 0 <--> 7 ; 0 <--> 1 ; 0 <--> 8 ; 0 <--> 7 ; 0 <--> 2 ; 0 <--> 6 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 1 ; 0 <--> 2'
    assert (end - start) < 0.05

def test_2():

    INITIAL_STATE = initial_state("7, 8, 6, 2, 3, 5, 1, 4, 0")
    HEURISTIC = 'euclidian'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial - Difícil 1')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos\n')
    assert result.show_path() == ' ; 0 <--> 5 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 6 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 6 ; 0 <--> 7 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 7 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 5 ; 0 <--> 6 ; 0 <--> 4 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 5 ; 0 <--> 4' 
    assert (end - start) < 0.05

def test_3():

    INITIAL_STATE = initial_state("7, 8, 6, 2, 3, 5, 0, 1, 4")
    HEURISTIC = 'euclidian'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial - Difícil 2')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos\n')
    assert result.show_path() == ' ; 0 <--> 1 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 6 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 6 ; 0 <--> 7 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 7 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 5 ; 0 <--> 6 ; 0 <--> 4 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 5 ; 0 <--> 4'
    assert (end - start) < 0.05

def test_4():

    INITIAL_STATE = initial_state("8, 3, 6, 7, 5, 4, 2, 1, 0")
    HEURISTIC = 'euclidian2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial - Muito Difícil')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos\n')
    assert result.show_path() == ' ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 7 ; 0 <--> 8 ; 0 <--> 3 ; 0 <--> 6 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 5 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 5 ; 0 <--> 4 ; 0 <--> 6 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 6 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 6 ; 0 <--> 8 ; 0 <--> 3 ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 4 ; 0 <--> 8 ; 0 <--> 3 ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 4 ; 0 <--> 3 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 8'
    assert (end - start) < 0.05

def test_5():

    INITIAL_STATE = initial_state("3, 4, 8, 1, 2, 5, 7, 0, 6")
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    print('Estado inicial - Impossível 1')
    pretty_print_table(INITIAL_STATE)
    is_possible = state.is_possible()
    
    assert not is_possible

def test_6():

    INITIAL_STATE = initial_state("5, 4, 0, 6, 1, 8, 7, 3, 2")
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    print('Estado inicial - Impossível 2')
    pretty_print_table(INITIAL_STATE)
    is_possible = state.is_possible()
    
    assert not is_possible
