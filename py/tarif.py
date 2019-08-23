# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def tarif(n):
    prix=30+3.5*n
    return prix

inputs_tarif = [
    Args(0), Args(1), Args(2), Args(5), Args(20)
]

exo_tarif = ExerciseFunction(
    tarif,
    inputs_tarif
)