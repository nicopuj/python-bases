# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def seuilSomme(seuil):
    m=150
    n=0
    while m<=seuil:
        m=m+3
        n=n+1
    return n
    

inputs_seuilSomme = [
    Args(1000), Args(2000), Args(150), Args(3000)
]

exo_seuilSomme = ExerciseFunction(
    seuilSomme,
    inputs_seuilSomme
)

def seuilProduit(seuil):
    m=150
    n=0
    while m<=seuil:
        m=m*2
        n=n+1
    return n
    
inputs_seuilProduit = [
    Args(7000), Args(100000), Args(150), Args(4800)
]

exo_seuilProduit = ExerciseFunction(
    seuilProduit,
    inputs_seuilProduit
)