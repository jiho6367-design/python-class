class Mul:
    def __init__(self,m):
        self.m = m

    def mul(self,n):
        return self.m * n
ins3 = Mul(3)
print("namespace : ",vars(ins3))
print(f"{ins3.m=}")
print(ins3.mul(10))
ins5 = Mul(5)
print(f"{ins5.m=}")
print(ins5.mul(10))

