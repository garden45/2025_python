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

# 게임 오버 및 재시작 기능을 위한 전역 변수
game_over_text_id = None
restart_button = None
# 점수
score = 0
score_display = None

# 점수판 업데이트
def update_score_display():
    global score_display, score
    if score_display is None:
        # 점수판이 없으면 (초기 시작 또는 재시작 후) 새로 생성
        score_display = canvas.create_text(50, 20, text=f'Score: {score}')
    else:
        # 점수판이 이미 있으면 텍스트만 업데이트
        canvas.itemconfig(score_display, text=f'Score: {score}')

# 게임 오버 화면을 표시하는 함수
def game_over():
    global game_over_text_id, restart_button
    game_over_text_id = canvas.create_text(250, 180, text='GAME OVER')
    
    restart_button = Button(tk, text="RESTART", command=restart_game)
    canvas.create_window(250, 250, window=restart_button)

# 게임 재시작 함수: 모든 요소를 초기 상태로
def restart_game():
    global game_over_text_id, restart_button, ball, paddle, score, score_display

    # 점수 및 점수판 초기화
    score = 0
    if score_display:
        canvas.delete(score_display)
        score_display = None
    update_score_display()
    
    # 게임 오버 텍스트 제거
    if game_over_text_id:
        canvas.delete(game_over_text_id)
        game_over_text_id = None
    
    # 재시작 버튼 제거
    if restart_button:
        restart_button.destroy() 
        restart_button = None
        
    # 기존 공과 패들을 제거하고 새로 생성
    canvas.delete(ball.id)
    canvas.delete(paddle.id)
    
    # 공과 패들 객체를 새로 만들고 초기화
    # 전역 변수를 다시 할당해야 다음 게임 루프에서 새 객체를 사용
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

        # pos는 공의 [x1, y1, x2, y2] 좌표
        # pos[0]은 왼쪽 X, pos[2]는 오른쪽 X
        # pos[1]은 상단 Y, pos[3]은 하단 Y

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
            game_over() # 공이 바닥에 닿으면 게임 오버 함수 호출

        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:
                self.y = -2

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
    # ball.hit_bottom이 False일 때만 공과 패들을 움직이도록 함.
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop