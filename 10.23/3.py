from tkinter import*

def exit():
    print("프로그램이 종료되었습니다.")
    root.quit()  #

root=Tk()

button=Button(root, text="Hello world", command=exit)
button.pack(padx=100)

root.mainloop()