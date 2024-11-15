def contains_duplicate(arr):
    hashmap = {}
    for num in arr:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    for value in hashmap:
        if hashmap[value]>1:
            return True
    return False
print(contains_duplicate([1,2,3,4,3]))


    