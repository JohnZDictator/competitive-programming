def palindrome(input):
    if len(input) <= 1:
        return True
    if input[0] == input[-1]:
        return palindrome(input[1:len(input)-1])
    return False

if __name__ == "__main__":
    input = str(input("Enter a string: "))
    print(palindrome(input))