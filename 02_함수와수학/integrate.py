N = 99999999999999
def square(x):
    return x**2
def integrate(func,a,b) : 
    sum = 0
    for i in range(0,N):
        area = func(a+i*(b-a)/N)*((b-a)/N)
        sum += area
    return sum

print(f"{integrate(square,1,2)=},{7/3}")