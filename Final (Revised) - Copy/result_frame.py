from tkinter import *


class ResultFrame(Frame):
    def __init__(self, parent, controller):
        super(ResultFrame, self).__init__(parent)
        self.controller = controller

        self.result_var = StringVar()
        self.label = Label(self, text=self.result_var.get())
        self.label.pack()

        self.button = Button(self, text="Next", command=lambda: controller.iterateLevel())
        self.button.pack()

    def loadResult(self, result):
        self.result_var.set(result)
        self.label.config(text=self.result_var.get())