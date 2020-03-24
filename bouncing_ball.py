#/usr/bin/env python
# _*_ coding:utf-8 _*_

#It's a bouncing game from the <python for kids>
#Author: CHEN Wen.

from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.inits()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def inits(self):
        self.canvas.coords(self.id, 255, 110, 270, 125) #Set the initial coords of Ball.
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: #If the ball x axis is in the paddle x axis scope.
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]: #If the ball y axis is in the paddle y axis scope.
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) 
        pos = self.canvas.coords(self.id)
        #Usually will go every [3,3] step except hit the top/bottom or left/right line.
        #In this exceptions, the ball should go back with -3 step in x or y axis.
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.inits()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def inits(self):
        self.canvas.coords(self.id, 200, 300, 300, 310) #Set the initial coords of the paddle.
        self.x = 0

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.x <= 0:
            self.x = 0
        elif pos[2] + self.x >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text = self.score, fill = color)

    def inits(self):
        self.score = 0
        self.canvas.itemconfig(self.id, text = self.score)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text = self.score)

class StartButton:
    def __init__(self, canvas, ball, paddle, score):
        self.canvas = canvas
        self.ball = ball
        self.paddle = paddle
        self.score = score
        self.button = Button(tk, text = 'Start', command = self.callback)
        self.button.pack()
        self.started = False 

    def callback(self):
        if self.started == False:
            self.started = True
            self.button.forget()
            self.init_game()

    def init_game(self):
        self.ball.inits()
        self.paddle.inits()
        self.score.inits()
        self.canvas.itemconfig(game_over_text, state = 'hidden')

if __name__ == '__main__':

    tk = Tk()
    tk.title('Bouncing Game')
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)

    canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
    canvas.pack()
    tk.update()

    paddle = Paddle(canvas, 'blue')
    score = Score(canvas, 'green')
    ball = Ball(canvas, paddle, score, 'red')
    startbutton = StartButton(canvas, ball, paddle, score)
    game_over_text = canvas.create_text(250, 200, text = 'GAME OVER', state = 'hidden')

    while 1:
        if ball.hit_bottom == False and startbutton.started == True:
            ball.draw()
            paddle.draw()
        if ball.hit_bottom == True:
            time.sleep(1)
            canvas.itemconfig(game_over_text, state = 'normal')
            startbutton.button.pack()
            startbutton.started = False
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

    #tk.mainloop()
