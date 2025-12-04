from tkinter import*
import random
import time

tk=Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

game_over_text_id = None
restart_button = None
score = 0
score_display = None

def update_score_display():
    global score_display, score
    if score_display is None:
        score_display = canvas.create_text(50, 20, text=f'Score: {score}')
    else:
        canvas.itemconfig(score_display, text=f'Score: {score}')

def game_over():
    global game_over_text_id, restart_button
    game_over_text_id = canvas.create_text(250, 180, text='GAME OVER')
    
    restart_button = Button(tk, text="RESTART", command=restart_game)
    canvas.create_window(250, 250, window=restart_button)

def restart_game():
    global game_over_text_id, restart_button, ball, paddle, score, score_display

    score = 0
    if score_display:
        canvas.delete(score_display)
        score_display = None
    update_score_display()
    
    if game_over_text_id:
        canvas.delete(game_over_text_id)
        game_over_text_id = None
    
    if restart_button:
        restart_button.destroy() 
        restart_button = None
        
    canvas.delete(ball.id)
    canvas.delete(paddle.id)

    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas=canvas
        self.id=canvas.create_oval(10, 10, 25, 25, fill=color)
        self.paddle=paddle
        self.canvas.move(self.id, 245, 100)

        starts=[-2, 2] 
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-2
        
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

        self.hit_bottom=False

    def hit_paddle(self, pos):
        paddle_pos= self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]: 
                return True
        return False

    def draw(self):
        global score
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y=2
        
        if pos[3] >= self.canvas_height:
            self.hit_bottom=True
            game_over()

        if not self.hit_bottom:
            if self.hit_paddle(pos):
                self.y = -abs(self.y)
                
                # 충돌할 경우 공 속도 점점 빨라지도록
                if self.x > 0:
                    self.x += 0.2
                else:
                    self.x -= 0.2

                self.y -= 0.2

                score += 1
                update_score_display()

        if pos[0] <= 0:
            self.x=2
        if pos[2] >= self.canvas_width:
            self.x=-2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x=0
        self.canvas_width=self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x=-3

    def turn_right(self, evt):
        self.x=3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos=self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x=0
        elif pos[2] >= self.canvas_width:
            self.x=0

update_score_display()

paddle=Paddle(canvas, 'blue')
ball=Ball(canvas, paddle, 'red')

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop