import pandas as pd

# Homework 2: StackOverflow Dataset
df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1. Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
q1 = df[df['creationdate'].dt.year < 2014]
print("HW2 Q1:\n", q1)

# 2. Find all questions with a score more than 50
q2 = df[df['score'] > 50]
print("HW2 Q2:\n", q2)

# 3. Find all questions with a score between 50 and 100
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("HW2 Q3:\n", q3)

# 4. Find all questions answered by Scott Boston
q4 = df[df['ans_name'] == 'Scott Boston']
print("HW2 Q4:\n", q4)

# 5. Find all questions answered by the following 5 users
users = ['Scott Boston', 'Mike Pennington', 'Demitri', 'doug', 'unutbu']  # Update with actual users if provided
q5 = df[df['ans_name'].isin(users)]
print("HW2 Q5:\n", q5)

# 6. Find all questions created between March 2014 and October 2014, answered by Unutbu, score < 5
q6 = df[
    (df['creationdate'].dt.year == 2014) &
    (df['creationdate'].dt.month >= 3) &
    (df['creationdate'].dt.month <= 10) &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]
print("HW2 Q6:\n", q6)

# 7. Find all questions with score between 5 and 10 or view count > 10,000
q7 = df[
    ((df['score'].between(5, 10)) | (df['viewcount'] > 10000))
]
print("HW2 Q7:\n", q7)

# 8. Find all questions not answered by Scott Boston
q8 = df[df['ans_name'] != 'Scott Boston']
print("HW2 Q8:\n", q8)

# Homework 3: Titanic Dataset
titanic_df = pd.read_csv('task\\titanic.csv')

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
q1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
print("HW3 Q1:\n", q1)

# 2. Filter Passengers Who Paid More than $100
q2 = titanic_df[titanic_df['Fare'] > 100]
print("HW3 Q2:\n", q2)

# 3. Select Passengers Who Survived and Were Alone
q3 = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print("HW3 Q3:\n", q3)

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
q4 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print("HW3 Q4:\n", q4)

# 5. Select Passengers with Siblings or Spouses and Parents or Children
q5 = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print("HW3 Q5:\n", q5)

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
q6 = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
print("HW3 Q6:\n", q6)

# 7. Select Passengers with Cabins and Fare Greater Than $200
q7 = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]
print("HW3 Q7:\n", q7)

# 8. Filter Passengers with Odd-Numbered Passenger IDs
q8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("HW3 Q8:\n", q8)

# 9. Select Passengers with Unique Ticket Numbers
unique_tickets = titanic_df['Ticket'].value_counts()[titanic_df['Ticket'].value_counts() == 1].index
q9 = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
print("HW3 Q9:\n", q9)

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1
q10 = titanic_df[
    (titanic_df['Name'].str.contains('Miss', case=False, na=False)) &
    (titanic_df['Pclass'] == 1)
]
print("HW3 Q10:\n", q10)