def fib(num):
    if num <= 1:
        return 1
    
    return fib(num-1) + fib(num-2)

if __name__ == '__main__':
    input = int(input("Enter a number: "))
    print(fib(input))