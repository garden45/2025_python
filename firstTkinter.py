import tkinter as tk

root=tk.TK()
root.title("Tkinter 예제")
root.geometry("200*100")

label=tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

root.mainloop()