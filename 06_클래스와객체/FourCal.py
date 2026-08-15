#%%
class FourCal :
    def __init__(self,x,y) :
        self.a, self.b = x,y
    def add(self) :
        self.c = 100
        result = self.a + self.b
        return result
    def sub(self) :
        result = self.a - self.b
        return result
    def mul(self) :
        result = self.a * self.b
        return result
    def div(self) :
        result = self.a / self.b
        return result
f0 = FourCal(3,4)
f1 = FourCal(5,6)

print(f1.add())
print(f1.sub())
print(f1.mul())
print(f1.div())
# %%
