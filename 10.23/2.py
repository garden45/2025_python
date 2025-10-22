from tkinter import*

root=Tk()

button=Button(root, text="Hello world", command=root.quit)
button.pack(padx=100)

root.mainloop()