# f = open("새파일.txt",'w',encoding="utf-8")
# for i in range(1,11):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)
# f.close()

# for i in range(1,11):
#     data = f"{i}번째 줄입니다."
#     print(data)

kim ="김"
print(hex(ord(kim)))
b = kim.encode("utf-8")
c = [hex(int(i)) for i in b]
print(c)
print(b)