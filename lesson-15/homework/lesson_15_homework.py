import sqlite3

# 1. Create database and table
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)''')

# 2. Populate the table
cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# 3. Update Jadzia Dax to Ezri Dax
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# 4. Display Name and Age of Bajorans
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Commit changes and close connection
conn.commit()
conn.close()