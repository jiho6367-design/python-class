
def add_many(*arg) : 
    b=0
    for i in arg :
        b=b+i
    return b
 

a= add_many(1,2,3)
print(a)