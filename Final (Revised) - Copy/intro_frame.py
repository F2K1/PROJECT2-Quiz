from tkinter import *


class IntroFrame(Frame):
    def __init__(self, parent, controller):
        super(IntroFrame, self).__init__(parent)
        self.controller = controller
        
        self.label = Label(self, text="Insert Nickname")
        self.label.pack()

        self.username = StringVar()
        self.entry = Entry(self, textvariable=self.username)
        self.entry.pack()
        
        self.button = Button(self, text="Submit", command=lambda: controller.registerPlayer(self.username.get()))
        self.button.pack()

        self.warning = StringVar()
        self.warning.set("")
        self.warning_label = Label(self, text=self.warning.get())
        self.warning_label.pack()
    
    def resetUsernameVar(self):
        self.username.set("")

        self.warning_label.destroy()
        self.warning.set("Please insert a correct username with: \n 1) less than or equal to 15 characters \n 2) no spaces in the front and end of the word \n 3) no commas")
        self.warning_label = Label(self, text=self.warning.get())
        self.warning_label.pack()