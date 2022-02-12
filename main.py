from tkinter import *
import logicalc
import ui_calc

class Main(Frame):
    ui_calc.ui_calc()
    logicalc.logic_calc()
    logicalc.update()
    
    def __init__(self, root):
            super(Main, self).__init__(root)
            self.ui_calc()
            
if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()