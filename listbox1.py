from tkinter import*

root=Tk()

Ib=Listbox(root, height=4)
Ib.pack()
Ib.insert(END,"Python")
Ib.insert(END,"C")
Ib.insert(END,"Java")
Ib.insert(END,"Swift")

root.mainloop()