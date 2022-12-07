from html import unescape
from window import App
from datafile_handler import DatafileHandler
from quiz import Quiz


class Controller:
    def __init__(self):
        self.window = App(self)
        self.players_list = DatafileHandler()
        self.current_player = None
        self.levels_list = None
        self.iteration = 0
        self.total_points = 0

    def showFrame(self, frame_id):
        self.window.showFrame(frame_id)

    def registerPlayer(self, username):
        self.current_player = self.players_list.registerPlayer(username)
        if self.current_player == None:
            self.window.intro_frame.resetUsernameVar()
            self.showFrame(0)
        else:
            self.getLevels()

    def getLevels(self):
        self.quiz = Quiz()
        self.levels_list = self.quiz.levels_list
        self.changeLevel(self.iteration)

    def changeLevel(self, iteration):
        if iteration > 9:
            self.window.endgame_frame.loadEndResult(self.getTotal())
            self.showFrame(3)

        elif iteration == 0:
            self.window.game_frame.loadLevel(unescape(self.levels_list[iteration][0].question), unescape(self.levels_list[iteration][0].answer1), 
                                            unescape(self.levels_list[iteration][0].answer2), unescape(self.levels_list[iteration][0].answer3), 
                                            unescape(self.levels_list[iteration][0].answer4), unescape(self.levels_list[iteration][1]))
            self.showFrame(1)
        
        elif (iteration >= 1) and (iteration <= 9):
            self.window.game_frame.destroyLevel()
            self.window.game_frame.loadLevel(unescape(self.levels_list[iteration][0].question), unescape(self.levels_list[iteration][0].answer1), 
                                            unescape(self.levels_list[iteration][0].answer2), unescape(self.levels_list[iteration][0].answer3), 
                                            unescape(self.levels_list[iteration][0].answer4), unescape(self.levels_list[iteration][1]))
            self.showFrame(1)
    
    def checkAnswer(self, choice, correct_answer):
        if choice == correct_answer:
            self.current_player.points = str(int(self.current_player.points) + 1)
            self.window.result_frame.loadResult("Correct!")
            self.total_points += 1

        elif choice != correct_answer:
            self.window.result_frame.loadResult("Wrong!")
    
    def iterateLevel(self):
        self.iteration += 1
        self.changeLevel(self.iteration)

    def getTotal(self):
        self.current_player.winning_ratio = str(self.total_points) + ":10"
        return self.total_points

    def restartGame(self):
        self.current_player.points = str(int(self.current_player.points) - self.total_points)
        self.total_points = 0
        self.iteration = 0
        self.window.game_frame.destroyLevel()
        self.getLevels()

    def endGame(self):
        self.players_list.updateFile(self.current_player)
        self.window.destroy()
        

if __name__ == "__main__":
    controller = Controller()
    controller.window.mainloop()
