# 1. Age Calculator
from datetime import datetime
birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.now()
age = today - birth_date
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30
print(f"Age: {years} years, {months} months, {days} days")

# 2. Days Until Next Birthday
from datetime import datetime
birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.now()
next_birthday = datetime(today.year, birth_date.month, birth_date.day)
if today > next_birthday:
    next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
days_remaining = (next_birthday - today).days
print(f"Days until next birthday: {days_remaining}")

# 3. Meeting Scheduler
from datetime import datetime, timedelta
current_time = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
duration = input("Enter meeting duration (hours minutes, e.g., 2 30): ").split()
hours, minutes = int(duration[0]), int(duration[1])
duration_total = timedelta(hours=hours, minutes=minutes)
end_time = current_time + duration_total
print(f"Meeting ends at: {end_time.strftime('%Y-%m-%d %H:%M')}")

# 4. Timezone Converter
from datetime import datetime
import pytz
current_time = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
current_tz = input("Enter current timezone (e.g., UTC, US/Pacific): ")
target_tz = input("Enter target timezone (e.g., Europe/London): ")
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
current_tz = pytz.timezone(current_tz)
target_tz = pytz.timezone(target_tz)
localized_time = current_tz.localize(current_time)
converted_time = localized_time.astimezone(target_tz)
print(f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M %Z')}")

# 5. Countdown Timer
from datetime import datetime
import time
future_time = input("Enter future date and time (YYYY-MM-DD HH:MM): ")
future_time = datetime.strptime(future_time, "%Y-%m-%d %H:%M")
while True:
    now = datetime.now()
    remaining = future_time - now
    if remaining.total_seconds() <= 0:
        print("Countdown finished!")
        break
    print(f"Time remaining: {remaining}")
    time.sleep(1)

# 6. Email Validator
import re
email = input("Enter an email address: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

# 7. Phone Number Formatter
phone = input("Enter phone number (e.g., 1234567890): ")
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(formatted)

# 8. Password Strength Checker
password = input("Enter a password: ")
if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password)):
    print("Password is strong")
else:
    print("Password is weak")

# 9. Word Finder
text = "This is a sample text with sample words"
word = input("Enter a word to search for: ")
occurrences = [i for i in range(len(text.split())) if text.split()[i] == word]
print(f"Occurrences of '{word}' at indices: {occurrences}")

# 10. Date Extractor
import re
text = input("Enter text: ")
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print("Dates found:", dates)