# 1. Create and Access List Elements
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print(f"Third fruit: {fruits[2]}")

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(f"Concatenated List: {concatenated_list}")

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
extracted = [numbers[0], numbers[len(numbers) // 2], numbers[-1]]
print(f"Extracted Elements: {extracted}")

# 4. Convert List to Tuple
movies = ["Inception", "Interstellar", "Matrix", "Avatar", "Titanic"]
movies_tuple = tuple(movies)
print(f"Movies Tuple: {movies_tuple}")

# 5. Check Element in a List
cities = ["Paris", "London", "New York", "Tokyo"]
is_paris_present = "Paris" in cities
print(f"Is Paris in the list? {is_paris_present}")

# 6. Duplicate a List Without Using Loops
numbers = [1, 2, 3]
duplicated_list = numbers * 2
print(f"Duplicated List: {duplicated_list}")

# 7. Swap First and Last Elements of a List
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"Swapped List: {numbers}")

# 8. Slice a Tuple
numbers_tuple = tuple(range(1, 11))
sliced_tuple = numbers_tuple[3:8]
print(f"Sliced Tuple: {sliced_tuple}")

# 9. Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print(f"Blue appears {count_blue} times")

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
lion_index = animals.index("lion")
print(f"Index of 'lion': {lion_index}")

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(f"Merged Tuple: {merged_tuple}")

# 12. Find the Length of a List and Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
print(f"Length of list: {len(my_list)}, Length of tuple: {len(my_tuple)}")

# 13. Convert Tuple to List
numbers_tuple = (10, 20, 30, 40, 50)
converted_list = list(numbers_tuple)
print(f"Converted List: {converted_list}")

# 14. Find Maximum and Minimum in a Tuple
numbers_tuple = (5, 10, 3, 8, 2)
max_value = max(numbers_tuple)
min_value = min(numbers_tuple)
print(f"Maximum: {max_value}, Minimum: {min_value}")

# 15. Reverse a Tuple
words_tuple = ("one", "two", "three", "four", "five")
reversed_tuple = words_tuple[::-1]
print(f"Reversed Tuple: {reversed_tuple}")
