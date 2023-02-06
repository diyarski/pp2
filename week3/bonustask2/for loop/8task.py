n = int(input())
sum = 0
res = 1

for i in range(1, n+1):
    res *= i
    sum += res
    
print(sum)
