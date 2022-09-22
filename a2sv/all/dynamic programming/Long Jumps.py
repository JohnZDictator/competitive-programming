t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  dp = [0] * (n+1)
  max_score = 0
  for i in range(n-1, -1, -1):
    dp[i] = arr[i] + (dp[-1] if i + arr[i] >= n else dp[i+arr[i]]) 
    max_score = max(max_score, dp[i])
  print(max_score)
