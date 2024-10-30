# Multiply 2 numbers with "+" operator 

def multiplication(n1,n2):
    sum = 0
    for i in range(0,n2):
        sum = sum + n1
    return sum
        
print(multiplication(3,2))
