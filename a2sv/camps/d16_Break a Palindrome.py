class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        orderPal = []
        count = 0
        
        if len(palindrome) == 1:
            return ""
        
        mid = len(palindrome)//2 if len(palindrome)%2 == 0 else len(palindrome)//2 + 1
        
        while count < mid:
            if ord(palindrome[count]) != 97:
                break
            count += 1
        
        arr = [char for char in palindrome]
        if count < mid-1:
            arr[count] = "a"
        elif count == mid-1 and len(palindrome) % 2 == 0: 
            arr[count] = "a"
        else: 
            arr[-1] = "b"
        
        
        return ''.join(arr)
    
'''
a-97 
...
z-122
'''