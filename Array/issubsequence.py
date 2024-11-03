def isSubsequence(s: str, t: str) -> bool:
        S,T = len(s),len(t)
        if s == '':
            return True
        if S>T:
            return False
        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j+=1
        return False

print(isSubsequence('abc','ahbqwec'))