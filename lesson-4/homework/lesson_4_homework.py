# Dictionary Exercises

# 1. Sort a Dictionary by Value
my_dict = {1: 10, 2: 30, 3: 20}
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending order:", sorted_dict_asc)
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending order:", sorted_dict_desc)

# 2. Add a Key to a Dictionary
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dict = {**dic1, **dic2, **dic3}
print(concatenated_dict)

# 4. Generate a Dictionary with Squares
n = 5
squares_dict = {x: x*x for x in range(1, n+1)}
print(squares_dict)

# 5. Dictionary of Squares (1 to 15)
squares_dict_15 = {x: x*x for x in range(1, 16)}
print(squares_dict_15)

# Set Exercises

# 1. Create a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Iterate Over a Set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# 4. Remove Item(s) from a Set
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)

# 5. Remove an Item if Present in the Set
my_set = {1, 2, 3, 4}
item_to_remove = 3
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
print(my_set)