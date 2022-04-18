def bubble_sort(index, arr):
    if index == 0:
        return arr
    for i in range(index-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return bubble_sort(index-1, arr)

arr = [9,6,2,12,11,9,3,7,100,99,98,97,123]
print(bubble_sort(len(arr), arr))
"""
=> bubble_sort: get the largest element and put it at the last index
"""