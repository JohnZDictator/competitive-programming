def makeProductOne(arr, n):
    coins = 0
    zeros = 0
    negatives = 0 
    
    for idx in range(n):
        if arr[idx] >= 1:
            coins += arr[idx] - 1
        elif arr[idx] <= -1:
            coins += abs(arr[idx]) - 1
            negatives += 1
        elif arr[idx] == 0:
            zeros += 1
    
    if (negatives + zeros) % 2 == 0 or negatives % 2 == 0:
        return coins + zeros
    elif negatives % 2 == 1:
        return coins + zeros + 2 
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(makeProductOne(arr, n))
    