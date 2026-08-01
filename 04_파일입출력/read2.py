# f= open("새파일.txt",'r',encoding="utf-8")
# data=f.read()
# print(data)
# f.close()

# f= open("새파일.txt",'r',encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

f= open("새파일.txt",'a',encoding="utf-8")
for i in range(11,20):
    data = f"{i}번째 줄입니다 .\n"
    f.write(data)
f.close()