class Student:
    def add(self):
        x = 50
        y = 24
        return x+y
    def sub(self):
        v = 10
        b = 5
        return v-b
    def mul(self):
        g = 10
        h = 5
        return g*h

Info = Student()
print(Info.add())
print(Info.sub())
print(Info.mul())