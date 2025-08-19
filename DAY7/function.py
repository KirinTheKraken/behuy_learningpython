#Level 1
#1
def add_two_numbers(x, y):
    sum = x + y
    return sum

import math

#2
def calculate_area(r):
    area = math.pi * r * r

#3
def add_all_nums(*numbers):
    total = 0

    for number in numbers:
        if not isinstance(number, (int, float)):
            return "Error"
        total += number

#4
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32

#5
def check_season(month):
    month = month.strip().lower()  # normalize input
    
    if month in ("september", "october", "november"):
        return "Autumn"
    elif month in ("december", "january", "february"):
        return "Winter"
    elif month in ("march", "april", "may"):
        return "Spring"
    elif month in ("june", "july", "august"):
        return "Summer"
#6
def calculate_slope(x1, x2, y1, y2):
    if x2 == x1:
        return "Error: verticle line"
    slope = (y2 - y1) / (x2 - x1)
    return slope

import cmath

#7
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Error: a cannot be 0"
    delta = (b**2) - (4*a*c)
    sqrt_delta = cmath.sqrt(delta)  # handles both real & complex
    
    if delta > 0:
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return(x1,x2)
    elif delta == 0:
        x = -b / (2*a) 
        return(x,) 
    elif delta < 0:
        print("Phuong trinh vo nghiem")
        return()
#8
def print_list(myList):
    for item in myList:
        print(item)

#9
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  # loop backwards
        reversed_arr.append(arr[i])
    return reversed_arr

#10
def capitalize_list_items(lst):
    capi = []
    for item in lst:
        capi.append(item.capitalize())
    return capi

#11
def add_item(lst, item):
    lst.append(item)
    return lst

#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

#13
def sum_of_numbers(n):
    return sum(range(1, n+1))

#14
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

#15
def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)

#Level 2
#1
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

#2
def factorial(n):
    if n < 0:
        return "Error"
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

#3
def is_empty(x):
    return not bool(x)

#Level 3
#1
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True