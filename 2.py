the_list = [1,2]
while the_list[-1]<4000000:
    the_list.append(the_list[-1]+the_list[-2])
del(the_list[-1])
evens = []
for i in the_list:
    if i%2==0:
        evens.append(i)
print(sum(evens))
