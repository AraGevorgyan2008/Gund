import math
class Gund:
    def __init__(self,r):
        self.r = r
    def S(self):
        return 4 * math.pi * self.r**2
    def V(self):
        return 4/3 * math.pi * self.r**3
    def L(self):
        return 2 * math.pi * self.r
