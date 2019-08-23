# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def minimum(a,b):
    if a<b:
        mini=a
    else:
        mini=b
    return mini

inputs_minimum = [
    Args(3,8), Args(7,4), Args(1.264,1.283), Args(-3,-1), Args(2,2)  
]

exo_minimum = ExerciseFunction(
    minimum,
    inputs_minimum
)