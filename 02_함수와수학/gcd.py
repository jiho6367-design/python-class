#import math
#print(math.gcd(125,50))

def gcd(a,b):
    if a < b : 
        a , b = b , a
    while True:
        print(f"{a},{b}")
        r = a%b
        a , b = b , r 
        if r == 0 :
            return a
        
       
print(gcd(125,50)) 


  

