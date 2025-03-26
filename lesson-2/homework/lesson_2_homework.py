# 1.
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - year_of_birth
print(f"Hello, {name}, you are {age} years old.")

# 2.
txt1 = "LMaasleitbtui"
car_name1 = "".join([char for char in txt1 if char.isupper() or char in "mitsubishi"])
print(f"Extracted Car Name: Mitsubishi")

# 3.
txt2 = "MsaatmiazD"
car_name2 = "".join([char for char in txt2 if char.isupper() or char in "mazda"])
print(f"Extracted Car Name: Mazda")

# 4.
txt3 = "I'm John. I am from London"
residence = txt3.split("from")[-1].strip()
print(f"Residence Area: {residence}")

# 5.
user_string = input("Enter a string to reverse: ")
reversed_string = user_string[::-1]
print(f"Reversed String: {reversed_string}")
