def probC(x, m):
    left = 0
    right = len(x)-1
    best = -1
    
    while left <= right:
        mid = left + (right-left)//2
        if m < x[mid]:
            right = mid-1
        else:
            left = mid+1
            best = mid
    return best+1

if __name__ == '__main__':
    n = int(input())
    
    x = input().split()
    for i in range(n):
        x[i] = int(x[i])
    x.sort()
    
    q = int(input())
    
    for i in range(q):
        m = int(input())
        print(probC(x, m))