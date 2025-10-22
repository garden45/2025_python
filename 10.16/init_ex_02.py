class Counter:


    def increment(self):
        self.count+=1

    def get(self):
        return self.count
    

a=Counter()
b=Counter()

a.count=0
b.count=0

a.increment()
a.increment()
b.increment()

print("a의 count:", a.get())
print("b의 count:", b.get())