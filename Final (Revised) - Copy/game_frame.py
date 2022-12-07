from tkinter import *


class GameFrame(Frame):
    def __init__(self, parent, controller):
        super(GameFrame, self).__init__(parent)
        self.controller = controller

    def loadLevel(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.label = Label(self, text=question)
        self.label.grid(row=0, column=1)

        self.button1 = Button(self, text=answer1, command=lambda: [self.controller.checkAnswer(answer1, correct_answer), self.controller.showFrame(2)])   
        self.button1.grid(row=1, column=0)

        self.button2 = Button(self, text=answer2, command=lambda: [self.controller.checkAnswer(answer2, correct_answer), self.controller.showFrame(2)])  
        self.button2.grid(row=1, column=2) 

        self.button3 = Button(self, text=answer3, command=lambda: [self.controller.checkAnswer(answer3, correct_answer), self.controller.showFrame(2)]) 
        self.button3.grid(row=2, column=0) 

        self.button4 = Button(self, text=answer4, command=lambda: [self.controller.checkAnswer(answer4, correct_answer), self.controller.showFrame(2)])
        self.button4.grid(row=2, column=2)
    
    def destroyLevel(self):
        self.label.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
