#%%
a=range(1,5)
print(a)

# %%
for i in a :
    print(i)

# %%
sorted(a)
# %%
li = list(range(1,6))
# %%
new_li=[35,675,13,96,11]

for i in range(0,len(li)):
    new_li[i]=li[i]*2
print(new_li) 
    

# %%
li = list(range(1,6))
new_li=[]
for i in range(0,len(li)):
    a=li[i]*2
    new_li.append(a)
print(new_li)

# %%
li = list(range(1,6))
new_li=[]
for v in li:
    new_li.append((v)*2)
print(new_li)
# %%
li = list(range(1,6))
list(map(lambda x:x*2,li))

# %%
li = list(range(1,6))
def my_map(func,it):
    new_li=[]
    for v in it:
        new_li.append(func(v))
    return new_li


        

my_map(lambda x : x*2, li)        


# %%
li = list(range(1,6))
new_li=[v*2 for v in li]
# %%
li = list(range(1,6))
new_li=[]
for v in li:
    new_li.append(v*2)
print(new_li)
# %%
li = list(range(1,6))
new_li=map(lambda x : x*2,li)
print(list(new_li))
# %%
def double(x):
    print(f"double:{x}")
    return x*2

li = list(range(1,6))
new_li=map(double,li)
print(list(new_li))
# %%
li = [4,9,6,2,7]
def my_filter(func,it):
    new_li=[]
    for v in it:
        if func(v):
            new_li.append(v)

    return new_li
print(my_filter(lambda x : x//2 !=0,li))



# %%
