#!/usr/bin/env python3

import turtle
import random
import time
import argparse
from shape import Shape
from window import Window

class Pong:
    """Class Pong, the behaviour of the game
    """
    def __init__(self):
        """Create a new Pong Game, and all its components
        """
        self.score_a = 0
        self.score_b = 0
        self.window = Window("Pong","black",800,600)
        self.paddle_a = Shape(-350,0)
        self.paddle_b = Shape(350,0)
        self.ball = Shape(0,0,1,1,"circle")
        self.pen = Shape(0, 260)
        self.pen.action.hideturtle()
    
    def run(self):
        """The main method of the game, a window for the game is created, and all
        the necessary components such as the paddles, the ball and the score.
        """
        self.window.actions(self.paddle_a,self.paddle_b)
        self.pen.action.write("0 - 0", align="center", font=("Courier", 20, "normal"))
        self.window.update()
        time.sleep(1)
        while True:
            self.window.update()
            self.ball.setx(self.ball.xcor() + self.ball.ball_dx)
            self.ball.sety(self.ball.ycor() + self.ball.ball_dy)
            self.__check_borders()
            if self.__point():
                time.sleep(1)
            self.__hit()
            if self.score_a == 5 or self.score_b == 5:
                time.sleep(1)
                break

    def __check_borders(self):
        """Check the collision between the edges and the ball so that it feels bouncing
        """
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.ball_dy *= -1
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.ball_dy *= -1

    def __point(self):
        """If a player score, the ball starts at the begining, the score its updated
        """
        while True:
            x = random.randint(-1,1)
            y = random.randint(-1,1)
            if x != 0 and y != 0:
                break
        if self.ball.xcor() > 390:
            self.ball.action.goto(0, 0)
            self.ball.ball_dx = 0.1 * x
            self.ball.ball_dy = 0.1 * y
            self.score_a += 1
            self.__update_score()
            return True
        if self.ball.xcor() < -390:
            self.ball.action.goto(0, 0)
            self.ball.ball_dx = 0.1 * x
            self.ball.ball_dy = 0.1 * y
            self.score_b += 1
            self.__update_score()
            return True
        return False

    def __hit(self):
        """The collision between the paddles and the ball so that it feels bouncing
        """
        if (self.ball.xcor() > 330 and self.ball.xcor() < 350) and (self.ball.ycor() < self.paddle_b.ycor() + 50 and self.ball.ycor() > self.paddle_b.ycor() -50):
            self.ball.setx(330)
            self.__speed()
            self.ball.ball_dx *= -1
        if (self.ball.xcor() < -330 and self.ball.xcor() > -350) and (self.ball.ycor() < self.paddle_a.ycor() + 50 and self.ball.ycor() > self.paddle_a.ycor() -50):
            self.ball.setx(-330)
            self.__speed()
            self.ball.ball_dx *= -1
    
    def __speed(self):
        """Each time a paddle hit the ball, the speed of the ball increase
        """
        if (self.ball.ball_dx > 0):
            self.ball.increase_dx()
        else:
            self.ball.decrease_dx()
        if (self.ball.ball_dy > 0):
            self.ball.increase_dy()
        else:
            self.ball.decrease_dy()

    def __update_score(self):
        """Update the score by cleaning the old one and writing a new one
        """
        self.pen.action.clear()
        self.pen.action.write("{} - {}".format(self.score_a,self.score_b), 
                                align="center", font=("Courier", 20, "normal"))
        
if __name__ == "__main__":
    Pong().run()