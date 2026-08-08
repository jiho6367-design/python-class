import sys
from pathlib import Path

memo_path = Path(__file__).with_name("memo.txt")

print(sys.argv)

if sys.argv[1] == '-a' :
    with open(memo_path,'a',encoding='utf-8') as f :
        f.write(sys.argv[2])
        f.write("\n")
elif sys.argv[1] == '-v' :
    with open(memo_path,'r',encoding='utf-8') as f :
        data = f.readlines()
        for i in data :
            print(i,end="")
