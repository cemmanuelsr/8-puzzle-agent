from Puzzle8 import Puzzle
from utils import initial_state, get_algorithm

from fastapi import FastAPI, HTTPException
from typing import Optional
from enum import Enum
from time import time

app = FastAPI()

class Algorithm(str, Enum):
    BuscaGananciosa: "bg"
    AEstrela: "star"

class Heuristic(str, Enum):
    Manhattan: "manhattan"
    Euclidian: "euclidian"
    MatchPositions: "match"
    ManhattanBetter: "manhattan2"

@app.get('/solve/')
async def solve(table : str, algorithm : Optional[Algorithm], heuristic : Optional[Heuristic]):
    pass
