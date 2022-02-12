from tkinter import *
import ui_calc

def logic_calc(self, operation):
    if operation == "C":
        self.formula = ""
    elif operation == "DEL":
        self.formula = self.formula[0:-1]
    elif operation == "X^2":
        self.formula = str((eval(self.formula))**2)
    elif operation == "=":
        self.formula = str(eval(self.formula))
    elif operation == ".":
        self.formula = str(float(self.formula))
    else:
        if self.formula == "0":
            self.formula = ""
        self.formula += operation