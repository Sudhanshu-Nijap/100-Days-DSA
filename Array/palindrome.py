def palindrome(string):
    rev_string = string[::-1]
    if rev_string == string:
        return 1
    else:
        return 0
        
print(palindrome("MOM"))

# Using 2 pointer
def palindrome(string):
    s = 0
    e = len(string)-1
    while s<e:
        if string[s] != string[e]:
            return False
        s+=1
        e-=1
    return True

print(palindrome("abcdcba"))
    