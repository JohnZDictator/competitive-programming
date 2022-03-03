def recursionA(n, counter):
    counter += 1

    return recursionA(n//2, counter) if n > 1 else counter

print(recursionA(8, 0))