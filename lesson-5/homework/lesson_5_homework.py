# 1.
def is_leap(year):
    """ Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 2.
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# 3.
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

if a % 2 == 0:
    start = a
else:
    start = a + 1

if start <= b:
    print(*range(start, b + 1, 2))
else:
    print("No even numbers in the range")


