#1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

#2
my_age = 30  # Có thể thay đổi (hoặc cố định)
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    year_word = "year" if diff == 1 else "years"
    print(f"You are {diff} {year_word} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    year_word = "year" if diff == 1 else "years"
    print(f"I am {diff} {year_word} older than you.")
else:
    print("We are the same age.")

#3
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
