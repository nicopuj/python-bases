# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def capital(n):
    c=1000
    for annee in range(1,n+1):
        c=c*1.05
    return c
    

inputs_capital = [
    Args(1), Args(2), Args(4), Args(10) , Args(0)
]

exo_evolution = ExerciseFunction(
    capital,
    inputs_capital
)

