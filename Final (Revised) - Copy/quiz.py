import requests
import json
import copy
import random
from level import Level


class Quiz:
    def __init__(self):
        url = 'https://opentdb.com/api.php?amount=10&type=multiple' #!IMPORTANT
      #   url = open('sample.json') #test
        request = requests.get(url) #!IMPORTANT
        data = json.loads(request.text) #!IMPORTANT
      #   data = json.loads(url.read()) #test
        results = data['results']
         
        self.levels_list = []

        i = 0
        while i <= 9:
           result = results[i]
           question = result['question']
           correct_answer = result['correct_answer']
           incorrect_answers = result['incorrect_answers']
           incorrect_answer1 = incorrect_answers[0]
           incorrect_answer2 = incorrect_answers[1]
           incorrect_answer3 = incorrect_answers[2]
           answers_list = [correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3]
           random.shuffle(answers_list)
           level = Level(question, answers_list[0], answers_list[1], answers_list[2], answers_list[3])
           self.levels_list.append([copy.copy(level), correct_answer])
           i += 1
