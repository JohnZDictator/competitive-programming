n, m, a = map(int, input().split())

flagstone_rows = 0
flagstone_columns = 0

if n % a == 0 :
    flagstone_rows = n / a
else:
    flagstone_rows = (n // a) + 1 

if m % a == 0 :
    flagstone_columns = m / a
else : 
    flagstone_columns = ( m // a ) + 1    

print(int(flagstone_rows * flagstone_columns))
