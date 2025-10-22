from tkinter import*

root=Tk()
root.geometry("300x100")

f=Frame(root)
f.pack()

b1=Button(root, text="버튼1", bg="red", fg="yellow")
b2=Button(root, text="버튼2", bg="green", fg="yellow")
b3=Button(root, text="버튼3", bg="blue", fg="yellow")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l=Label(root, text="이 레이블은 버튼들 위에 배치된다.")
l.pack()

root.mainloop()