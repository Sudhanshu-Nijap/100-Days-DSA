def pattern1(n):
    for row in range(1,n+1):
        for col in range(row):
            print("*",end=" ")
        print()
pattern1(5)

def pattern2(n):
    for row in range(1,n+1):
        for col in range(row):
            print(col+1,end=" ")
        print()
pattern2(5)

def pattern3(n):
    for row in range(n,0,-1):
        for col in range(row-1):
            print(" ",end="")
        print()
        
pattern3(5)