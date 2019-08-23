# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def imc(P,T):
    I=P/T**2
    if I>25:
        return "individu en surpoids"
    else:
        return "individu pas en surpoids"

inputs_imc = [
    Args(60,1.80), Args(80,1.60), Args(100,2) 
]

exo_imc = ExerciseFunction(
    imc,
    inputs_imc
)

def imc2(P,T):
    I=P/T**2
    if I>25:
        return "individu en surpoids"
    elif I<18.5:
        return "individu en état de maigreur"
    else:
        return "individu ni maigreur ni surpoids"
    
inputs_imc2 = [
    Args(60,1.80), Args(80,1.60), Args(50,1.70), Args(100,2), Args(74,2)
]

exo_imc2 = ExerciseFunction(
    imc2,
    inputs_imc2,
    layout_args=(20, 35, 35)
)