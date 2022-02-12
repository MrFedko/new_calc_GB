from tkinter import *
import ui_calc

def logicalc(operation):
    if operation == "C":
        formula = ""
    elif operation == "DEL":
        formula = formula[0:-1]
    elif operation == "X^2":
       formula = str((eval(formula))**2)
    elif operation == "=":
        formula = str(eval(formula))
    elif operation == ".":
        formula = str(float(formula))
    else:
        if formula == "0":
            formula = ""
        formula += operation


