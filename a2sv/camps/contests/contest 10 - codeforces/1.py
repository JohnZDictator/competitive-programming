def red_blue_shuffle(red, blue, n):
    if red == blue:
        return "EQUAL"
    
    red_count = 0
    blue_count = 0
    for idx in range(n):
        if int(red[idx]) > int(blue[idx]):
            red_count += 1
        elif int(blue[idx]) > int(red[idx]):
            blue_count += 1
    
    if red_count > blue_count:
        return "RED"
    elif blue_count > red_count:
        return "BLUE"
    elif blue_count == red_count:
        return "EQUAL"

if __name__ == '__main__':
    test_cases = int(input())
    counter = 0
    while counter < test_cases:
        n = int(input())
        red = str(input())
        blue = str(input())
        
        print(red_blue_shuffle(red, blue, n))
        counter += 1

