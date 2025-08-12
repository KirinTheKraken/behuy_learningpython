#1
score = float(input("Enter your score (0–100): "))

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
elif 50 <= score < 60:
    grade = "D"
elif 0 <= score < 50:
    grade = "F"
else:
    grade = None
    print("Invalid score.")

if grade:
    print(f"Your grade is {grade}")

#2
month = input("Enter month: ").strip().capitalize()

if month in ("September", "October", "November"):
    season = "Autumn"
elif month in ("December", "January", "February"):
    season = "Winter"
elif month in ("March", "April", "May"):
    season = "Spring"
elif month in ("June", "July", "August"):
    season = "Summer"
else:
    season = None

if season:
    print(f"The season is {season}.")
else:
    print("Invalid month entered.")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)
