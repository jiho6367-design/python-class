a = [15000,25000,1000,5000,35000]

def my_min(data):
    m=data[0]
    m_i=0

    for i, d in enumerate(data): 
        if m > d :
            m=d
            m_i=i  
    print(f"my min={m_i},{m}")       
    return m_i, m

def my_max(data):
    m=data[0]
    m_i=0

    for i, d in enumerate(data): 
        if m < d :
            m=d
            m_i=i  
    print(f"my max={m_i},{m}")       
    return m_i, m
     
def my_sort(data,comp):
    for x in range(len(data)) :
        tmp=data[x] 
        i, data[x] = comp(data[x:])
        data[i+x]=tmp
    print(data)

my_sort(a,my_min)
my_sort(a,my_max)
# print(a)    

a= [99,34,315264375,78,2]
# b= sorted(a,reverse=True)
# print(b)
a.sort()
print(a)
a=[(34,1),(565,76),(1,2),(1,1)]
print(sorted(a,key= lambda x : x[1]))

