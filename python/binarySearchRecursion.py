def binarySearch(nums, num, left, right):
    if left > len(nums)-1 or right < 0:
        return False 
    
    mid = left + (right-left)//2
    if int(nums[mid]) < num:
        return binarySearch(nums, num, mid+1, right)
    elif int(nums[mid]) == num:
        return mid
    
    return binarySearch(nums, num, left, mid-1) 


# def binarySearch(nums, num):
#     left = 0
#     right = len(nums)-1

#     while left <= right:
#         mid = left + (right-left)//2

#         if int(nums[mid]) < num:
#             left = mid+1
#         elif int(nums[mid]) == num:
#             return mid
#         else:
#             right = mid-1
#     return -1

if __name__ == '__main__':
    nums = (input("Enter an array: ").split())
    num = int(input("Enter the number you are looking for: "))
    print(binarySearch(nums, num, 0, len(nums)-1))
    # print(binarySearch(nums, num))
