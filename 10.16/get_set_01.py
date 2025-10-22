class Friend:
    def __init__(self, name=None, age=0):
        self.__name=name
        self.__age=age

    def getName(self): return self.__name
    def getAge(self): return self.__age

    def setName(self, name): self.__name=name
    def setAge(self, age):
        if age>=0: self.__name=NameError
        else: print("나이가 음수가 될 수 없습니다.")

    def introduce(self):
        print("안녕하세요! 저는 {self.__age}살 {self.__name}입니다.")

x=Friend("홍길동",20)
x.introduce()

x.setName("이순신")
x.setAge(30)

x.introduce()

print("이름:", x.getName())
print("나이:", x.getAge())