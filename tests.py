from Puzzle8 import Puzzle
from SearchAlgorithms import BuscaGananciosa, AEstrela, pretty_print_table
from main import get_algorithm

from time import time

def test_1():

    INITIAL_STATE = [
        [1, 3, 4],
        [8, 0, 5],
        [7, 2, 6]
    ]
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos')
    assert result.show_path() == ' ; 0 <--> 2 ; 0 <--> 6 ; 0 <--> 5 ; 0 <--> 4 ; 0 <--> 3 ; 0 <--> 2'
    assert (end - start) < 0.05

def test_2():

    INITIAL_STATE = [
        [2, 3, 1],
        [8, 0, 4],
        [7, 6, 5]
    ]
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos')
    assert result.show_path() == ' ; 0 <--> 4 ; 0 <--> 1 ; 0 <--> 3 ; 0 <--> 2 ; 0 <--> 8 ; 0 <--> 4 ; 0 <--> 1 ; 0 <--> 3 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 4 ; 0 <--> 8 ; 0 <--> 1 ; 0 <--> 2 ; 0 <--> 3 ; 0 <--> 4' 
    assert (end - start) < 0.05

def test_3():

    INITIAL_STATE = [
        [2, 3, 1],
        [7, 0, 8],
        [6, 5, 4]
    ]
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm('A*')
    print('Estado inicial')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos')
    assert result.show_path() == ' ; 0 <--> 8 ; 0 <--> 1 ; 0 <--> 3 ; 0 <--> 8 ; 0 <--> 1 ; 0 <--> 4 ; 0 <--> 5 ; 0 <--> 6 ; 0 <--> 7 ; 0 <--> 1 ; 0 <--> 8 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 8'
    assert (end - start) < 0.05

def test_4():

    INITIAL_STATE = [
        [2, 8, 3],
        [1, 4, 0],
        [7, 6, 5]
    ]
    HEURISTIC = 'manhattan'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    algo_name, algorithm = get_algorithm()
    print('Estado inicial')
    pretty_print_table(INITIAL_STATE)
    print(f'{algo_name} c/ heuristica {HEURISTIC}')
    
    start = time()
    result = algorithm.search(state)
    end = time()
    print(f'Tempo de espera: {end - start} segundos')
    assert result.show_path() == ' ; 0 <--> 4 ; 0 <--> 8 ; 0 <--> 2 ; 0 <--> 1 ; 0 <--> 8'
    assert (end - start) < 0.05

def test_5():

    INITIAL_STATE = [
        [5, 4, 0],
        [6, 1, 8],
        [7, 3, 2]
    ]
    HEURISTIC = 'manhattan2'
    state = Puzzle(INITIAL_STATE, (0, 0), '', HEURISTIC)

    print('Estado inicial')
    pretty_print_table(INITIAL_STATE)
    is_possible = state.is_possible()
    
    assert not is_possible
