n, k = map(int, input().split())

a = input().split()
t = input().split()

window_size = k
max_theorm_window = 0

left = 0
right = window_size
while right < len(n):
    total_theorem = sum(a[left:right+1])
    max_theorem = max(max_theorem, total_theorem)
    left += 1
    right += 1
max_theorem



