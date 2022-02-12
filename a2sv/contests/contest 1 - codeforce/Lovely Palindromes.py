n = str(input())

arr = [n]
counter = len(n)-1
while counter >= 0:
    arr.append(n[counter])
    counter -= 1
print(int(''.join(arr)))