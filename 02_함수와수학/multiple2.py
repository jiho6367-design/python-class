sum1 = 0
sum2 = 0
sum3 = 0
for i in range(1,1000) :
    if(i%3==0):
        sum1 += i
    if(i%5==0):
        sum2 += i
    if(i%15==0):
        sum3 += i
result = sum1 + sum2 - sum3
print(f"{sum1=},{sum2=},{sum3=}")

print(result)



