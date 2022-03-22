from Puzzle8 import Puzzle
from SearchAlgorithms import BuscaGananciosa, AEstrela

from fastapi import FastAPI, HTTPException
from typing import Optional
from enum import Enum
from time import time

app = FastAPI()

class Algorithm(str, Enum):
    BuscaGananciosa: "bg"
    AEstrela: "a"

class Heuristic(str, Enum):
    Manhattan: "manhattan"
    Euclidian: "euclidian"
    MatchPositions: "match"
    ManhattanBetter: "manhattan2"

@app.get('/solve/')
async def solve(table : str, algorithm : Optional[Algorithm], heuristic : Optional[Heuristic]):
    pass
