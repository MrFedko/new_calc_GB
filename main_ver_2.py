from tkinter import *


window = Tk()      
window.title("Калькулятор выходного дня")
window["bg"] = "#555"
window.geometry("400x200+200+200")
window.resizable(False, False)

formula = "0"
text_bar = Label(window, text="Что посчитать?", font=("Times New Roman", 21, "bold"))
text_bar.place(x=50, y=51)


txt = Entry(window,width=10)
txt.place(x=50, y=101) 
txt.focus() 
def commands(_):
    global formula
    formula = str(eval(txt.get()))
    update()
    


result_text = Label(window, text="Ответ: ", font=("Times New Roman", 21, "bold"))
result_text.place(x=50, y=151)

lbl = Label(text=formula, font=("Times New Roman", 21, "bold"), bg="#555", foreground="#FFF")
lbl.place(x=150, y=151)

def update():
    global formula
    global lbl
    if formula == "":
        formula = "0"
    lbl.configure(text=formula)

com = lambda x=formula: commands(x)
Button(text='Ответ', bg="#FFF", font=("Times New Roman", 15), command=com).place(x=50, y=151)

window.mainloop()
