'''
The classic fibonacci recursive call has:
    - O(2^n) - time complexity &
    - O(n) - space complexity
We can use Dynamic programming to make our call efficient:
    - O(n) - time complexity &
    - O(n) - space complexity as we only n number of function call stack 
'''
# def fib(n):
#     if n <= 2: return 1
#     return fib(n-1) + fib(n-2)

# def fib(n, memo = {}):
#     if n in memo: return memo[n]

#     if n <= 2: return 1

#     memo[n] = fib(n-1, memo) + fib(n-2, memo)

#     return memo[n] 

print(fib(50))