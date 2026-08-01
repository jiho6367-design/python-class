sum1 = 0
sum2 = 0
sum3 = 0
for i in range(1,1000):
   if(i%3==0):
    sum1 += i
for j in range(1,1000):
   if(j%5==0):
    sum2 += j
for n in range(1,1000):
    if(n%15==0):
        sum3 += n
result = sum1 + sum2 - sum3
print(f"{sum1=},{sum2=},{sum3=}")

print(result)



