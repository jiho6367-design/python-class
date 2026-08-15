result = 0
result2 = 0
def add(x):
    global result
    result += x
    return result
def add2(x):
    global result2
    result2 += x
    return result2


print(add(3))
print(add(4))
print(add2(5))
print(add2(6))
