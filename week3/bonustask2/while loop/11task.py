element = int(input())
i = 0
a = 0

while element != 0:
    if a < element:
        i += 1
    a = element
    element = int(input())
    
print(i-1)
