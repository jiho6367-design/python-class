li = [1,2,3,4]
# f1 = filter(lambda x : x % 2 == 0,li)
# print(list(f1))
f2 = [ x for x in li if x % 2 == 0]
print(f2)