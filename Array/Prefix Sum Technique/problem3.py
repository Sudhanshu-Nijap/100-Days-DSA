#left subarray == right subarray (find pivot index)
def pivot_index(arr):
    prefix_sum = 0
    left_sum = 0
    for i in arr:
        prefix_sum+=i
    for j,num in enumerate(arr):
        right_sum = prefix_sum - left_sum - num
        if right_sum == left_sum:
            return j
        left_sum+=num
    return -1
print(pivot_index([1, 7, 3, 6, 5, 6]))