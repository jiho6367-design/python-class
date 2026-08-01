# f = open("새파일.txt",'r',encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line :
#       break  
#     print(line, end="")

# f.close()

# while True:
#    data = input()
#    if not data : break
#    print(data)

# f = open("새파일.txt",'r',encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)

# f.close()

from pathlib import Path

# 이 파일(read.py)이 있는 폴더의 새파일.txt를 찾는다.
file_path = Path(__file__).parent / "새파일.txt"
f = open(file_path, 'r', encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)

f.close()
