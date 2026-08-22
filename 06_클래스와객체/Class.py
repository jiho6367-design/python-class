result = 0
result2 = 0
def add(x) :
    global result
    result = result + x
    return result

def add2(x) :
    global result2
    result2 = result2 + x
    return result2

print(add(2))
print(add(3))
print(add2(4))
print(add2(5))

class Cookie :

    pass
ck0 = Cookie()
ck1 = Cookie()

ck0.result = 0
ck1.result = 0


def add(inst,x):
    inst.result += x
    return inst.result
print(add(ck0,3))
print(add(ck0,2))
print(add(ck1,3))
print(add(ck1,3))




class Cookie :
    def add(self,x):
        self.result += x
        return self.result
    
ck0 = Cookie()
ck1 = Cookie()
ck2 = Cookie()

ck0.result = 0
ck1.result = 0
ck2.result = 0 
print(ck0.add(3))
print(ck0.add(2))
print(ck1.add(3))
print(ck1.add(3))

print(Cookie.add(ck2,4))









