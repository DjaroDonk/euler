the_list = []
for i in range(0,1000):
    if (i%3==0) or (i%5==0):
        the_list.append(i)
print(sum(the_list))
