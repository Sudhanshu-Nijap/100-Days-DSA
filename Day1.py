def binarytodecimal(num):
    decimal,i = 0,0
    while num!=0:
        rem = num % 10
        decimal = decimal + rem * pow(2,i)
        num = num//10
        i = i+1
    
    return decimal

print(binarytodecimal(1101))

def decimaltobinary(num):
    if num >=1:
        decimaltobinary(num//2)
    print(num % 2,end=" ")

decimaltobinary(13)
