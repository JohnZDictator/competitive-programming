def summation(input):
    if input <= 1:
        return 1
    return input + summation(input-1)

if __name__ == '__main__':
    input = int(input("Enter a number: "))
    print(summation(input))