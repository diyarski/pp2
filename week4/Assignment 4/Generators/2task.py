def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

even_numbers = even_generator(n)

print(*even_numbers, sep=", ")
