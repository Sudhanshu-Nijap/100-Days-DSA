import math
def primeornot(num):
    if num<2:
        return 0
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return 0
    return 1
print(primeornot(12))