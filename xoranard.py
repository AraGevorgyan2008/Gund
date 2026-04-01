class Xoranard:
    def __init__(self,koxm):
        self.koxm=koxm
    def caval(self):
        return self.koxm**3
    def makeres(self):
        return 6*self.koxm**2
    def ankyunagic(self):
        return self.koxm*3**(1/2)
    def ankyunagcayin_hatuyti_makeres(self):
        return self.koxm**2*2**(1/2)
koxm=int(input())
x=Xoranard(koxm)
print(x.caval())
print(x.makeres())
print(x.ankyunagic())


print(x.ankyunagcayin_hatuyti_makeres())