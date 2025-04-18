# File: math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# File: string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# File: geometry/__init__.py
# (Empty file, just needed for package structure)

# File: geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

# File: file_operations/__init__.py
# (Empty file, just needed for package structure)

# File: file_operations/file_reader.py
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# File: file_operations/file_writer.py
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

# Example usage in a main script (e.g., main.py)
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Test math_operations
print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
print(multiply(5, 3))  # Output: 15
print(divide(5, 3))  # Output: 1.666...

# Test string_utils
print(reverse_string("hello"))  # Output: olleh
print(count_vowels("hello"))  # Output: 2

# Test geometry.circle
print(calculate_area(5))  # Output: 78.539...
print(calculate_circumference(5))  # Output: 31.415...

# Test file_operations
write_file("test.txt", "Hello, World!")
print(read_file("test.txt"))  # Output: Hello, World!