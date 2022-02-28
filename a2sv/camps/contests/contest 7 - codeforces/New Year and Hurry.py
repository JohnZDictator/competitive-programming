def probA(n,k):
    total = 4*60
    left = total - k
    counter = 1
    
    while left > 0:
        left -= counter*5
        if left >= 0:
            counter += 1
    if counter > n:
        return n
    return counter-1

if __name__=='__main__':
    n, k = map(int, input().split())
    print(probA(n, k))