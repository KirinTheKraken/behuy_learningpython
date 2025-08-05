#Day 2: 30 Days of python programming
#exercise1
firstName = "Bế"
lastName = "Huy"
fullName = "Bế Gia Huy"
country = "VietNam"
city = "Cao Bang"
age = 16
year = 2025
ismarried = False
isTrue = True
isLightOn = True

favoriteSport, favoriteNumber, loveCoding = "Basketball", 11, True

#exercise2
#1. Checking data types
print("firstName: ", type(firstName))
print("lastName: ", type(lastName))
print("fullName: ", type(fullName))
print("country: ", type(country))
print("city: ", type(city))
print("age: ", type(age))
print("year: ", type(year))
print("isMarried: ", type(ismarried))
print("IsTrue: ", type(isTrue))
print("isLightOn: ", type(isLightOn))

#2. Finding the length of firstName
print(len(firstName))

#3. Comparing first and last name
print(len(firstName) == len(lastName))

#4. Declaring numone and numtwo
numone, numtwo = 5, 4

#5. Adding
total = numone + numtwo

print(total)

#6. Subtracting
diff = numone - numtwo

print(diff)

# 7. Multiply
product = numone * numtwo

# 8. Division
division = numone / numtwo

# 9. Modulus
remainder = numtwo % numone

# 10. Exponentiation
exp = numone ** numtwo

# 11. Floor Division
floordivision = numone // numtwo

# Checking
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floordivision)

#12. Getting data from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print("Hello,", first_name, last_name + " from", country + ".", "You are", age, "years old.")

#13. keywords
help('keywords')