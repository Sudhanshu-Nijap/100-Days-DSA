#count subarrays with a given sum (target)
def sum_of_k(arr,target):
    prefix_sum = 0
    hashmap = {}
    result = 0
    for i in arr:
        prefix_sum += i
        if prefix_sum - target in hashmap:
            result += hashmap[prefix_sum - target]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1
    return result
print(sum_of_k([1,4,3],5))