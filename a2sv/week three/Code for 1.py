n = int(input())
start = int(input())
end = int(input())

def countOnes(bits, start, end):
    counter = 0
    while start <= end:
        if bits[start-1] == '1':
            counter += 1
        start += 1
    return counter

def toBit(n):
    if n == 1:
        return 1
    
    return str(toBit(n//2)) + str(n%2) + str(toBit(n//2))
    
bits = toBit(n)
print(bits)
print(countOnes(bits, start, end))
    
    
