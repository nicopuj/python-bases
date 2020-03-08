# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def bissextile(annee):
    if annee%400==0 or (annee%4==0 and annee%100!=0):
        return True
    else:
        return False

inputs_bissextile = [
    Args(2020), Args(1988), Args(2010), Args(2100), Args(2400)  
]

exo_bissextile = ExerciseFunction(
    bissextile,
    inputs_bissextile
)