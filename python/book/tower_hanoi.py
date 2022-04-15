def towerOfHanoi(source, destination, extra, n):
    if n <= 0:
        return
    
    towerOfHanoi(source, extra, destination, n-1)
    print("Move Disk:", n, "from:", source, "to:", destination)
    towerOfHanoi(extra, destination, source, n-1)
    
if __name__ == '__main__':
    source, destination, extra = map(str, input().split())
    n = int(input())

    towerOfHanoi(source, destination, extra, n)