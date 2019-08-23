# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def calcul(x):
    resultat=3*(x-2)/5
    return resultat

inputs_calcul = [
    Args(7), Args(0), Args(12), Args(2), Args(-3)
]

exo_calcul = ExerciseFunction(
    calcul,
    inputs_calcul
)