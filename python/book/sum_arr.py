def summ(arr, n):
    if n == 0:
        return arr[n]    
    
    arr[n] = arr[n] + summ(arr, n-1)
    return arr[n]

print(summ([1,2,3,4,5,6], 5))