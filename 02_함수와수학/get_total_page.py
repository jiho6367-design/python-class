def get_total_page(m,n):
    #m/n 나머지가 있으면 +1 없으면 그냥 
    page1 = m//n
    if(m%n != 0):
        page1 += 1
    return (page1)

print(get_total_page(21,10))