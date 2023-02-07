max = 0
element = -1
i = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        i += 1
print(i)
