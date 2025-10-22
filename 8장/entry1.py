from tkinter import*

def x():
    value=entry.get()
    print("입력된 값:",value)

root=Tk()
root.geometry("300x200")

entry=Entry(root)
entry.pack()

button=Button(root, text="확인", command=x)
button.pack()

root.mainloop()
