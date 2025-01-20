from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNALE_COLOR = "#FFC0CB"
FOOD_COLOR = "FF0000"
BACKGROUND_COLOR = "000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0]) #appear in top left corner

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.square.append(square)
class Food:
    def __innit__(self):
        x=random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x+ SPACE_SIZE, y +SPACE_SIZE, fill=FOOD_COLOR, tag ="food")
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinartes.insert(0(x,y))

    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y +SPACE_SIZE, fill = SNAKE_COLOR)

    snake.squares.insert(0, square)
    
    window.after(SPEED, next_turn, snake, food)

def change_direction(new direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snek Game")
window.resizable(False, False)

score = 0
direction = "down"
label = label(window, text = "Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, HEIGHT=GAME__HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height =window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_widht/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.mainloop()