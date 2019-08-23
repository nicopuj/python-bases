# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def difference(a,b):
    resultat=b-a
    return resultat

inputs_difference = [
    Args(3,7), Args(6,2), Args(4,4), Args(-5,1)
]

exo_difference = ExerciseFunction(
    difference,
    inputs_difference
)