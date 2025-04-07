# 1. is_prime(n) Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))  # Output: False
print(is_prime(7))  # Output: True

# 2. digit_sum(k) Function
def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total

print(digit_sum(24))   # Output: 6
print(digit_sum(502))  # Output: 7

# 3. Power of Two Function
def power_of_two(n):
    result = []
    for i in range(n):
        result.append(2 ** i)
    return result

print(power_of_two(10))  # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]