def gcd2(a,b):
    if a<b:
        a,b = b,a 
    for i in range(1,b+1) :
        # print(f"{i=}")
        ra = a % i
        rb = b % i
        if ra == 0 and rb == 0 :
            tmp = i
    return tmp
    # else :
    #     for i in range(1,a+1) :
    #         ra = a % i
    #         rb = b % i
    #         if ra == 0 and rb == 0 :
    #             tmp = i
    #     return tmp

print(gcd2(50,125))   
     

