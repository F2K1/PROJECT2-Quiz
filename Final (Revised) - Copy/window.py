from tkinter import *
from intro_frame import IntroFrame
from game_frame import GameFrame
from result_frame import ResultFrame
from endgame_frame import EndgameFrame


class App(Tk):
    def __init__(self, controller):
        super(App, self).__init__()
        
        self.controller = controller

        self.cont = Frame(self)
        self.cont.pack()
        self.cont.rowconfigure(0, weight=1)
        self.cont.columnconfigure(0, weight=1)

        self.geometry("400x400")

        self.intro_frame = IntroFrame(self.cont, self.controller)
        self.intro_frame.grid(row=0, column=0, sticky="nsew")
        
        self.game_frame = GameFrame(self.cont, self.controller)
        self.game_frame.grid(row=0, column=0, sticky="nsew")

        self.result_frame = ResultFrame(self.cont, self.controller)
        self.result_frame.grid(row=0, column=0, sticky="nsew")
        
        self.endgame_frame = EndgameFrame(self.cont, self.controller)
        self.endgame_frame.grid(row=0, column=0, sticky="nsew")

        self.intro_frame.tkraise()
    
    def showFrame(self, frame_id):
        if frame_id == 0:
            self.intro_frame.tkraise()
        elif frame_id == 1:
            self.game_frame.tkraise()
        elif frame_id == 2:
            self.result_frame.tkraise()
        elif frame_id == 3:
            self.endgame_frame.tkraise()
