def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

x = int(input("Enter n: "))
print(fac(x**2))