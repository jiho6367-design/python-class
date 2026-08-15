#%%
class Cookie:
    pass
#%%
inst0 = Cookie()
inst1 = Cookie()

# %%
inst0.a = 0
inst1.a = 0
# %%
def add(inst,x):
    
    inst.a = inst.a + x
    return inst.a


print(add(inst0,3))
print(add(inst0,4))
print(add(inst1,3))
print(add(inst1,4))

# %%
class Cookie:
    pass

inst0 = Cookie()
inst1 = Cookie()

inst0.a = 0
inst1.a = 0
def add(inst,x):
    
    inst.a = inst.a + x
    return inst.a

# inst0.add = add
# inst1.add = add
# print(inst0.add(inst0,3))
# print(inst0.add(inst0,4))
# print(inst1.add(inst1,3))
# print(inst1.add(inst1,4))
# %%
Cookie.add = add
print(inst0.add(3))
print(inst0.add(4))
print(inst1.add(5))
print(inst1.add(6))

# %%
class Cookie:
    def add(self,x):
        
        self.a = self.a + x
        return self.a
inst0 = Cookie()
inst1 = Cookie()

inst0.a = 0
inst1.a = 0

print(inst0.add(3))
print(inst0.add(4))
print(inst1.add(5))
print(inst1.add(6))
# %%
class Calculator:
    def __init__(self) :
        self.result = 0
    def add(self,x):
        
        self.result += x
        return self.result
cal0 = Calculator()
cal1 = Calculator()
#%%

print(cal0.add(3))
print(cal0.add(4))
print(cal1.add(5))
print(cal1.add(6))
# %%
