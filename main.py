from tkinter import *

window = Tk()      
window.title("Калькулятор выходного дня")
window["bg"] = "#000"
window.geometry("400x350+500+250")
window.resizable(False, False)
formula = "0"
lbl = Label(text=formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
lbl.place(x=11, y=50)
btns = ["C", "(", ")", "*",
        "1", "2", "3", "/",
        "4", "5", "6", "+",
        "7", "8", "9", "-",
        "0101", "0", ".", "="
        ]     

def commands(any_char):
    global formula 
    if any_char == "C":
        formula = ""
    elif any_char == "0101":
        formula = int(formula)
        result = ''
        while formula != 0:
            result = str(formula % 2) + result
            formula //= 2
        formula = result
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

x = 0
y = 100
for bt in btns:
    com = lambda x=bt: commands(x)
    Button(text=bt, bg="#FFF", font=("Times New Roman", 15), command=com).place(x=x, y=y, width=100, height=50)
    x += 100
    if x > 300:
        x = 0
        y += 50

window.mainloop()