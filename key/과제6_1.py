import tkinter as tk


class Employee:
    def __init__(self, name):
        self.name = name
    def calculate_bonus(self, score):
        return 0 


class Manager(Employee):
    def calculate_bonus(self, score):
        return score * 100000
    def get_role_name(self):
        return "매니저"

class Engineer(Employee):
    def calculate_bonus(self, score):
        return score * 50000 + 150000
    def get_role_name(self):
        return "엔지니어"

employee_name = "홍길동"
manager = Manager(employee_name)
engineer = Engineer(employee_name)
current_employee = manager 


def set_manager_role():
    global current_employee
    current_employee = manager

def set_engineer_role():
    global current_employee
    current_employee = engineer

def calculate():
    global current_employee, score_entry, result_label 
    
    score = int(score_entry.get()) 
    
    bonus = current_employee.calculate_bonus(score)
    role_text = current_employee.get_role_name()
    
    result = f"{role_text} {current_employee.name}의 보너스: {bonus:,}원"
    result_label.config(text=result, foreground='blue')


root = tk.Tk()
root.title("성과 보너스 계산")
root.geometry("350x200")

role_var = tk.StringVar(value="Manager")

tk.Label(root, text=f"직원: {employee_name}\n역할/점수(1-10)를 선택하고 계산하세요.").grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(root, text="역할:").grid(row=1, column=0, padx=5, sticky='w')

tk.Radiobutton(root, text="매니저", variable=role_var, value="Manager", 
                command=set_manager_role).grid(row=1, column=1, sticky='w')
tk.Radiobutton(root, text="엔지니어", variable=role_var, value="Engineer", 
                command=set_engineer_role).grid(row=1, column=2, sticky='w')

tk.Label(root, text="점수 (1-10):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
score_entry = tk.Entry(root, width=5)
score_entry.insert(0, "8")
score_entry.grid(row=2, column=1, sticky='w')

tk.Button(root, text="보너스 계산", command=calculate).grid(row=3, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="계산 결과를 여기에 표시합니다.", font=('Arial', 10, 'bold'))
result_label.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()