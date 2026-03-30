import math
class erankyun:
    def __init__(self, a):
        self.a = a

    def paragic(self):
        return self.a * 3

    def makeres(self):
        return (math.sqrt(3) / 4) * (self.a ** 2)

a = int(input())
n = erankyun(a)
print(n.paragic())
print(n.makeres())