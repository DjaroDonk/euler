def ispalindrome(num):
    if list(str(num)) == list(str(num))[::-1]:
        return(True)
    else:
        return(False)
lp = 0
for i in range(100,1000):
    for j in range(100,1000):
        if ispalindrome(i*j):
            if i*j>lp:
                lp=i*j

print(lp)
