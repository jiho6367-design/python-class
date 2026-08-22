class FourCal :
    def __init__(self,x,y) :
        self.x = x
        self.y = y 
    def __repr__(self):
          return f"FourCal({self.x}, {self.y})"
    def add(self):
        return self.x + self.y
    def mul(self):
            return self.x * self.y
    def sub(self):
            return self.x - self.y
    def div(self):
            return self.x / self.y   

a = FourCal(4,2)
#a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# b = FourCal()
# b.setdata(6,3)
# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())

li = [FourCal(4,2) for i in range(0,100)]