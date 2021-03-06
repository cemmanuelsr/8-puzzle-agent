from Puzzle8 import Puzzle
from utils import initial_state, get_algorithm, shuffle_table

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from time import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Algorithm(str, Enum):
    bg = "BuscaGananciosa"
    star = "A*"

class Heuristic(str, Enum):
    euclidian2 = "EuclidianBetter"
    euclidian = "Euclidian"
    manhattan2 = "ManhattanBetter"
    manhattan = "Manhattan"
    match = "MatchPositions"

@app.get('/solve/{algorithm}/{heuristic}')
async def solve(table : str, algorithm : Algorithm, heuristic : Heuristic):
    initial_table = initial_state(table)
    if(heuristic):
        state = Puzzle(initial_table, (0, 0), '', heuristic.name)
    else:
        state = Puzzle(initial_table, (0, 0), '')

    if(not state.is_possible()):
        raise HTTPException(status_code = 404, detail = 'Not possible solution')

    if(algorithm):
        algo_name, algo = get_algorithm(algorithm.name)
    else:
        algo_name, algo = get_algorithm()
    start = time()
    result = algo.search(state)
    end = time()
    
    if(result != None):
        return { 
            "path": result.show_path(),
            "time": end - start,
            "algorithm_name": algo_name,
            "heuristic_name": state.heuristic
        }
    else:
        raise HTTPException(status_code = 404, detail = 'Not found solution')

@app.get('/shuffle')
def shuffle(table : str):
    initial_table = initial_state(table)
    shuffled = shuffle_table(initial_table)

    return {
        "path": shuffled
    }
