# calculating it by brute force would be inefficient

# Going to use the prime factor function from file 3

###### COPY PASTE from 3.py
def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def biggestdivisor(num):
    if isprime(num):
        return(num)
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                b=i
        return(b)
def findfactors(num):
    #print("finding factors of " + str(num))
    factors = []
    if isprime(num):
        factors.append(num)
        return(factors)
    else:
        for f in findfactors(biggestdivisor(num)):
            factors.append(f)
        for f in findfactors(int(num/biggestdivisor(num))):
            factors.append(f)
    return(sorted(factors))
#####################

def countitems(the_list):
    the_dic = {}
    for ob in the_list:
        the_dic.setdefault(ob,0)
        the_dic[ob]+=1
    return(the_dic)

def lcm(thelist):
    thefactors={}
    for i in thelist:
        nums = countitems(findfactors(i))
        for j in nums.keys():
            thefactors.setdefault(j,nums[j])
            if thefactors[j]<nums[j]:
                thefactors[j]=nums[j]
    return(thefactors)

fac20 = lcm([*range(1,20)])

endnum = 1
for i in fac20.keys():
    endnum*=i**fac20[i]
print(endnum)
