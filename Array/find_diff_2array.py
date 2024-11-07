def samediff(num1,num2):
    num1 = set(num1)
    num2 = set(num2)
    diff1 = num1.difference(num2)
    diff2 = num2.difference(num1)
    return [list(diff1),list(diff2)]

print(samediff([1,2,3],[2,4,6]))

def find_diff(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    ans = [[],[]]
    for i in arr1:
        if i not in arr2:
            ans[0].append(i)
    for j in arr2:
        if j not in arr1:
            ans[1].append(j)
    return ans

print(find_diff([1,2,3],[2,4,6]))
        