# 이 장에서는 클래스에 대해 배웁니다.

class Student:
    def __init__(self, name):
        self.name = name

    def sayGoodLuck(self):
        print(f"{self.name}: Good Luck!")

uneon = Student('uneon')
uneon.sayGoodLuck()