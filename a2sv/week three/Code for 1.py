n, start, end = map(int, input().split())

def countOnes(bits, start, end):
    counter = 0
    while start <= end:
        if bits[start-1] == '1':
            counter += 1
        start += 1
    return counter

def toBit(n):
    if n <= 1:
        return 1
    
    return str(n%2) + str(toBit(n//2))

def reflector(bits):
    return str(bits[1:]) + bits

bits = toBit(n)
print(type(bits))
refBit = reflector(bits)
print(type(refBit))
print(len(bits))
print(len(refBit))
print(countOnes(refBit, start, end))
    
    

# n, start, end = map(int, input().split())

# def countOnes(bits, start, end):
#     counter = 0
#     while start <= end:
#         if bits[start-1] == '1':
#             counter += 1
#         if start < end and bits[end-1] == '1':
#             counter += 1
#         start += 1
#         end -= 1
#     return counter

# def toBit(n):
#     if n == 1:
#         return 1
    
#     return str(toBit(n//2)) + str(n%2) + str(toBit(n//2))
    
# bits = toBit(n)
# print(bits)
# print(countOnes(bits, start, end))
    
    
