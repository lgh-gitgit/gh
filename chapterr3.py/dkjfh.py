class Person:
    def greeting(self):
        print("안녕하세요")



class bogum(Person):
    def __init__(self, a):
        self.a = a

    def greeting(self):
        super().greeting()
        print(f"저의 이름은 이건희 이고 {self.a}입니다")
b = input()
bogum_1 = bogum(b)
bogum_1.greeting()