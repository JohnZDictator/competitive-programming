def reverseString(input):
    if len(input) == 1:
        return input
    return reverseString(input[1:]) + input[0]


if __name__ == '__main__':
    input = str(input("Enter a string: "))
    print(reverseString(input))


