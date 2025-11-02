from tkinter import*

def draw_image():
    global img
    img=PhotoImage(file="wl.gif")
    canvas.create_image(20,20,anchor=NW, image=img) #NW는 North-West
    
root=Tk()
root.geometry("500x500")

canvas=Canvas(root, width=400, height=400, bg='white')
canvas.pack()

button=Button(root, text="이미지 표시", command=draw_image)
button.pack()

root.mainloop()