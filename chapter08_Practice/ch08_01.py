from tkinter import*

root=tk.Tk()
root.title("Moving Shape App")

canvas=tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

shape=canvas.create_oval(100, 100, 200, 200, fill="blue")

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>, move_right")

canvas.bind("<B1-Motion>", change_color)

root.mainloop()