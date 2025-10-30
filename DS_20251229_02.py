from tkinter import *

# 도형을 그리는 함수
def draw_shape():
    canvas.delete("all")  # 이전 그림 지우기
    choice = shape_var.get()
    
    if choice == 1:  # 사각형
        canvas.create_rectangle(50, 50, 150, 150, fill="red")
    elif choice == 2:  # 원(oval)
        canvas.create_oval(200, 80, 300, 180, fill="blue")
    elif choice == 3:  # 텍스트
        def draw_image():
            global img
            img=PhotoImage(file="dog1.gif")
            canvas.create_image(20,20,anchor=NW, image=img)

# 메인 윈도우 생성
root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

# 캔버스
canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

# 라디오 버튼 선택값 저장 변수
shape_var = IntVar()
shape_var.set(1)  # 기본값: 사각형

frame = Frame(root)
frame.pack(pady=10)

button1=Button(root, text="사각형", command=draw_shape).pack(side="left", padx=10)
button2=Button(root, text="원", command=draw_shape).pack(side="left", padx=10)
button3=Button(root, text="그림", command=draw_shape).pack(side="left", padx=10)
button4=Button(root, text="지우기", command=draw_shape).pack(side="left", padx=10)

label=Label(root, text="버튼을 눌러 도형을 선택하세요.")
label.pack()


root.mainloop()