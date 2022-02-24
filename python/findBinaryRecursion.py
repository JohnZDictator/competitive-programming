def findBinary(input, result):
    if input == 0:
        return result
    result = str(input%2) + result
    return findBinary(input//2, result)

if  __name__ == '__main__':
    input = int(input("Enter a number: "))
    print(findBinary(input, ''))