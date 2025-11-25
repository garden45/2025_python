import tkinter as tk

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = []  # has-a: 수강 과목 리스트

    def enrollCourse(self, subject):
        if subject not in self.classes:
            self.classes.append(subject)

    def clearCourses(self):
        self.classes.clear()

root = tk.Tk()
root.title("문제 4")
root.geometry("380x280")

stu = Student("홍길동")
title = tk.Label(root, text=f"학생: {stu.name}", font=("맑은고딕", 11, "bold"))
title.pack(pady=10)

frm = tk.Frame(root)
frm.pack(pady=10, anchor="center")

# Checkbutton 상태 변수, 모두 해제되어 있는 상태
var_py  = tk.IntVar(value=0)
var_ai  = tk.IntVar(value=0)
var_ds  = tk.IntVar(value=0)

cb1 = tk.Checkbutton(frm, text="Python",      variable=var_py)
cb2 = tk.Checkbutton(frm, text="AI",          variable=var_ai)
cb3 = tk.Checkbutton(frm, text="DataScience", variable=var_ds)

cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

result = tk.StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=10)

# 동작 함수들 # 현재 체크 상태를 기준으로 과목 리스트 갱신
def register_courses():
    stu.clearCourses()
    if var_py.get(): stu.enrollCourse("Python")
    if var_ai.get(): stu.enrollCourse("AI")
    if var_ds.get(): stu.enrollCourse("DataScience")

    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0); var_ai.set(0); var_ds.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="등록하기", command=register_courses).pack(side="left", padx=10)
tk.Button(button_frame, text="초기화",   command=reset_all).pack(side="left", padx=10)

root.mainloop()