#importing classes

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setting the screen up 

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game ")
screen.tracer(0)

#creating the objects (Snake , Food , Scoreboard)

food=Food()
snake = Snake()
scoreboard=Scoreboard()

#setting the key map 


screen.listen()
screen.onkeypress(snake.up ,"z")
screen.onkeypress(snake.down,"s")
screen.onkeypress(snake.left,"q")
screen.onkeypress(snake.right,"d")
game_is_on=True

#the implementation 

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    scoreboard.update_score()
    # Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_score()
    # Detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() <-290 or snake.head.ycor() >280 or snake.head.ycor() <-280 :
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
         if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
    #if head collides with any segment in the tail
        #trigger game_over


screen.exitonclick()







