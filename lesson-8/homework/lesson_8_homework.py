# 1. Handle ZeroDivisionError
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# 2. Handle ValueError for invalid integer input
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Please enter a valid integer")

# 3. Handle FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")

# 4. Handle TypeError for non-numerical inputs
try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = int(num1) + int(num2)
except TypeError:
    print("Error: Inputs must be numerical")

# 5. Handle PermissionError
try:
    with open("file.txt", "w") as file:
        file.write("Test")
except PermissionError:
    print("Error: Permission denied to access the file")

# 6. Handle IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range")

# 7. Handle KeyboardInterrupt
try:
    num = input("Enter a number (or press Ctrl+C to cancel): ")
except KeyboardInterrupt:
    print("Error: Operation cancelled by user")

# 8. Handle ArithmeticError
try:
    result = 10 ** 1000000  # This may cause an overflow
except ArithmeticError:
    print("Error: Arithmetic error occurred")

# 9. Handle UnicodeDecodeError
try:
    with open("file.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Encoding issue while reading the file")

# 10. Handle AttributeError
try:
    my_list = [1, 2, 3]
    my_list.append_attribute(4)  # Incorrect method
except AttributeError:
    print("Error: Attribute does not exist")


# 1. Read an entire text file
with open("file.txt", "r") as file:
    content = file.read()
print(content)

# 2. Read first n lines of a file
n = int(input("Enter number of lines to read: "))
with open("file.txt", "r") as file:
    for i in range(n):
        line = file.readline().strip()
        if not line:
            break
        print(line)

# 3. Append text to a file and display the text
text = input("Enter text to append: ")
with open("file.txt", "a") as file:
    file.write(text + "\n")
with open("file.txt", "r") as file:
    print(file.read())

# 4. Read last n lines of a file
n = int(input("Enter number of lines to read: "))
with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())

# 5. Read a file line by line and store it into a list
lines_list = []
with open("file.txt", "r") as file:
    lines_list = file.readlines()
    lines_list = [line.strip() for line in lines_list]
print(lines_list)

# 6. Read a file line by line and store it into a variable
content = ""
with open("file.txt", "r") as file:
    for line in file:
        content += line
print(content)

# 7. Read a file line by line and store it into an array
lines_array = []
with open("file.txt", "r") as file:
    for line in file:
        lines_array.append(line.strip())
print(lines_array)

# 8. Find the longest words
with open("file.txt", "r") as file:
    words = file.read().split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
print(longest_words)

# 9. Count the number of lines in a text file
with open("file.txt", "r") as file:
    line_count = sum(1 for line in file)
print(line_count)

# 10. Count the frequency of words in a file
word_freq = {}
with open("file.txt", "r") as file:
    words = file.read().split()
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)

# 11. Get the file size of a plain file
import os
file_size = os.path.getsize("file.txt")
print(file_size)

# 12. Write a list to a file
my_list = ["line1", "line2", "line3"]
with open("output.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

# 13. Copy the contents of a file to another file
with open("source.txt", "r") as source, open("destination.txt", "w") as dest:
    dest.write(source.read())

# 14. Combine each line from the first file with the corresponding line in the second file
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    for line1, line2 in zip(lines1, lines2):
        print(line1.strip() + " " + line2.strip())

# 15. Read a random line from a file
import random
with open("file.txt", "r") as file:
    lines = file.readlines()
    random_line = random.choice(lines).strip()
print(random_line)

# 16. Assess if a file is closed or not
file = open("file.txt", "r")
print(file.closed)  # False
file.close()
print(file.closed)  # True

# 17. Remove newline characters from a file
with open("file.txt", "r") as file:
    lines = file.readlines()
with open("file.txt", "w") as file:
    for line in lines:
        file.write(line.rstrip("\n"))

# 18. Count the number of words in a given text file
with open("file.txt", "r") as file:
    content = file.read()
    words = content.replace(",", " ").split()
    word_count = len(words)
print(word_count)

# 19. Extract characters from various text files and put them into a list
import glob
characters = []
files = glob.glob("*.txt")
for file_name in files:
    with open(file_name, "r") as file:
        content = file.read()
        characters.extend(list(content))
print(characters)

# 20. Generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")

# 21. Create a file where all letters of the English alphabet are listed with a specified number of letters on each line
import string
letters = string.ascii_lowercase
n = int(input("Enter number of letters per line: "))
with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(" ".join(letters[i:i + n]) + "\n")