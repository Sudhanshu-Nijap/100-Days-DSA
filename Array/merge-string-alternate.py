def mergeAlternately(word1,word2):
        A,B = len(word1),len(word2)
        a,b = 0,0
        s = []
        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a+=1
                word = 2
            else:
                s.append(word2[b])
                b+=1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a+=1

        while b < B:
            s.append(word2[b])
            b+=1
        
        return ''.join(s)

word1 = 'abc'
word2 = 'pqrst'
print(mergeAlternately(word1,word2))  # Output: apbqcrst

        