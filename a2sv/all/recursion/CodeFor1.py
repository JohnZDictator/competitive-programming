 def codeFor1(n, l, r):
    if n < 2:
        return n 
        
    arr = {}
    count = 1
    m = n
    while m > 0:
        m //= 2
        count *= 2
    
    while n > 0:
        arr[count] = n%2
        n = n // 2
        count //= 2
    
    ones = 0
    for i in range(l, r+1):
        if i % 2 == 1 and arr[2] == 1:
            ones += 1
        else:
            for j in range(1, len(arr)):
                num = i - (2**j)
                power = 2**(j+1) 
                if (num == 0 or num % power == 0) and arr[power] == 1:
                    ones += 1
                    break
    return ones

if __name__ == '__main__':
    n, l, r = map(int, input().split())
    print(codeFor1(n, l, r))