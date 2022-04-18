def printTable(i, n):
    if i > 10:
        return
    print("Product of", i, "and", n, "is", i*n)
    printTable(i+1, n)

printTable(1, 17)