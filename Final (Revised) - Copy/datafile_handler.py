import csv
import copy
import datetime
from re import search
from player import Player


class DatafileHandler:
    def __init__(self):
        self.players_list = []
        self.current_player = None

        self.readFile()
    
    def readFile(self):
        with open("players.csv", "r") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                player = Player(row["Username"], row["Date"], row["Points"], row["Winning Ratio"])
                self.players_list.append(copy.copy(player))
    
    def registerPlayer(self, username):
        if (username.strip()) and (len(username) <= 15) and (search(",", username) == None) and (username != None):
            for player in self.players_list:
                if username == player.username:
                    self.current_player = copy.copy(player)
                    return self.current_player
                else:
                    pass

            if self.current_player == None:
                self.current_player = Player(username, self.getCurrentDate(), "0", "0:10")
                return self.current_player
            else:
                pass
        else:
            pass
    
    def getCurrentDate(self):
        return datetime.datetime.now().strftime("%d/%m/%Y")
        
    def updateFile(self, current_player):
        for player in self.players_list:
            if current_player.username == player.username:
                self.players_list.remove(player)
                self.current_player.date = self.getCurrentDate()
                self.players_list.append(current_player)
                self.current_player = None
                break
            else:
                pass
        
        if self.current_player != None:
            self.current_player.date = self.getCurrentDate()
            self.players_list.append(current_player)
        
        with open("players.csv", "w") as file:
            file.write("Username,Date,Points,Winning Ratio\n")
            for player in self.players_list:
                file.write(player.username + "," + player.date + "," + player.points + "," + player.winning_ratio + "\n")

