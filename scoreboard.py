from turtle import Turtle
import os

#creating the scoreboard class

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-50,279)
        self.score=0
    def update_score(self):
        with open(file="data.txt",mode="r") as data:
            content=int(data.read())
            print(content)
            if content>0:
                self.highscore=content
                self.clear()
                self.write(f"Score: {self.score} High score :{content}  ", font=('Arial', 14, 'normal'))
            else:
                self.clear()
                self.write(f"Score: {self.score} High score :{self.highscore}  " , font=('Arial', 14, 'normal'))
    def reset(self):
        if self.score>self.highscore:
           self.highscore=self.score
           with open(file="data.txt", mode="w") as data:
               data.write(str(self.highscore))
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score+=1
 
