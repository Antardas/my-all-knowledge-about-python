
class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num


n1 = Num(1)
n2 = Num(2)

print(n1)
