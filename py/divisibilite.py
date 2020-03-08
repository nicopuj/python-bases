# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def divisible(a,b):   # teste si a divisible par b
    if a%b==0:
        return True
    else:
        return False

inputs_divisibilite = [
    Args(14357,2), Args(486,9), Args(1876,4), Args(1876,3), Args(1876,2), Args(765,5)  
]

exo_divisibilite = ExerciseFunction(
    divisible,
    inputs_divisibilite
)