from tkinter import *


window = Tk()      
window.title("Калькулятор выходного дня")
window["bg"] = "#000"
window.geometry("485x550+200+200")
window.resizable(False, False)
formula = "0"
lbl = Label(text=formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
lbl.place(x=11, y=50)
btns = ["C", "(", ")", "*",
        "1", "2", "3", "/",
        "4", "5", "6", "+",
        "7", "8", "9", "-",
        "DEL", "0", ".", "="
        ]     

def commands(any_char):
    global formula 
    if any_char == "C":
        formula = ""
    elif any_char == "DEL":
        formula = formula[0:-1]
    elif any_char == "X^2":
        formula = str((eval(formula))**2)
    elif any_char == "=":
        formula = str(eval(formula))
    else:
        if formula == "0":
            formula = ""
        formula += any_char
    update()

def update():
    global formula
    global lbl
    if formula == "":
        formula = "0"
    lbl.configure(text=formula)

x = 10
y = 140
for bt in btns:
    com = lambda x=bt: commands(x)
    Button(text=bt, bg="#FFF", font=("Times New Roman", 15), command=com).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81

window.mainloop()