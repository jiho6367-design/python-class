import sys 
print(*sys.path, sep ='\n')
#sys.path.append(R"C:\Users\USER\파이썬수업\06_클래스와객체")
import MoreFourCal as M
#from MoreFourCal import FourCal

print(*vars(M), sep="\n")
calc0 = M.FourCal(4,2)


print(calc0.add())
print(calc0.mul())
print(calc0.sub())
print(calc0.div())