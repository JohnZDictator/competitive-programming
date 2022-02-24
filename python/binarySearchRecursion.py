def binarySearch(nums, num, left, right):
    if right < 0 or left > len(nums)-1:
        return False
    mid = (left + right) // 2
    if int(nums[mid]) == num:
        return True
    elif int(nums[mid]) < num:
        left = mid+1
    elif int(nums[mid]) > num:
        right = mid-1
    
    return binarySearch(nums, num, left, right)

if __name__ == '__main__':
    nums = (input("Enter an array: ").split())
    num = int(input("Enter the number you are looking for: "))
    print(binarySearch(nums, num, 0, len(nums)-1))
