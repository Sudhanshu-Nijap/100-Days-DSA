def string_count(s):
    hashmap = {}
    output = ""
    for char in s:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1
    for key,value in hashmap.items():
        output += "{}{}".format(key,value)
    return output
print(string_count("abbac"))