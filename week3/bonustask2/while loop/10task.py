element = int(input())
i = 0

while element != 0:
    if element % 2 == 0:
        i += 1
    element = int(input())
print(i)
