def filter_primes(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_primes(numbers))
