from tkinter import*

class Vehicle:
    def __init__(self, name):
        self.name=name

    def drive(self):
        raise NotImplementedError("이것은 추상메소드입니다.") #상속받는 자식 클래스에서 반드시 구현해야함.

class Car(Vehicle):
    def drive(self):
        return (f"승용차 {self.name}가 주행합니다.")
    
class Truck(Vehicle):
    def drive(self):
        return (f"트럭 {self.name}가 화물을 싣고 주행합니다.")
    
car = Car("car1")
truck = Truck("truck1")

root=Tk()
root.title("문제1")
root.geometry("400X300")

label=Label(root, text="버튼을 눌러보세요.")
label.pack()


button1=Button(root, text="자동차 주행")