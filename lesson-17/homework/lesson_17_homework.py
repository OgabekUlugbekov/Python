import pandas as pd
import numpy as np

# Homework 1
# 1. Create a DataFrame
data = {"First Name": ["Alice", "Bob", "Charlie", "David"], "Age": [25, 30, 35, 40],
        "City": ["New York", "San Francisco", "Los Angeles", "Chicago"]}
df = pd.DataFrame(data)

# 2. Rename column names
df = df.rename(columns={"First Name": "first_name", "Age": "age"})

# 3. Find the mean age of the DataFrame
mean_age = df["age"].mean()
print(f"Mean age: {mean_age}")

# 4. Select and print only the 'Name' and 'City' columns
print(df[["first_name", "City"]])

# 5. Add a new column 'Salary' with random salary values
df["Salary"] = np.random.randint(30000, 100000, size=len(df))

# 6. Display summary statistics of the DataFrame
print(df.describe())

# Homework 2
# 1. Create a DataFrame
data = {"Month": ["Jan", "Feb", "Mar", "Apr"], "Sales": [5000, 6000, 7500, 8000],
        "Expenses": [3000, 3500, 4000, 4500]}
df2 = pd.DataFrame(data)

# 2. Calculate and display the maximum sales and expenses
max_sales = df2["Sales"].max()
max_expenses = df2["Expenses"].max()
print(f"Maximum Sales: {max_sales}, Maximum Expenses: {max_expenses}")

# 3. Calculate and display the minimum sales and expenses
min_sales = df2["Sales"].min()
min_expenses = df2["Expenses"].min()
print(f"Minimum Sales: {min_sales}, Minimum Expenses: {min_expenses}")

# 4. Calculate and display the average sales and expenses
avg_sales = df2["Sales"].mean()
avg_expenses = df2["Expenses"].mean()
print(f"Average Sales: {avg_sales}, Average Expenses: {avg_expenses}")

# Homework 3
# 1. Create a DataFrame
data = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
}
df3 = pd.DataFrame(data)

# 2. Calculate and display the maximum expense for each category
max_expenses_by_category = df3[["January", "February", "March", "April"]].max()
print("Maximum Expenses by Category:")
print(max_expenses_by_category)

# 3. Calculate and display the minimum expense for each category
min_expenses_by_category = df3[["January", "February", "March", "April"]].min()
print("Minimum Expenses by Category:")
print(min_expenses_by_category)

# 4. Calculate and display the average expense for each category
avg_expenses_by_category = df3[["January", "February", "March", "April"]].mean()
print("Average Expenses by Category:")
print(avg_expenses_by_category)

# Set 'Category' as index
df3.set_index("Category", inplace=True)
print("\nDataFrame with Category as Index:")
print(df3)