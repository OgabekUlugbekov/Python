# 1. Task: JSON Parsing
import json

with open("students.json", "r") as file:
    students = json.load(file)
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# 2. Task: Weather API
import requests

city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data")

# 3. Task: JSON Modification
import json

def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

books = load_books()
while True:
    print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        books.append({"title": title, "author": author})
        save_books(books)
    elif choice == "2":
        title = input("Enter book title to update: ")
        for book in books:
            if book["title"] == title:
                book["author"] = input("Enter new author: ")
                save_books(books)
                break
    elif choice == "3":
        title = input("Enter book title to delete: ")
        books = [book for book in books if book["title"] != title]
        save_books(books)
    elif choice == "4":
        break

# 4. Task: Movie Recommendation System
import requests
import random

genre = input("Enter a movie genre (e.g., Action, Comedy): ")
url = f"http://www.omdbapi.com/?apikey=YOUR_API_KEY&type=movie&s={genre}"
response = requests.get(url)
data = response.json()
if data["Response"] == "True":
    movies = data["Search"]
    movie = random.choice(movies)
    print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
else:
    print("No movies found for this genre")