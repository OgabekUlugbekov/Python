import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 1: Student Grades
data1 = {
    'Student ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print("Exercise 1: Average Grade for Each Student:")
print(df1[['Student ID', 'Average']])

# Exercise 2: Find the student with the highest average grade
top_student = df1.loc[df1['Average'].idxmax()]
print("\nExercise 2: Student with Highest Average Grade:")
print(f"Student ID: {top_student['Student ID']}, Average: {top_student['Average']}")

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print("\nExercise 3: Student Grades with Total Marks:")
print(df1)

# Exercise 4: Plot a bar chart to visualize the average grades in each subject
avg_grades = df1[['Math', 'English', 'Science']].mean()
avg_grades.plot(kind='bar', title='Average Grades by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Grade')
plt.show()

# DataFrame 2: Sales Data
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product A': [120, 150, 130, 110, 140, 160, 135, 125, 155, 145],
    'Product B': [90, 110, 100, 95, 105, 98, 88, 102, 112, 115],
    'Product C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product
total_sales = df2[['Product A', 'Product B', 'Product C']].sum()
print("\nExercise 1: Total Sales for Each Product:")
print(total_sales)

# Exercise 2: Find the date with the highest total sales
df2['Total Sales'] = df2[['Product A', 'Product B', 'Product C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total Sales'].idxmax(), 'Date']
print("\nExercise 2: Date with Highest Total Sales:")
print(max_sales_date)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day
df2[['Product A', 'Product B', 'Product C']] = df2[['Product A', 'Product B', 'Product C']].pct_change() * 100
print("\nExercise 3: Percentage Change in Sales:")
print(df2[['Date', 'Product A', 'Product B', 'Product C']])

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time
df2[['Product A', 'Product B', 'Product C']].plot(title='Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# DataFrame 3: Employee Information
data3 = {
    'Employee ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 68000, 78000, 69000, 76000, 72000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean()
print("\nExercise 1: Average Salary for Each Department:")
print(avg_salary_by_dept)

# Exercise 2: Find the employee with the most experience
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nExercise 2: Employee with Most Experience:")
print(f"Name: {most_experienced['Name']}, Experience: {most_experienced['Experience (Years)']} years")

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("\nExercise 3: Employee Data with Salary Increase:")
print(df3)

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments
df3['Department'].value_counts().plot(kind='bar', title='Distribution of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()

# DataFrame 4: Customer Orders
data4 = {
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Order_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Customer': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'C'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders
total_revenue = df4['Total Price'].sum()
print("\nExercise 1: Total Revenue from All Orders:")
print(total_revenue)

# Exercise 2: Find the most ordered product
most_ordered = df4['Product'].value_counts().idxmax()
print("\nExercise 2: Most Ordered Product:")
print(most_ordered)

# Exercise 3: Calculate the average quantity of products ordered
avg_quantity = df4['Quantity'].mean()
print("\nExercise 3: Average Quantity of Products Ordered:")
print(avg_quantity)

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
sales_by_product = df4.groupby('Product')['Total Price'].sum()
sales_by_product.plot(kind='pie', title='Distribution of Sales Across Products', autopct='%1.1f%%')
plt.ylabel('')
plt.show()