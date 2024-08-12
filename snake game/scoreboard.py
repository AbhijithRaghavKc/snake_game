import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
            super().__init__()
            self.hideturtle()
            self.goto(0, 270)
            self.score = 0
            self.color("white")
            self.speed("fastest")
            self.penup()
            with open("data.txt") as file:
                self.high_score = int(file.read())
            self.update_score()



    def update_score(self):
            self.clear()
            self.write(f"score: {self.score}  highscore: {self.high_score}", move=False, align="center", font=('Arial', 25, 'normal'))


    def reset(self):
            if self.score > int(self.high_score):
                self.high_score = self.score
                with open("data.txt", mode="w") as file:
                    file.write(f"{self.high_score}")


            self.score = 0
            self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align="center", font=('Arial', 25, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()



