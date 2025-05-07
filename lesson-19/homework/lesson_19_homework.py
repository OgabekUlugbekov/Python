import pandas as pd
import sqlite3

# Homework Assignment 1: E-commerce Sales Data
sales_df = pd.read_csv('task\\sales_data.csv')

# 1. Group by Category and calculate aggregate statistics
# Total quantity sold, average price per unit, maximum quantity sold in a single transaction
q1 = sales_df.groupby('Category').agg({
    'Quantity': ['sum', 'max'],
    'Price': 'mean'
}).reset_index()
q1.columns = ['Category', 'Total_Quantity', 'Max_Quantity', 'Avg_Price']
print("HW1 Q1:\n", q1)

# 2. Identify the top-selling product in each category based on total quantity sold
q2 = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
q2 = q2.loc[q2.groupby('Category')['Quantity'].idxmax()]
print("HW1 Q2:\n", q2)

# 3. Find the date with the highest total sales (quantity * price)
sales_df['Total_Sales'] = sales_df['Quantity'] * sales_df['Price']
q3 = sales_df.groupby('Date')['Total_Sales'].sum().reset_index()
q3 = q3.loc[q3['Total_Sales'].idxmax()]
print("HW1 Q3:\n", q3)

# Homework Assignment 2: Customer Orders
orders_df = pd.read_csv('task\\customer_orders.csv')

# 1. Group by CustomerID and filter customers with less than 20 orders
q1 = orders_df.groupby('CustomerID').size().reset_index(name='Order_Count')
q1 = q1[q1['Order_Count'] < 20]
print("HW2 Q1:\n", q1)

# 2. Identify customers with average price per unit greater than $120
q2 = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
q2 = q2[q2['Price'] > 120]
print("HW2 Q2:\n", q2)

# 3. Total quantity and price for each product, filter products with total quantity < 5
q3 = orders_df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': 'sum'
}).reset_index()
q3 = q3[q3['Quantity'] >= 5]
print("HW2 Q3:\n", q3)

# Homework Assignment 3: Population Salary Analysis
# Step 1: Connect to SQLite database
conn = sqlite3.connect('task\\population.db')

# Step 2: Use SQL to categorize population by Salary Band
# Assuming the salary bands are defined in 'task\\population_salary_analysis.xlsx'
# For simplicity, let's assume salary bands are: <30k, 30k-50k, 50k-70k, >70k
query = """
SELECT *,
    CASE
        WHEN Salary < 30000 THEN '<30k'
        WHEN Salary BETWEEN 30000 AND 50000 THEN '30k-50k'
        WHEN Salary BETWEEN 50000 AND 70000 THEN '50k-70k'
        ELSE '>70k'
    END AS Salary_Band
FROM population
"""
pop_df = pd.read_sql_query(query, conn)
conn.close()

# Calculate percentage of population and other metrics for each salary category
total_population = len(pop_df)
q2 = pop_df.groupby('Salary_Band').agg({
    'Salary': ['mean', 'median', 'count']
}).reset_index()
q2.columns = ['Salary_Band', 'Avg_Salary', 'Median_Salary', 'Count']
q2['Percentage'] = (q2['Count'] / total_population) * 100
print("HW3 Q2:\n", q2)

# Step 3: Calculate the same measures by State
q3 = pop_df.groupby('State').agg({
    'Salary': ['mean', 'median', 'count']
}).reset_index()
q3.columns = ['State', 'Avg_Salary', 'Median_Salary', 'Count']
q3['Percentage'] = (q3['Count'] / total_population) * 100
print("HW3 Q3:\n", q3)