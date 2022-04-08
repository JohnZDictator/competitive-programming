def nth_pow(b, n):
    if n == 0:
        return 1
    if b == 1:
        return b

    return b * nth_pow(b, n-1)

print(nth_pow(3, 4))
print(nth_pow(1, 1000))