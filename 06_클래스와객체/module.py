import MoreFourCal

print(*vars(MoreFourCal), sep="\n")

calc0 = MoreFourCal.FourCal(4,2)

print(calc0.add())
print(calc0.mul())
print(calc0.sub())
print(calc0.div())