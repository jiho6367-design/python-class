import random
#nums = random.sample("0123456789",3)
nums = random.sample(range(0,10),3)
nums = [str(x) for x in nums]

count = 0

while True :
    guess = input("세 자리 숫자를 입력하세요: ")
    count += 1
    ball = 0
    strike = 0
    for i,v in enumerate(guess) :
        if v == nums[i] :
            strike += 1
        elif v in nums :
            ball += 1
    print(f"{strike=},{ball=}") 

    if strike == 3 :
        print(f"{count=} END")   
        break




    