from tkinter import *


class EndgameFrame(Frame):
    def __init__(self, parent, controller):
        super(EndgameFrame, self).__init__(parent)
        self.controller = controller

        label1 = Label(self, text="Game Over!")
        label1.grid(row=0, column=1)

        self.total_var = StringVar()
        self.label2 = Label(self, text=self.total_var.get())
        self.label2.grid(row=1, column=1)

        button1 = Button(self, text="Exit", command=lambda: controller.endGame())
        button1.grid(row=2, column=0)

        button2 = Button(self, text="Restart", command=lambda: controller.restartGame())
        button2.grid(row=2, column=2)
    
    def loadEndResult(self, total_points):
        self.total_var.set(total_points)
        self.label2.config(text=self.total_var.get())
