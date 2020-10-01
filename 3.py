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

print(findfactors(600851475143)[-1])
