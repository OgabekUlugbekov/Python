# 1. Modify String with Underscores
def modify_string(txt):
    result = ""
    vowels = "aeiouAEIOU"
    for i in range(len(txt)):
        if i > 0 and txt[i] in vowels and txt[i-1] not in vowels:
            result += "_" + txt[i]
        else:
            result += txt[i]
    return result

print(modify_string("hello"))         # Output: hel_lo
print(modify_string("assalom"))      # Output: ass_alom
print(modify_string("abcabcdeabcdefabcdefg"))  # Output: abc_abcd_abcdeab_cde_abcdfg

# 2. Integer Squares Exercise
n = int(input())
for i in range(1, n + 1):
    print(i * i)

# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print the following pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# Exercise 4: Print multiplication table of a given number
n = int(input())
for i in range(1, 11):
    print(n * i)

# Exercise 5: Display numbers from a list using a loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    print(num)

# Exercise 6: Count total number of digits in a number
n = int(input())
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# Exercise 7: Print reverse number pattern
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8: Print in reverse order using a loop
list1 = [1, 2, 3, 4, 5]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)

# Exercise 10: Display message "Done" after successful loop execution
for i in range(5):
    print(i)
print("Done")

# Exercise 11: Print all prime numbers within a range
start = 25
end = 50
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12: Display Fibonacci series up to 10 terms
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

# Exercise 13: Find the factorial of a given number
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))

list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))  # Output: [1, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  # Output: [2, 5]