class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id=stu_id
        self.name=name

    def show_info(self):
        print(f"학번: {self.stu_id}, 이름: {self.name}")

x=DSstudent(20251229, "한정원")
x.show_info()